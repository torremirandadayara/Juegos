map = [[' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']]


def print_map():
    global map

    cont = 0
    for coordenada in map:
        cont += 1
        if cont == 3:
            print(coordenada)
            cont = 0
        else:
            print(coordenada, end='')

    return


def conv(x, y):
    conv = {0: [1, 1],
            1: [1, 2],
            2: [1, 3],
            3: [2, 1],
            4: [2, 2],
            5: [2, 3],
            6: [3, 1],
            7: [3, 2],
            8: [3, 3],
            }

    for key in conv:
        if conv[key][0] == x and conv[key][1] == y:
            return key


def update_map(pos, char):
    global map

    if map[pos] == [' ']:
        map[pos] = [char]
    else:
        print('La posición ya estaba ocupada, vuelva a intentarlo')
    return


def winner():
    if map[0] == map[3] == map[6] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[1] == map[4] == map[7] != [' ']:
        print('Winner %s' % map[1])
        return True
    elif map[2] == map[5] == map[8] != [' ']:
        print('Winner %s' % map[2])
        return True

    elif map[0] == map[1] == map[2] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[3] == map[4] == map[5] != [' ']:
        print('Winner %s' % map[3])
        return True
    elif map[6] == map[7] == map[8] != [' ']:
        print('Winner %s' % map[6])
        return True

    elif map[0] == map[4] == map[8] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[6] == map[4] == map[2] != [' ']:
        print('Winner %s' % map[6])
        return True
    else:
        if not [' '] in map:
            print('EMPATE')
            return True
        return False


def ask_data():
    while True:
        try:
            x = int(input('Introduce la coordenada X del 1 al 3: '))
            y = int(input('Introduce la coordenada Y del 1 al 3: '))
            char = str(input('Introduce 0 para círculo o X para cruz: '))
            if 0 <= x <= 3 and y >= 0 and x <= 3:
                if char.lower() == 'x' or char == '0':
                    return x, y, char
            else:
                print('Por favor introduce una coordenada válida')


        except:
            print('Por favor introduce un número entero')


if __name__ == '__main__':

    while True:

        print_map()
        X, Y, CHAR = ask_data()
        POS = conv(X, Y)
        update_map(POS, CHAR)
        if winner():
            print('\n\nReinicio del mapa\n\n')
            map = [[' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']]

1
