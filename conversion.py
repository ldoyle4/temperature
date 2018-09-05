def kelvin_tocelsius(temp):
    """
    Convert a temperature from Kelvin to Celsius
    """
    return temp - 273.15

def celsius_to_fahr(temp):
    """
    Convert a temperature from celsius to Fahrenheit
    """
    return temp * (9/5) +32

def kelvin_to_fahr(temp):
    """
    Convert kelvin to fahrenheit
    """
    temp_c = kelvin_to_celsius(temp)
    result = celsius_to_fahr(temp_c)
    return result
