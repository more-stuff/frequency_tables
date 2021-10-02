import numpy as np
from tabulate import tabulate



print('Como quieres dar los datos')
print('1. sin intervalos')
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
            if Xi[i].__contains__('.'):
                Xi[i] = float(Xi[i])
            else:
                Xi[i] = int(Xi[i])
            i += 1

        X = []

        for num in Xi:
            if not num in X:
                X.append(num)
                X = sorted(X)

        fi = [0] * (len(X))
        for num in Xi:
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

        # variance fashion median
        variance = 0
        fashion = [[0, 0]]
        for column in table:
            variance += ((column[0] - average) ** 2 ) * column[1]

            if column[1] == fashion[0][1]:
                fashion.append([column[0], column[1]])

            if column[1] > fashion[0][1]:
                fashion[0][0] = column[0]
                fashion[0][1] = column[1]



        variance = variance / n

        median = n / 2
        for column in table:
            if column[2] >= median:
                median = column[0]
                break



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
            numParsed = num
            if num.__contains__('.'):
                numParsed = float(numParsed)
            else:
                numParsed = int(numParsed)

            for category in categories:
                if numParsed >= category[0] and numParsed < category[1]:
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


        # variance fashion median
        variance = 0
        fashion = [[0, 0, 0]]
        for column in table:
            variance += ((column[0] - average) ** 2 ) * column[2]

            if column[2] == fashion[0][2]:
                fashion.append([column[0], column[1], column[2]])

            if column[1] > fashion[0][2]:
                fashion[0][0] = column[0]
                fashion[0][1] = column[1]
                fashion[0][2] = column[2]



        variance = variance / n

        median = n / 2
        for column in table:
            if column[3] >= median:
                median = [column[0], column[1]]
                break

    size = len(table[1])



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
        print()

        fashions = ''
        for values in fashion:
            fashions += f" {values[0]},"
        fashions = fashions[:-1]
        print(f"Moda = {fashions}")

        print(f"Mediana = {median}")

    else:
        num1 = []
        num2 = []
        fi = []
        Fi = []
        hi = []
        Hi = []
        porcentaje = []
        mark_class = []

        for column in table:
            num1.append(column[0])
            num2.append(column[1])
            fi.append(column[2])
            Fi.append(column[3])
            hi.append(column[4])
            Hi.append(column[5])
            porcentaje.append(column[7])
            mark_class.append(column[6])
        info = {'num1': num1,
            'num2': num2,
            'fi': fi,
            'Fi': Fi,
            'hi': hi,
            'Hi': Hi,
            'Porcentaje': porcentaje,
            'Marca de clase': mark_class}
        head = ["Intervalo", "Intervalo", "fi", 'Fi', 'hi', 'Hi', 'porcentaje', 'marca de clase']
        print(tabulate(info, headers = head))
        print()

        fashions = ''
        for values in fashion:
            fashions += f" {values[0]} - {values[1]},"
        fashions = fashions[:-1]
        print(f"Moda = {fashions}")

        print(f"Mediana = {median[0]} - {median[1]}")
        print(f"Has introducido {n} numeros")




    print(f"Media = {average}")
    print(f"Desviacion mediana = {average_deviation}")
    print(f"Varianza = {variance}")
else:
    print('Has puesto algo mal vuelve a probar')

