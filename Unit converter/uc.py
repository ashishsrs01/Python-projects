# Length/Distance (base: meter)
length_units = {
                "mm": 0.001,
                "cm": 0.01,
                "dm": 0.1,
                "m": 1,
                "dam": 10,
                "hm": 100,
                "km": 1000,
                "inch": 0.0254,
                "ft": 0.3048,
                "yd": 0.9144,
                "mile": 1609.34
}

# Mass/Weight (base: kilogram)
mass_units = {
                "mg": 0.000001,
                "cg": 0.00001,
                "dg": 0.0001,
                "g": 0.001,
                "dag": 0.01,
                "hg": 0.1,
                "kg": 1,
                "t": 1000,
                "oz": 0.0283495,
                "lb": 0.453592,
                "st": 6.35029,
                "us_ton": 907.1847,
                "imp_ton": 1016.05
}

# Temperature (formulas instead of factors)
temperature_units = {
                ("c", "f"): lambda c: (c * 9/5) + 32,
                ("f", "c"): lambda f: (f - 32) * 5/9,
                ("c", "k"): lambda c: c + 273.15,
                ("k", "c"): lambda k: k - 273.15,
                ("f", "k"): lambda f: (f - 32) * 5/9 + 273.15,
                ("k", "f"): lambda k: (k - 273.15) * 9/5 + 32
            }

# Time (base: second)
time_units = {
                "s": 1,
                "min": 60,
                "h": 3600,
                "day": 86400,
                "week": 604800
}

# Speed (base: m/s)
speed_units = {
                "m/s": 1,
                "km/h": 0.277778,
                "mph": 0.44704,
                "knot": 0.514444
}

# Area (base: square meter)
area_units = {
                "m2": 1,
                "cm2": 0.0001,
                "km2": 1e6,
                "ft2": 0.092903,
                "yd2": 0.836127,
                "acre": 4046.86,
                "hectare": 10000
}

# Volume (base: cubic meter)
volume_units = {
                "ml": 0.000001,
                "l": 0.001,
                "m3": 1,
                "cm3": 1e-6,
                "gallon": 0.00378541,
                "pint": 0.000473176,
                "quart": 0.000946353
            }

# Energy (base: joule)
energy_units = {
                "j": 1,
                "kj": 1000,
                "cal": 4.184,
                "kcal": 4184,
                "wh": 3600,
                "kwh": 3.6e6
}

# Pressure (base: pascal)
pressure_units = {
                "pa": 1,
                "bar": 100000,
                "atm": 101325,
                "psi": 6894.76
}

# Data/Storage (base: byte)
data_units = {
                "bit": 0.125,
                "byte": 1,
                "kb": 1024,
                "mb": 1024**2,
                "gb": 1024**3,
                "tb": 1024**4
}


def length(a,b,t):

    try:
        if b not in length_units or t not in length_units:
            raise ValueError('Invalid unit provided')

        result = a * length_units[t] / length_units[b]
        print(result)
    except Exception as e:
        return f'Unexpected error occured: {e}'
    
def mass(a,b,t):

    try:
        if b not in mass_units or t not in mass_units:
            raise ValueError('Invalid unit provided')

        result = a * length_units[t] / length_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def temp(a,b,t):

    try:
        if b not in temperature_units or t not in temperature_units:
            raise ValueError('Invalid unit provided')

        result = a * temperature_units[t] / temperature_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def time(a,b,t):

    try:
        if b not in time_units or t not in time_units:
            raise ValueError('Invalid unit provided')

        result = a * time_units[t] / time_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def speed(a,b,t):

    try:
        if b not in speed_units or t not in speed_units:
            raise ValueError('Invalid unit provided')

        result = a * speed_units[t] / speed_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def area(a,b,t):

    try:
        if b not in area_units or t not in area_units:
            raise ValueError('Invalid unit provided')

        result = a * area_units[t] / area_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def volume(a,b,t):

    try:
        if b not in volume_units or t not in volume_units:
            raise ValueError('Invalid unit provided')

        result = a * volume_units[t] / volume_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def energy(a,b,t):

    try:
        if b not in energy_units or t not in energy_units:
            raise ValueError('Invalid unit provided')

        result = a * energy_units[t] / energy_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def pressure(a,b,t):

    try:
        if b not in pressure_units or t not in pressure_units:
            raise ValueError('Invalid unit provided')

        result = a * pressure_units[t] / pressure_units[b]
        print(result)
    except Exception as e:
            return f'Unexpected error occured: {e}'

def data(a,b,t):

    try:
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
        b = input('Enter the numeric value unit: ').lower()
        t = input('Enter the target unit: ').lower()

        b.replace(' ', '')
        t.replace(' ', '')


        

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


while True:
     converter()