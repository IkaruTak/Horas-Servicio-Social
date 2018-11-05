import time
from fop import readf as rf
from found import found
from datetime import datetime, timedelta

fextras = found("pfHorasExtras.txt")
fhoras = found("pfHoras.txt")

def extras(nh):
    h = rf(fextras)
    if (nh > 4):
        h += nh-4
    elif (nh < 4):
        h -= 4-nh
    if h > 0:
        print("\tTenemos", h, "hora" + ("s" if h > 1 else ""), "extra registrada" + ("s." if h > 1 else "."))
    elif h < 0:
        print("\tDebemos", (h)*-1 , "hora" + ("s." if h < -1 else "."))
    else:
        print("\tNo hay diferencia de horas.\n")
        return
    print("\t(Ya incluida" + ("s" if h > 1 else ""), "en el conteo)\n")

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
    print("\tFinal tentativo:", md.strftime("%A %d, %b"), "\n\n")

def addDay(md):
    md += timedelta(days = 1)
    if (md.weekday() == 5):
        md += timedelta(days = 2)
    return md

def add():
    h = rf(fhoras)
    print("\tHasta hoy hemos cubierto", h, "horas\n")
    nh = int(input("\tCuantas horas fueron hoy? "))
    return nh
