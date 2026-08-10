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
    except ValueError:
        print('Invalid input LOL!')
    except Exception as e:
        print(f'\nUnexpected Error occurred, {e}')
    


def Menu():
    print('--- Welcome to Unit Converter ---')
    print('\nEnter 0 to start')
    n = int(input())

    if n == 0:
        start()
    else:
        print('Not valid') 
        return


