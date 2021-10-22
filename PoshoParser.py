import csv

with open('datos.csv', 'r') as file:
    csvReader = csv.reader(file)

    lang = next(csvReader)

    data = list(csvReader)
    '''    
    print(len(lang))
    print(len(data))
    print(len(data[0]))

    print(lang[2], data[0][1], data[0][2])
    print(lang[2], data[1][1], data[1][2])
    print(lang[3], data[0][1], data[0][3])
    print(lang[3], data[1][1], data[1][3])
    print(lang[4], data[0][1], data[0][4])
    print(lang[4], data[1][1], data[1][4])
    '''

    ini = ''

    for i in range(2, len(lang)):
        s = '['+lang[i]+']'

        ini += s + '\n'
        for j in range(len(data)):
            s = str(data[j][1]+'='+data[j][i])
            ini += s
            ini += '\n'
        
        ini += '\n'
    
    enum = 'enum Dialogue {\n'

    for i in range(len(data)):
        enum += str(data[i][0] + '=' + data[i][1] + '\n')
    enum += '}'

    print(ini)
    print(enum)

f = open('newDatos.ini', 'w')
f.write(ini)
f.close()

f = open('Dialogue.enum', 'w')
f.write(ini)
f.close()