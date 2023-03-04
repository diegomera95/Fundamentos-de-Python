text = 'Ella sabe programar en Python'
'''
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien!')
else:
    print('Tambien elegiste bien')
'''
size = len('amor')
print(size)

print(text)
print(text.upper()) # cambia el texto a mayuscula
print(text.lower()) # cambia el texto a minuscula
print(text.count('a')) # cuenta cuantos caracteres tiene el texto

print(text.swapcase()) # cambia las mayusculas por las minusculas y viceversa
print(text.startswith('Ella')) # indica si el texto inicia con un termino en especifico
print(text.endswith('Rust')) # indica si el texto finaliza con un termino en especifico
print(text.replace('Python', 'Go')) # reemplaza caracteres dentro del texto

text2 = 'este es un titulo'
print(text2)
print(text2.capitalize()) # cambia a mayuscula la primera letra
print(text2.title()) # iniicio de cada una de las palabras en mayusculas / sirve como nompropio
print(text2.isdigit()) # nos dice si este texto es un digito
print("398".isdigit())

