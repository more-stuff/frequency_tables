from typing import OrderedDict
import numpy as np
from numpy.lib.function_base import average
from pandas import DataFrame
from timeit import timeit
from tabulate import tabulate



print('Como quieres dar los datos')
print('1. sin intervalor')
print('2. con intervalos')
typeGettingData = input()

if typeGettingData.isnumeric():
    typeGettingData = int(typeGettingData)
    if typeGettingData > 3 or typeGettingData < 0:
        print('Has puesto algo mal vuelve a probar')

    if typeGettingData == 1:
        print('Pon los numeros separados por espacios')
        Xi = input()
        Xi = Xi.split(' ')
        if Xi[len(Xi) - 1] == '':
            Xi.pop()

        i = 0
        while i < len(Xi):
            Xi[i] = int(Xi[i])
            i += 1

        X = []

        for num in Xi:
            if not num in X:
                X.append(num)
                X = sorted(X)

        fi = [0] * (len(X))
        for num in Xi:
#            print(fi[X.index(num)])
            fi[X.index(num)] += 1




        table = np.zeros((len(X), 6))
        # fi
        i = 0
        while i < len(X):
            table[i, 0] = X[i]
            i += 1

        for column in table:
            column[1] = fi[0]
            fi.pop(0)

        # Fi
        i = 0
        while i < len(table):
            nc = i
            if nc == 0:
                table[i, 2] = table[0, 1]
            else:
                while nc > -1:
                    table[i, 2] += table[nc, 1]
                    nc -= 1
            i += 1
        n = table[len(table) - 1, 2]

        # hi
        for column in table:
            column[3] = column[1] / n

        # Hi
        i = 0
        while i < len(table):
            nc = i
            if nc == 0:
                table[i, 4] = table[0, 3]
            else:
                while nc > -1:
                    table[i, 4] += table[nc, 3]
                    nc -= 1
            i += 1

        # %
        for column in table:
            column[5] = column[3] * 100

        # average
        average = 0
        for column in table:
            average += column[0] * column[1]
        average = average / n

        # average deviation
        average_deviation = 0
        for column in table:
            average_deviation += (column[0] - average) * column[1]

        average_deviation = average_deviation / n

        # variance
        variance = 0
        for column in table:
            variance += ((column[0] - average) ** 2 )* column[1]

        variance = variance / n


    else:
        num_categories = input('Cuantas categorias quieres? ')
        if num_categories.isnumeric():
            num_categories = int(num_categories)
        table = np.zeros((num_categories, 8))

        # introduce the categories
        categories = []
        for column in table:
            print('Introduce una categoria')
            print('Pon los dos numeros de la categoria separados por un espacio')
            category = input()
            category = category.split(' ')
            category[0] = int(category[0])
            category[1] = int(category[1])
            categories.append(category)

            column[0] = category[0]
            column[1] = category[1]

        print('Pon los numeros separados por espacios')
        Xi = input()
        Xi = Xi.split(' ')
        if Xi[len(Xi) - 1] == '':
            Xi.pop()

        # fi
        for num in Xi:
            for category in categories:
                if int(num) >= category[0] and int(num) < category[1]:
                    for column in table:
                        if column[0] == category[0] and column[1] == category[1]:
                            column[2] += 1

        # Fi
        i = 0
        while i < len(table):
            nc = i
            if nc == 0:
                table[i, 3] = table[0, 2]
            else:
                while nc > -1:
                    table[i, 3] += table[nc, 2]
                    nc -= 1
            i += 1
        n = table[len(table) - 1, 3]

        print(n)
        # hi
        for column in table:
            column[4] = column[2] / n

        # Hi
        i = 0
        while i < len(table):
            nc = i
            if nc == 0:
                table[i, 5] = table[0, 4]
            else:
                while nc > -1:
                    table[i, 5] += table[nc, 4]
                    nc -= 1
            i += 1

        # class mark
        for column in table:
            column[6] = (column[0] + column[1]) / 2

        # %
        for column in table:
            column[7] = column[4] * 100

        # average
        average = 0
        for column in table:
            average += column[6] * column[2]
        average = average / n

        # average deviation
        average_deviation = 0
        for column in table:
            average_deviation += (column[0] - average) * column[1]

        average_deviation = average_deviation / n

        # variance
        variance = 0
        for column in table:
            variance += ((column[0] - average) ** 2 )* column[1]

        variance = variance / n

    size = len(table[1])
    print(size)

    

    

    if size == 6:
        X = []
        fi = []
        Fi = []
        hi = []
        Hi = []
        porcentaje = []

        for column in table:
            X.append(column[0])
            fi.append(column[1])
            Fi.append(column[2])
            hi.append(column[3])
            Hi.append(column[4])
            porcentaje.append(column[5])

        info = {'X': X,
            'fi': fi,
            'Fi': Fi,
            'hi': hi,
            'Hi': Hi,
            'Porcentaje': porcentaje}
        head = ["X", "fi", 'Fi', 'hi', 'Hi', 'porcentaje']

        print(tabulate(info, headers = head))

    else:
        X = []
        fi = []
        Fi = []
        hi = []
        Hi = []
        porcentaje = []
        mark_class = []

        for column in table:
            X.append(column[0])
            fi.append(column[1])
            Fi.append(column[2])
            hi.append(column[3])
            Hi.append(column[4])
            porcentaje.append(column[5])
            mark_class.append(column[6])
        info = [{'X': X,
            'fi': fi,
            'Fi': Fi,
            'hi': hi,
            'Hi': Hi,
            'Porcentaje': porcentaje,
            'Marca de clase': mark_class}]
        head = ["X", "fi", 'Fi', 'hi', 'Hi', 'porcentaje']
        print(tabulate(info, headers = head))

    print()
    print(f"Media = {average}")
    print(f"Desviacion mediana = {average_deviation}")
    print(f"Varianza = {variance}")
else:
    print('Has puesto algo mal vuelve a probar')

