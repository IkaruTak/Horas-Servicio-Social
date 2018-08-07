import hfun

while(1):
    print("Que deseas hacer?\n")
    print("1- Agregar horas.")
    print("2- Consultar historial.")
    print("3- Consultar resumen.")
    print("4- Horas extras o pagadas.")
    print("5- Registrar faltas.")
    print("6- Consultar faltas.")
    print("9- Hacer simulacion de horas.")
    print("0- Salir\n")
    menu = input()
    print("\n")
    if (menu == '1'):
        hfun.agregar()
    elif (menu == '2'):
        hfun.historial()
    elif (menu == '3'):
        hfun.resumen()
    elif (menu == '4'):
        hfun.extras()
    elif (menu == '5'):
        hfun.rfaltas()
    elif (menu == '6'):
        hfun.cfaltas()
    elif (menu == '9'):
        hfun.simulacion()
    elif (menu == '0'):
        break
print("Adios")
