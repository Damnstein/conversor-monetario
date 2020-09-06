# El usuario ingresa la cantidad de pesos que quiere
# convertir a dolares mediante la funcion input()
pesos = input("¿Cuántos pesos colombianos tienes?: ")

# Modificamos la variable con la funcion float()
# pasandola a un numero decimal (variable del tipo float)
pesos = float(pesos)

# Establecemos en una variable "valor_dolar", el valor
# del dolar con respecto al peso colombiano
valor_dolar = 3875

# Establecemos una variable "dolares", cuyo valor sera
# el de la variable "pesos" dividida a la variable
# "valor_dolar"
dolares = pesos / valor_dolar

# Modificamos la variable dolares con la funcion "round()"
# dandole como parametros el nombre de la variable que 
# queremos modificar y la cantidad de decimales que queremos
# dejar en su valor.
dolares = round(dolares, 2)

# Modificamos la variable "dolares" convirtiendo 
# su TIPO DE VALOR a un TIPO STRING (texto)
dolares = str(dolares)

# Para finalizar, con la funcion "print()" imprimiremos en 
# la consola, una concatencion (suma de textos) de 
# la informacion obtenida por nuestro programa :)
print("Tenes $" + dolares + " dólares")