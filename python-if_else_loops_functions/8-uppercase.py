#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= str <= 'z':
            caracter = chr(ord(caracter) - 32)
        elif 'a' <= str <= 'z':
            caracter = chr(ord(caracter) + 32)

        resultado += str
    print("{}".format(resultado))
