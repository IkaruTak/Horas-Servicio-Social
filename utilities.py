import time
import fop
from found import found
from datetime import datetime, timedelta

fextras = found("pfHorasExtras.txt")
fhoras = found("pfHoras.txt")

def extras(nh = 4):
    h = fop.readf(fextras)
    if (nh > 4):
        h += nh-4
    elif (nh < 4):
        h -= 4-nh
    if h > 0:
        print("\tTenemos", h, "horas extra registradas.\n\n")
    elif h < 0:
        print("\tDebemos", (h)*-1 , "horas.\n\n")
    else:
        print("\tNo hay diferencia de horas.\n\n")

def prestante(h, m, d, hr):
    if h > 0:
        msj = "\t" + ("Solo faltan " + str(h) + " horas") if h > 1 else ("Solo falta " + str(h) + " hora")
    else:
        msj = "\tTerminamos!"
    msj += ": " if h > 3 else ""
    if m > 0:
        msj +=  str(m) + " mes" + ("es" if m > 1 else "")
    if d > 0:
        if m > 0:
            msj += ", " if hr > 0 else " y "
        msj += str(d) + " dia" + ("s" if d > 1 else "")
    if hr > 0 and h > 3:
        msj += " y " + str(hr) + " hora" + ("s" if hr > 1 else "")
    msj += ".\n"
    print(msj)

def drestante(d,hr):
    md = datetime.now()
    for i in range(d):
        md = addDay(md)
    if hr > 0:
        md = addDay(md)
    print("\tFinal tentativo:", md.strftime("%A %d, %b"))

def addDay(md):
    md += timedelta(days = 1)
    if (md.weekday() == 5):
        md += timedelta(days = 2)
    return md

def timeFinder(nh = 0):
    h = fop.readf(fhoras) + nh
    m = int(((480 - h) / 4) // 20)
    d = int(((480 - h) / 4) % 20)
    hr = 480 - h - ((m*20*4) + (d*4))
    list = {'h':h, 'm':m, 'd':d, 'hr':hr}
    return list

def add():
    h = fop.readf(fhoras)
    print("\tHasta hoy hemos cubierto", h, "horas\n")
    nh = int(input("\tCuantas horas fueron hoy? "))
    return nh
