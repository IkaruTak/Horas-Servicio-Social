import time
import fop
from found import found
from datetime import datetime, timedelta

fhoras = found("pfHoras.txt")
fhistorial = found("pfHistorial.txt")
fextras = found("pfHorasExtras.txt")
ffaltas = found("pfFaltas.txt")
fnfaltas = found("pfNFaltas.txt")

def agregar():
    conf = input("Estas seguro de querer agregar horas? ")
    print("\n")
    if (conf == 's' or conf == 'S'):
        h = fop.readf(fhoras)
        print("Hasta hoy hemos cubierto", h, "horas\n")
        nh = int(input("Cuantas horas fueron hoy? "))
        if (nh > 0):
            h += nh
            m = int(((480 - h) / 4) // 20)
            d = int(((480 - h) / 4) % 20)
            hr = 480 - h - ((m*20*4) + (d*4))
            print("Total de horas cubiertas:", h)
            if hr > 0:
                print("Solo faltan", 480 - h, "horas:", m, "meses,", d, "dias y", hr, "horas.\n")
            else:
                print("Solo faltan", 480 - h, "horas:", m, "meses y", d, "dias.\n")
            fop.writef(fhoras,h)
            hist = time.strftime("%A %d, %b")+" "*(20 - len(time.strftime("%A %d, %b")))+str(nh)+"\t"+str(h)+"\n"
            fop.addf(fhistorial,hist)
            if (nh > 4):
                fop.writef(fextras,fop.readf(fextras)+(nh-4))
            elif (nh < 4):
                h = fop.readf(fextras)
                fop.writef(fextras,fop.readf(fextras)-(4-nh))
        else:
            print("No se pueden agregar horas negativas o 0.")

def resumen():
    h = fop.readf(fhoras)
    m = int(((480 - h) / 4) // 20)
    d = int(((480 - h) / 4) % 20)
    hr = 480 - h - ((m*20*4) + (d*4))
    print("Total de horas cubiertas:", h)
    if hr > 0:
        print("Solo faltan", 480 - h, "horas:", m, "meses,", d, "dias y", hr, "horas.\n")
    else:
        print("Solo faltan", 480 - h, "horas:", m, "meses y", d, "dias.\n")
    print("Llevamos", fop.readf(fnfaltas), "faltas.\n")
    extras()

def simulacion():
    h = fop.readf(fhoras)
    print("Hasta hoy hemos cubierto", h, "horas\n")
    nh = int(input("Cuantas horas fueron hoy? "))
    h += nh
    m = int(((480 - h) / 4) // 20)
    d = int(((480 - h) / 4) % 20)
    hr = 480 - h - ((m*20*4) + (d*4))
    print("Total de horas cubiertas:", h)
    if hr > 0:
        print("Solo faltan", 480 - h, "horas:", m, "meses,", d, "dias y", hr, "horas.\n")
    else:
        print("Solo faltan", 480 - h, "horas:", m, "meses y", d, "dias.\n")

def historial():
    with open(fhistorial,"r") as f:
        print(f.read())

def extras():
    h = fop.readf(fextras)
    if h > 0:
        print("Tenemos", h, "horas extra registradas.\n")
    elif h < 0:
        print("Debemos", (h)*-1 , "horas.\n")
    else:
        print("No hay diferencia de horas.\n")

def rfaltas():
    print("Hace o dentro de cuantos dias fue/sera la falta? ")
    md = datetime.now() + timedelta(days = int(input("(-) para dias atras, sin signo para dias adelante: ")))
    hist = md.strftime("%A %d, %b") + "\n"
    fop.addf(ffaltas,hist)
    fop.writef(fnfaltas,fop.readf(fnfaltas)+1)
    print("\nNueva falta el dia", hist)
    print("Llevamos", fop.readf(fnfaltas), "faltas.\n")
    fop.writef(fextras,fop.readf(fextras)-4)


def cfaltas():
    with open(ffaltas,"r") as f:
        print(f.read())
