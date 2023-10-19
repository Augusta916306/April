"""
program to convert celsius to fahrenheint
"""
def celsius_to_farenheint(celsius):
    """ convert value given to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah


celsius = 25
fah = celsius_to_farenheint(celsius)
print(f"{celsius} degree is {fah} Farenheint")