def homeView(): # main menu/home page
    print('')
    print('Press 1: menage member')
    print('Press 2: manage book')
    print('Press 3: manage loan')
    print('Press 4: exit')
    return int(input('# '))

def bookView(): # book manu
    print('Press 1: add book')
    print('Press 2: edit book')
    print('Press 3: delete book')
    return int(input('# '))

def invalidInput():
    print('[+] ERROR!: Invalid input')