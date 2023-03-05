text = "Ella sabe Python"
print(text[0])
print(text[1])
print(text[0:4])
# print(text[999]) sale error porque pasa el limite de caracteres
size = len(text)
print('size => ', size)
print(text[size - 1])
print(text[-1])

# slicing

print(text[0:5]) # 0 es el primer caracter que empieza el texto, y 5 es el numero de caracteres que sacara del texto
