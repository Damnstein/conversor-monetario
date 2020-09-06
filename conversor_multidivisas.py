def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")

peso_col = 3875
peso_arg = 74
peso_mex = 24


menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu)) #int() convierte a numero entero

if opcion == 1:
    conversor("colombianos", peso_col)
elif opcion == 2:
    conversor("argentinos", peso_arg)
elif opcion == 3:
    conversor("mexicanos", peso_mex)
else:
    print("Elige una opcion válida")