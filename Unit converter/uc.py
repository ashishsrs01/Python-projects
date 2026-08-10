# Length/Distance (base: meter)
length_units = {
                "mm": 0.001,
                "millimeter": 0.001,
                "millimeters": 0.001,
                "cm": 0.01,
                "centimeter": 0.01,
                "centimeters": 0.01,
                "dm": 0.1,
                "decimeter": 0.1,
                "decimeters": 0.1,
                "m": 1,
                "meter": 1,
                "meters": 1,
                "metre": 1,
                "metres": 1,
                "dam": 10,
                "decameter": 10,
                "decameters": 10,
                "dekameter": 10,
                "dekameters": 10,
                "hm": 100,
                "hectometer": 100,
                "hectometers": 100,
                "km": 1000,
                "kilometer": 1000,
                "kilometers": 1000,
                "kilometre": 1000,
                "kilometres": 1000,
                "inch": 0.0254,
                "inches": 0.0254,
                "ft": 0.3048,
                "foot": 0.3048,
                "feet": 0.3048,
                "yd": 0.9144,
                "yard": 0.9144,
                "yards": 0.9144,
                "mile": 1609.34,
                "miles": 1609.34
}

# Mass/Weight (base: kilogram)
mass_units = {
                "mg": 0.000001,
                "milligram": 0.000001,
                "milligrams": 0.000001,
                "cg": 0.00001,
                "centigram": 0.00001,
                "centigrams": 0.00001,
                "dg": 0.0001,
                "decigram": 0.0001,
                "decigrams": 0.0001,
                "g": 0.001,
                "gram": 0.001,
                "grams": 0.001,
                "dag": 0.01,
                "decagram": 0.01,
                "decagrams": 0.01,
                "hg": 0.1,
                "hectogram": 0.1,
                "hectograms": 0.1,
                "kg": 1,
                "kilogram": 1,
                "kilograms": 1,
                "t": 1000,
                "tonne": 1000,
                "tonnes": 1000,
                "metric ton": 1000,
                "metric tons": 1000,
                "oz": 0.0283495,
                "ounce": 0.0283495,
                "ounces": 0.0283495,
                "lb": 0.453592,
                "pound": 0.453592,
                "pounds": 0.453592,
                "st": 6.35029,
                "stone": 6.35029,
                "stones": 6.35029,
                "us_ton": 907.1847,
                "us ton": 907.1847,
                "short ton": 907.1847,
                "short tons": 907.1847,
                "imp_ton": 1016.05,
                "imperial ton": 1016.05,
                "imperial tons": 1016.05,
                "long ton": 1016.05,
                "long tons": 1016.05
}

# Temperature (formulas instead of factors)
temperature_units = {
                ("c", "f"): lambda c: (c * 9/5) + 32,
                ("f", "c"): lambda f: (f - 32) * 5/9,
                ("c", "k"): lambda c: c + 273.15,
                ("k", "c"): lambda k: k - 273.15,
                ("f", "k"): lambda f: (f - 32) * 5/9 + 273.15,
                ("k", "f"): lambda k: (k - 273.15) * 9/5 + 32,
                ("celsius", "fahrenheit"): lambda c: (c * 9/5) + 32,
                ("fahrenheit", "celsius"): lambda f: (f - 32) * 5/9,
                ("celsius", "kelvin"): lambda c: c + 273.15,
                ("kelvin", "celsius"): lambda k: k - 273.15,
                ("fahrenheit", "kelvin"): lambda f: (f - 32) * 5/9 + 273.15,
                ("kelvin", "fahrenheit"): lambda k: (k - 273.15) * 9/5 + 32
            }

# Time (base: second)
time_units = {
                "s": 1,
                "sec": 1,
                "second": 1,
                "seconds": 1,
                "min": 60,
                "minute": 60,
                "minutes": 60,
                "h": 3600,
                "hour": 3600,
                "hours": 3600,
                "day": 86400,
                "days": 86400,
                "week": 604800,
                "weeks": 604800
}

# Speed (base: m/s)
speed_units = {
                "m/s": 1,
                "meter per second": 1,
                "meters per second": 1,
                "metre per second": 1,
                "metres per second": 1,
                "km/h": 0.277778,
                "kilometer per hour": 0.277778,
                "kilometers per hour": 0.277778,
                "kilometre per hour": 0.277778,
                "kilometres per hour": 0.277778,
                "mph": 0.44704,
                "mile per hour": 0.44704,
                "miles per hour": 0.44704,
                "knot": 0.514444,
                "knots": 0.514444,
                "nautical mile per hour": 0.514444
}

# Area (base: square meter)
area_units = {
                "m2": 1,
                "m^2": 1,
                "square meter": 1,
                "square meters": 1,
                "square metre": 1,
                "square metres": 1,
                "cm2": 0.0001,
                "cm^2": 0.0001,
                "square centimeter": 0.0001,
                "square centimeters": 0.0001,
                "square centimetre": 0.0001,
                "square centimetres": 0.0001,
                "km2": 1e6,
                "km^2": 1e6,
                "square kilometer": 1e6,
                "square kilometers": 1e6,
                "square kilometre": 1e6,
                "square kilometres": 1e6,
                "ft2": 0.092903,
                "ft^2": 0.092903,
                "square foot": 0.092903,
                "square feet": 0.092903,
                "yd2": 0.836127,
                "yd^2": 0.836127,
                "square yard": 0.836127,
                "square yards": 0.836127,
                "acre": 4046.86,
                "acres": 4046.86,
                "hectare": 10000,
                "hectares": 10000
}

