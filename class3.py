import random
while True:
    a = input()
    if a =='Hi':
        print('Hi')

    if a == 'pogoda':
        weather = random.randint(1,3)
        if weather == 1:
            print('Segodnya solnechno')
        elif weather == 2:
            print('Segodnya budet dojd')
        elif weather == 3:
            print('Segodnya u nas sneg')
        print('poshli gulyat')

        c = input()
        if c == 'kuda':
            if weather == 3:
                venue = random.randint(1,3)
                if venue == 1:
                    print('poidem na katok')
                elif venue == 2:
                    print('poidem na lyji')
                elif venue == 3:
                    print('poidem v gory')
            if weather == 2:
                venue1 = random.randint(1,3)
                if venue1 == 1:
                    print('vozmi zont i poidem v kafe')
                if venue1 == 2:
                    print('poidem v kino')
                if venue1 == 3:
                    print('poshli v biblioteku')
            if weather == 1:
                venue3 = random.randint(1,3)
                if venue3 == 1:
                    print('poidem v Asanbai')
                if venue3 == 2:
                    print('poidem v SunClub')
                if venue3 == 3:
                    print('poidem  na ozero')
        answer = input()
        if answer == 'ok' or answer == 'horosho':
            print('Vse poshli!')
        elif answer != 'ok' or answer != 'horosho':
            print()



























