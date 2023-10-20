"""Python Statement to convert degree celsius to fahrenheit"""

"""Function to convert temperature from celsius to fahrenheit"""

def celsius_to_farenheit(celsius):
    """ Funtion to convert temperature from celsius to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah

def farenheit_to_celsius(fahrenheit):
    """Function to convert temerature from fahrenheit to celsius"""
    celsius = (fahrenheit- 32) * 5/9
    return celsius

celsius = 25
fah = celsius * 9/5 + 32
print(f"{celsius} celsius degree is {fah} fahrenheit")

celsius = farenheit_to_celsius(fah)
print(f"{fah} degree Fahrenheit is {celsius} celsius")