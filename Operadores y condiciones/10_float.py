x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# formato string
y_Str = format(y, ".2g")
print('str =>', y_Str)
print(y_Str == str(x))

# formato matematico
print('*' * 10)
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance) # abs => valor absoluto
