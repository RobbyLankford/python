"""
6.101 Lab 0:
Audio Processing
"""

import wave
import struct


# No additional imports allowed!


def backwards(sound):
    """
    Returns a new sound containing the samples of the original in reverse
    order, without modifying the input sound.

    Args:
        sound: a dictionary representing the original mono sound

    Returns:
        A new mono sound dictionary with the samples in reversed order
    """
    #> Error check: make sure sound is in the correct representation
    if ("rate" not in sound) or ("samples" not in sound):
        print("Argument `sound` is not in the correct representation.")
        return None
    
    return {"rate": sound["rate"], "samples": sound["samples"][::-1]}


def mix(sound1, sound2, p):
    #> Error check: make sure sounds are in the correct representation
    if ("rate" not in sound1) or ("samples" not in sound1):
        print("Argument `sound1` is not in the correct representation.")
        return None 

    if ("rate" not in sound2) or ("samples" not in sound2):
        print("Argument `sound2` is not in the correct representation.")
        return None
    
    #> Error check: the two sounds should have the sampe sampling rates
    if sound1["rate"] != sound2["rate"]:
        print("Arguments `sound1` and `sound2` must have the same error rates.")
        return None
    
    rate = sound1["rate"]
    samples1 = sound1["samples"]
    samples2 = sound2["samples"]
    
    length = min(len(samples1), len(samples2))
    
    new_samples = []
    for i in range(length):
        samp1, samp2 = p * samples1[i], (1 - p) * samples2[i]
        new_samples.append(samp1 + samp2)
    
    return {"rate": rate, "samples": new_samples}


def echo(sound, num_echoes, delay, scale):
    """
    Compute a new signal consisting of several scaled-down and delayed versions
    of the input sound. Does not modify input sound.

    Args:
        sound: a dictionary representing the original mono sound
        num_echoes: int, the number of additional copies of the sound to add
        delay: float, the amount of seconds each echo should be delayed
        scale: float, the amount by which each echo's samples should be scaled

    Returns:
        A new mono sound dictionary resulting from applying the echo effect.
    """
    raise NotImplementedError


def pan(sound):
    samples_left = sound["left"]
    samples_right = sound["right"]
    
    if (len(samples_left) != len(samples_right)):
        print("Length of channel samples is not the same.")
        return None
    
    num_samples = len(samples_left)
    
    new_samples_left = []
    new_samples_right = []
    for i in range(num_samples):
        weight = i / (num_samples - 1)
        
        new_samples_left.append(samples_left[i] * (1 - weight))
        new_samples_right.append(samples_right[i] * weight)
    
    return {"rate": sound["rate"], "left": new_samples_left, "right": new_samples_right}


def remove_vocals(sound):
    samples_left = sound["left"]
    samples_right = sound["right"]
    
    if len(samples_left) != len(samples_right):
        print("Samples in left and right channels are not the same length.")
        return None
    
    new_samples = []
    for i in range(len(samples_left)):
        samp = samples_left[i] - samples_right[i]
        new_samples.append(samp)
    
    return {"rate": sound["rate"], "samples": new_samples}


# below are helper functions for converting back-and-forth between WAV files
# and our internal dictionary representation for sounds


def load_wav(filename, stereo=False):
    """
    Load a file and return a sound dictionary.

    Args:
        filename: string ending in '.wav' representing the sound file
        stereo: bool, by default sound is loaded as mono, if True sound will
            have left and right stereo channels.

    Returns:
        A dictionary representing that sound.
    """
    sound_file = wave.open(filename, "r")
    chan, bd, sr, count, _, _ = sound_file.getparams()

    assert bd == 2, "only 16-bit WAV files are supported"

    out = {"rate": sr}

    left = []
    right = []
    for i in range(count):
        frame = sound_file.readframes(1)
        if chan == 2:
            left.append(struct.unpack("<h", frame[:2])[0])
            right.append(struct.unpack("<h", frame[2:])[0])
        else:
            datum = struct.unpack("<h", frame)[0]
            left.append(datum)
            right.append(datum)

    if stereo:
        out["left"] = [i / (2**15) for i in left]
        out["right"] = [i / (2**15) for i in right]
    else:
        samples = [(ls + rs) / 2 for ls, rs in zip(left, right)]
        out["samples"] = [i / (2**15) for i in samples]

    return out


def write_wav(sound, filename):
    """
    Save sound to filename location in a WAV format.

    Args:
        sound: a mono or stereo sound dictionary
        filename: a string ending in .WAV representing the file location to
            save the sound in
    """
    outfile = wave.open(filename, "w")

    if "samples" in sound:
        # mono file
        outfile.setparams((1, 2, sound["rate"], 0, "NONE", "not compressed"))
        out = [int(max(-1, min(1, v)) * (2**15 - 1)) for v in sound["samples"]]
    else:
        # stereo
        outfile.setparams((2, 2, sound["rate"], 0, "NONE", "not compressed"))
        out = []
        for l_val, r_val in zip(sound["left"], sound["right"]):
            l_val = int(max(-1, min(1, l_val)) * (2**15 - 1))
            r_val = int(max(-1, min(1, r_val)) * (2**15 - 1))
            out.append(l_val)
            out.append(r_val)

    outfile.writeframes(b"".join(struct.pack("<h", frame) for frame in out))
    outfile.close()


if __name__ == "__main__":
    # code in this block will only be run when you explicitly run your script,
    # and not when the tests are being run.  this is a good place to put your
    # code for generating and saving sounds, or any other code you write for
    # testing, etc.

    # here is an example of loading a file (note that this is specified as
    # sounds/hello.wav, rather than just as hello.wav, to account for the
    # sound files being in a different directory than this file)
    song = load_wav("sounds/lookout_mountain.wav", stereo=True)
    
    write_wav(remove_vocals(song), "lookout_mountain_no_vocals.wav")
