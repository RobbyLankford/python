# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis

import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    return [pylab.polyfit(x, y, deg) for deg in degs]

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    mean = pylab.mean(y)
    num = pylab.sum((y - estimated) ** 2)
    denom = pylab.sum((y - mean) ** 2)
    
    return 1 - (num / denom)

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        p = pylab.poly1d(model)
        deg = p.order
        preds = p(x)
        rsq = round(r_squared(y, preds), 2)
        
        #> Plot the data points as individual blue dots
        pylab.plot(x, y, 'bo', label='Data Points')
        
        #> Plot the model as a red solid line
        pylab.plot(x, preds, 'r-', label='Model')
        
        #> Title should inlcude the R-sq value and the degree of the model
        if deg == 1:
            #> If linear curve (degree = 1), title should also include result of `se_over_slope`
            slope_se = round(se_over_slope(x, y, preds, model), 2)
            pylab.title(f"R-Squared: {rsq}\nDegree of fit: {deg}\nRatio of SE: {slope_se}")
        else:
            pylab.title(f"R-Squared: {rsq}\nDegree of fit: {deg}")
        
        pylab.legend(loc='best')
        pylab.xlabel('Year')
        pylab.ylabel('Temperature (C)')
        pylab.show()

def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    temps_yearly_avg = []
    for year in years:
        #> Get yearly tempature for each city
        temps_cities_yearly = pylab.array([climate.get_yearly_temp(city, year) for city in multi_cities])
        
        #> Calculate the average tempature for the year across all cities
        temps_yearly_avg.append(temps_cities_yearly.mean())
    
    return pylab.array(temps_yearly_avg)

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    avg = []
    
    for i, _ in enumerate(y):
        if i < window_length:
            #> If we have fewer than `window_length` years, just average over what we have
            #> This will only occur at the beginning of the list
            years = pylab.array(y[ :(i + 1)])
        else:
            #> Grab the current `window_length` window and average over it
            years = pylab.array(y[(i - window_length + 1):(i + 1)])
        
        avg.append(years.mean())
    
    return pylab.array(avg)
            

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    numer = ((y - estimated) ** 2).sum()
    denom = len(y)
    
    return pylab.sqrt(numer / denom)

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    temps_yearly_stdev = []
    for year in years:
        #> Get yearly tempature for each city
        temps_cities_yearly = pylab.array([climate.get_yearly_temp(city, year) for city in multi_cities])
        
        #> Calculate the standard deviation over the averaged yearly tempature for each city
        temps_yearly_avg = temps_cities_yearly.mean(axis=0)
        temps_yearly_stdev.append(temps_yearly_avg.std(axis=0))
    
    return pylab.array(temps_yearly_stdev)

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        p = pylab.poly1d(model)
        deg = p.order
        preds = p(x)
        rmse_val = round(rmse(y, preds), 3)
        
        #> Plot the data points as individual blue dots
        pylab.plot(x, y, 'bo', label='Data Points')
        
        #> Plot the model as a red solid line
        pylab.plot(x, preds, 'r-', label='Model')
        
        #> Title should include RMSE and the degree of the model
        pylab.title(f"RMSE: {rmse_val}\nDegree of fit: {deg}")
        
        #> Rest of the model
        pylab.legend(loc='best')
        pylab.xlabel('Year')
        pylab.ylabel('Temperature (C)')
        pylab.show()


if __name__ == '__main__':

    pass 

    # Part A.4
    
    #> Problem A.4.I
    
    # ##> Generate data samples
    # data = Climate('data.csv')
    # years = pylab.array(TRAINING_INTERVAL)
    # temps = pylab.array([data.get_daily_temp('NEW YORK', 1, 10, year) for year in years])
    
    # ##> Fit degree-one polynomial
    # models = generate_models(years, temps, [1])
    
    # ##> Plot the regression results
    # evaluate_models_on_training(years, temps, models)
    
    #> Problem A.4.II
    
    # ##> Generate data samples
    # data = Climate('data.csv')
    # years = pylab.array(TRAINING_INTERVAL)
    # temps = pylab.array([data.get_yearly_temp('NEW YORK', year).mean() for year in years])
    
    # ##> Fit degree-one polynomial
    # models = generate_models(years, temps, [1])
    
    # ##> Plot the regression results
    # evaluate_models_on_training(years, temps, models)
    
    # Part B
    
    # #> Generate data samples
    # data = Climate('data.csv')
    # years = pylab.array(TRAINING_INTERVAL)
    # temps = gen_cities_avg(data, CITIES, years)
    
    # #> Fit degree-one polynomial
    # models = generate_models(years, temps, [1])
    
    # #> Plot the regression results
    # evaluate_models_on_training(years, temps, models)

    # Part C
    
    # #> Generate data samples
    # data = Climate('data.csv')
    # years = pylab.array(TRAINING_INTERVAL)
    # temps = moving_average(gen_cities_avg(data, CITIES, years), window_length=5)
    
    # #> Fit degree-one polynomial
    # models = generate_models(years, temps, [1])
    
    # #> Plot the regression results
    # evaluate_models_on_training(years, temps, models)

    # Part D.2
    
    # #> Generate data samples (training)
    # data = Climate('data.csv')
    # years = pylab.array(TRAINING_INTERVAL)
    # temps = gen_cities_avg(data, CITIES, years)
    
    # #> Fit degree-one polynomial
    # models = generate_models(years, temps, [1])
    
    # #> Generate data samples (testing)
    # years_test = pylab.array(TESTING_INTERVAL)
    # temps_test = gen_cities_avg(data, CITIES, years_test)
    
    # #> Plot the regression results
    # evaluate_models_on_testing(years_test, temps_test, models)
    
    #> Problem D.2.I
    
    # #> Generate data samples
    # data = Climate('data.csv')
    # years = pylab.array(TRAINING_INTERVAL)
    # temps = moving_average(gen_cities_avg(data, CITIES, years), window_length=5)
    
    # #> Fit degree-one, -two, and -twenty polynomials
    # models = generate_models(years, temps, [1, 2, 20])
    
    # #> Plot the regression results
    # evaluate_models_on_training(years, temps, models)
    
    #> Problem D.2.II
    
    # #> Generate data samples (training)
    # data = Climate('data.csv')
    # years = pylab.array(TRAINING_INTERVAL)
    # temps = moving_average(gen_cities_avg(data, CITIES, years), window_length=5)
    
    # #> Fit degree-one, -two, and -twenty polynomials
    # models = generate_models(years, temps, [1, 2, 20])
    
    # #> Generate data samples (testing)
    # years_test = pylab.array(TESTING_INTERVAL)
    # temps_test = moving_average(gen_cities_avg(data, CITIES, years_test), window_length=5)
    
    # #> Plot regression results
    # evaluate_models_on_testing(years_test, temps_test, models)

    # Part E
    
    #> Generate data samples
    data = Climate('data.csv')
    years = pylab.array(TRAINING_INTERVAL)
    stdevs = moving_average(gen_std_devs(data, CITIES, years), window_length=5)
    
    #> Fit degree-one polynomial
    models = generate_models(years, stdevs, [1])
    
    #> Plot regression results
    evaluate_models_on_training(years, stdevs, models)
