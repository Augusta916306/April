"""Python Statement to convert degree celsius to fahrenheit"""

"""Function to convert temperature from celsius to fahrenheit"""

def celsius_to_farenheint(celsius):
    """ Funtion to convert value given to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah

celsius = 25
fah = celsius * 9/5 + 32
print(f"{25} celsius degree is {fah} farenheit")