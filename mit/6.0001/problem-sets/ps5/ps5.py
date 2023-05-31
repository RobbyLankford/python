# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Robert Lankford

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """
        Initializes a NewsStory object

        Args:
            guid (string): a globally unique identifier of story
            title (string): the news story's headline
            description (string): a paragraph or so summarizing the news story
            link (string): a link to a website with the entire story
            pubdate (datetime): date the news story was published
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        """Getter Method For self.guid

        Returns:
            str: a globally unique identifier of story
        """
        return self.guid
    
    def get_title(self):
        """Getter Method For self.title

        Returns:
            str: the news story's headline
        """
        return self.title
    
    def get_description(self):
        """Getter Method For self.description

        Returns:
            str: a paragraph or so summarizing the news story
        """
        return self.description
    
    def get_link(self):
        """Getter Method For self.link

        Returns:
            str: a link to a website with the entire story
        """
        return self.link
    
    def get_pubdate(self):
        """Getter Method For self.pubdate

        Returns:
            datetime: date the news story was published
        """
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        """Initializes a PhraseTrigger object

        Args:
            phrase (string): a short phrase searched for in a NewsStory
        """
        self.phrase = phrase
    
    def evaluate(self, story):
        """Returns True if an alert should be generated.

        Args:
            story (NewsStory): a NewsStory object

        Raises:
            NotImplementedError: raised if a trigger is not implemented
        """
        raise NotImplementedError
    
    def clean_text(self, text):
        """Clean arbitrary text to put in a usable format for other functions

        Args:
            text (string): arbitrary text

        Returns:
            list: the same text, but without punctuation, multiple spaces, and split into individual words
        """
        no_punct_lst = []

        #> Replace punctuation with spaces
        for char in text:
            if char in string.punctuation:
                no_punct_lst.append(' ')
            else:
                no_punct_lst.append(char)

        #> Reduce multiple spaces to a single space
        words_lst = ''.join(no_punct_lst).split()
        words_str = ' '.join(words_lst).lower()

        #> Want a list of words to prepare for self.is_phrase_in()
        return words_str.split()
    
    def is_phrase_in(self, text):
        """Determine if a specific phrase is in an aribitrary text

        Args:
            text (string): arbitrary text

        Returns:
            bool: True if all the words in the phrase are found, are in the correct order, and are side-by-side
        """
        phrase_lst = self.clean_text(self.phrase)
        text_lst = self.clean_text(text)

        words_int = len(phrase_lst)
        check_int = 0
        order_lst = []
        space_lst = []
        
        for word in phrase_lst:
            if word in text_lst:
                check_int += 1
                order_lst.append(text_lst.index(word))

        for i in range(len(order_lst) - 1):
            space_lst.append(order_lst[i + 1] - order_lst[i])

        #> Check if all words in the phrase are in the text
        all_words_found_lgl = check_int == words_int
        
        #> Check if words in the phrase appear in the correct order in the text
        correct_order_lgl = order_lst == sorted(order_lst)
        
        #> Check if words in the phrase appear next to each other in the text
        side_by_side_lgl = set(space_lst) == {1}

        return all_words_found_lgl and correct_order_lgl and side_by_side_lgl

# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        """Returns True if a phrase is in the title of a story

        Args:
            story (NewsStory): A NewsStory object

        Returns:
            bool: True or False
        """
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        """Returns True if a phrase is in the description of a story

        Args:
            story (NewsStory): a NewsStory object

        Returns:
            bool: True or False
        """
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        """Initializes a TimeTrigger object

        Args:
            time (string): time in EST and in the format "%d %b %Y %H:%M:%S"
        """
        #> Convert string into datetime (should be in EST already)
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S")

# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        """Return True if story was published before a specific datetime

        Args:
            story (NewsStory): a NewsStory object

        Returns:
            bool: True or False
        """
        try:
            #> Assumes publication date is in EST
            before = story.get_pubdate() < self.time
        except:
            #> Handles if publication date is not in EST
            before = story.get_pubdate() < self.time.replace(tzinfo=pytz.timezone("EST"))
        
        return before

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        """Return True if a story was published after a specific datetime

        Args:
            story (NewsStory): a NewsStory object

        Returns:
            bool: True or False
        """
        try:
            after = story.get_pubdate() > self.time
        except:
            after = story.get_pubdate() > self.time.replace(tzinfo=pytz.timezone("EST"))
        
        return after


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, T):
        """Initializes a NotTrigger object

        Args:
            T (Trigger): a Trigger object
        """
        self.T = T
    
    def evaluate(self, story):
        """Return True if the input trigger is False and vice-versa

        Args:
            story (NewsStory): a NewsStory object

        Returns:
            bool: True or False
        """
        return not self.T.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        """Initializes an AndTrigger object

        Args:
            T1 (Trigger): a Trigger object
            T2 (Trigger): a Trigger object
        """
        self.T1 = T1
        self.T2 = T2
    
    def evaluate(self, story):
        """Return True if both input triggers are triggered on a story

        Args:
            story (NewsStory): a NewsStory object

        Returns:
            bool: True or False
        """
        return self.T1.evaluate(story) and self.T2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        """Initializes an OrTrigger object

        Args:
            T1 (Trigger): a Trigger object
            T2 (Trigger): a Trigger object
        """
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        """Return True if either input triggers are triggered on a story

        Args:
            story (NewsStory): a NewsStory object

        Returns:
            bool: True or False
        """
        return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    stories_filtered = []
    
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                stories_filtered.append(story)
                next
    
    return stories_filtered


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    t_map_dict = {
        "TITLE": TitleTrigger,
        "DESCRIPTION": DescriptionTrigger,
        "AFTER": AfterTrigger,
        "BEFORE": BeforeTrigger,
        "NOT": NotTrigger,
        "AND": AndTrigger,
        "OR": OrTrigger
    }
    
    t_commands_dict = {}
    t_commands_list = []
    
    for line in lines:
        commands = line.split(',')
        
        #> ADD handled differently: add triggers to the trigger list
        if commands[0] == "ADD":
            #> Example: ADD,t1, t2 -> [ADD, t1, t2]
            for trigger in commands[1:]:
                t_commands_list += [t_commands_dict[trigger]]
            
        else:
            t_name = commands[0]
            t_type = commands[1]
            
            #> OrTrigger and AndTrigger have four tokens in the command
            if commands[1] in ["OR", "AND"]:
                #> Example: t4,AND,t1,t2 -> [t4, AND, t1, t2]
                t_1 = t_commands_dict[commands[2]]
                t_2 = t_commands_dict[commands[3]]
                
                t_commands_dict[t_name] = t_map_dict[t_type](t_1, t_2)
            
            #> All other triggers have three tokens in the command
            else:
                #> Example: t1,DESCRIPTION,Presidential Election -> [t1, DESCRIPTION, Presidential Election]
                data = commands[2]
                
                t_commands_dict[t_name] = t_map_dict[t_type](data)

    return t_commands_list

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