# Volume (base: cubic meter)
volume_units = {
                "ml": 0.000001,
                "milliliter": 0.000001,
                "milliliters": 0.000001,
                "millilitre": 0.000001,
                "millilitres": 0.000001,
                "l": 0.001,
                "liter": 0.001,
                "liters": 0.001,
                "litre": 0.001,
                "litres": 0.001,
                "m3": 1,
                "m^3": 1,
                "cubic meter": 1,
                "cubic meters": 1,
                "cubic metre": 1,
                "cubic metres": 1,
                "cm3": 1e-6,
                "cm^3": 1e-6,
                "cubic centimeter": 1e-6,
                "cubic centimeters": 1e-6,
                "cubic centimetre": 1e-6,
                "cubic centimetres": 1e-6,
                "gallon": 0.00378541,
                "gallons": 0.00378541,
                "pint": 0.000473176,
                "pints": 0.000473176,
                "quart": 0.000946353,
                "quarts": 0.000946353
            }

# Energy (base: joule)
energy_units = {
                "j": 1,
                "joule": 1,
                "joules": 1,
                "kj": 1000,
                "kilojoule": 1000,
                "kilojoules": 1000,
                "cal": 4.184,
                "calorie": 4.184,
                "calories": 4.184,
                "kcal": 4184,
                "kilocalorie": 4184,
                "kilocalories": 4184,
                "wh": 3600,
                "watt-hour": 3600,
                "watt hours": 3600,
                "watt hour": 3600,
                "watt-hours": 3600,
                "kwh": 3.6e6,
                "kilowatt-hour": 3.6e6,
                "kilowatt hours": 3.6e6,
                "kilowatt hour": 3.6e6,
                "kilowatt-hours": 3.6e6
}

# Pressure (base: pascal)
pressure_units = {
                "pa": 1,
                "pascal": 1,
                "pascals": 1,
                "bar": 100000,
                "atm": 101325,
                "atmosphere": 101325,
                "atmospheres": 101325,
                "psi": 6894.76,
                "pound per square inch": 6894.76,
                "pounds per square inch": 6894.76
}

# Data/Storage (base: byte)
data_units = {
                "bit": 0.125,
                "bits": 0.125,
                "byte": 1,
                "bytes": 1,
                "kb": 1024,
                "kilobyte": 1024,
                "kilobytes": 1024,
                "mb": 1024**2,
                "megabyte": 1024**2,
                "megabytes": 1024**2,
                "gb": 1024**3,
                "gigabyte": 1024**3,
                "gigabytes": 1024**3,
                "tb": 1024**4,
                "terabyte": 1024**4,
                "terabytes": 1024**4
}


def normalize_unit(unit):
    return " ".join(unit.strip().lower().split())


def length(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in length_units or t not in length_units:
            raise ValueError('Invalid unit provided')

        result = a * length_units[t] / length_units[b]
        print(result)
    except Exception as e:
        return f'Unexpected error occured: {e}'
    
def mass(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in mass_units or t not in mass_units:
            raise ValueError('Invalid unit provided')

        result = a * mass_units[t] / mass_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def temp(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)
        key = (b, t)

        if key not in temperature_units:
            raise ValueError('Invalid temperature unit conversion')

        result = temperature_units[key](a)
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def time(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in time_units or t not in time_units:
            raise ValueError('Invalid unit provided')

        result = a * time_units[t] / time_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def speed(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in speed_units or t not in speed_units:
            raise ValueError('Invalid unit provided')

        result = a * speed_units[t] / speed_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def area(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in area_units or t not in area_units:
            raise ValueError('Invalid unit provided')

        result = a * area_units[t] / area_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def volume(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in volume_units or t not in volume_units:
            raise ValueError('Invalid unit provided')

        result = a * volume_units[t] / volume_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def energy(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in energy_units or t not in energy_units:
            raise ValueError('Invalid unit provided')

        result = a * energy_units[t] / energy_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def pressure(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in pressure_units or t not in pressure_units:
            raise ValueError('Invalid unit provided')

        result = a * pressure_units[t] / pressure_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def data(a,b,t):

    try:
        b = normalize_unit(b)
        t = normalize_unit(t)

        if b not in data_units or t not in data_units:
            raise ValueError('Invalid unit provided')

        result = a * data_units[t] / data_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'


def start():

    try:
        print('\nChoose your unit type\n')
        print('1 -> Length/Distance')
        print('2 -> Mass/Weight')
        print('3 -> Temperature')
        print('4 -> Time')
        print('5 -> Speed')
        print('6 -> Area')
        print('7 -> Volume')
        print('8 -> Energy')
        print('9 -> Pressure')
        print('10 -> Data/Storage\n')
        n = int(input())
        a = float(input('\nEnter the numeric Value: '))
        b = input('Enter the numeric value unit: ')
        t = input('Enter the target unit: ')

        b = normalize_unit(b)
        t = normalize_unit(t)

        if n == 1:
             length(a, b, t)
        elif n == 2:
             mass(a, b, t)
        elif n == 3:
             temp(a, b, t)
        elif n == 4:
             time(a, b, t)
        elif n == 5:
             speed(a, b, t)
        elif n == 6:
             area(a, b, t)
        elif n == 7:
             volume(a, b, t)
        elif n == 8:
             energy(a, b, t)
        elif n == 9:
             pressure(a, b, t)
        elif n == 10:
             data(a, b, t)
        else:
             print('Invalid unit type number')
        

    except ValueError:
        print('Invalid input LOL!, please enter numeric value')
    except Exception as e:
        print(f'\nUnexpected Error occurred, {e}')

    


def converter():
    print('--- Welcome to Unit Converter ---')
    print('\nEnter 0 to start')
    n = int(input())

    if n == 0:
        start()
    else:
        print('Not valid') 
        return


if __name__ == '__main__':
    while True:
        converter()