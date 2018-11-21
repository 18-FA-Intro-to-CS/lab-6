from weatherFunctions import *


# DO NOT CHANGE ANYTHING BELOW THIS POINT!
def getDewPoint(temp, humidity):
    dewPoint = calculateDewPoint(temp, humidity)
    dewPoint = round(dewPoint, 0)
    output = ("With a temperature of {0} "
                "and a relative humidity of {1}, "
                "the dew point is {2}.").format(temp, humidity, dewPoint)
    print(output)

def getWindChill(temp, windSpeed):
    windChill = calculateWindChill(temp, windSpeed)
    windChill = round(windChill, 0)
    output = ("With a temperature of {0} "
                "and a wind speed of {1}, "
                "the wind chilld is {2}.").format(temp, windSpeed, windChill)
    print(output)



def main():
    temp = float(input("What is the temperature? "))
    humidity = float(input("What is the relative humidity? "))
    windSpeed = float(input("What is the wind speed? "))

    getDewPoint(temp, humidity)
    getWindChill(temp, windSpeed)

    print()
    print("Have a nice day!")

main()

