# Introduction to Computer Science - Fall 2018

## Lab 6 - It's not the heat, it's the humidity

**Functions as abstractions - Creating a Library:** This lab gives you a chance to practice defining and using functions and putting them in a lbrary. In this lab, you will write two functions. One will compute the dew point and another that computes the wind chill factor. In addition, you will create a library to put those functions in. The lab has been started for you and the files are included in this repository.

**Discussion:** A library is just a collection of Python functions that are stored in their own file - a file that is separate from the html file. Rather than an html extension, a JavaScript library has a js extension. For this exercise, you will place your own functions in your copy of `weatherFunctions.py`. Note that for this lab, keep `weather.py` and `weatherFunctions.py` should be stored in the same directory.

The first step is for you to indicate in your main Python file where to find the library. You will do this with an import statement of the form `from <library> import *`. This will enable you to use any function defined in the library.

The formula for computing the dew point given the temperature and humidity is rather straightforward. It is:

`dewpoint = temperature - (9(100 - humidity) / 25)`

The formula for computing the wind chill is a bit more complex. Here is a simplified version that you can use:

<code>windchill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * wind<sup>0.16</sup></code>

**The Dew Point Function:** Develop a Python function named calculateDewPoint() that will calculate the dew point using the formula described above. The function must have two parameters: the temperature and the humidity. The function must return the dew point.

**The Wind Chill Function:** Develop a Python function named calculateWindChill() that will calculate the wind chill using the formula described above. The function must have two parameters: the temperature and the wind speed. The function must return the wind chill.

Once you have completed the assignment, push it back to the repository for grading.
