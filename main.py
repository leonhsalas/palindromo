palabra = input("Cual va a ser la palabra ")

palindromo = palabra[::-1]
if palabra == '':
    print("Escribe algo por favor")
elif palabra == palindromo:
    print("Es un palindromo")
else:
    print("No es un palindromo")