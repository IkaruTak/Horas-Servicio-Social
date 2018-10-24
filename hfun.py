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
    print("\t\n")
    if (conf == 's' or conf == 'S'):
        h = fop.readf(fhoras)
        print("\tHasta hoy hemos cubierto", h, "horas\n")
        nh = int(input("\tCuantas horas fueron hoy? "))
        if (nh > 0):
            h += nh
            m = int(((480 - h) / 4) // 20)
            d = int(((480 - h) / 4) % 20)
            hr = 480 - h - ((m*20*4) + (d*4))
            print("\tTotal de horas cubiertas:", h)
            prestante(480 - h, m, d, hr)
            fop.writef(fhoras,h)
            hist = time.strftime("%A %d, %b")+" "*(20 - len(time.strftime("%A %d, %b")))+str(nh)+"\t"+str(h)+"\n"
            fop.addf(fhistorial,hist)
            if (nh > 4):
                fop.writef(fextras,fop.readf(fextras)+(nh-4))
            elif (nh < 4):
                h = fop.readf(fextras)
                fop.writef(fextras,fop.readf(fextras)-(4-nh))
        else:
            print("\tNo se pueden agregar horas negativas o 0.\n\n")

def resumen():
    h = fop.readf(fhoras)
    m = int(((480 - h) / 4) // 20)
    d = int(((480 - h) / 4) % 20)
    hr = 480 - h - ((m*20*4) + (d*4))
    print("\tTotal de horas cubiertas:", h)
    prestante(480 - h, m, d, hr)
    d +=  (d//5)*2 + (m * 28)
    md = datetime.now() + timedelta(days = d)
    # md = datetime.strptime("2018-06-01", "%Y-%m-%d") + timedelta(days = d)
    if (md.weekday() == 5):
        md += timedelta(days = 2)
    elif (md.weekday() == 6):
        md += timedelta(days = 1)
    print("\tFinal tentativo: ", md.strftime("%A %d, %b"))
    print("\tLlevamos", fop.readf(fnfaltas), "faltas.\n")
    extras()

def simulacion():
    h = fop.readf(fhoras)
    print("\tHasta hoy hemos cubierto", h, "horas\n")
    nh = int(input("\tCuantas horas fueron hoy? "))
    h += nh
    m = int(((480 - h) / 4) // 20)
    d = int(((480 - h) / 4) % 20)
    hr = 480 - h - ((m*20*4) + (d*4))
    print("\tTotal de horas cubiertas:", h)
    prestante(480 - h, m, d, hr)
    h = fop.readf(fextras)
    if (nh > 4):
        h += nh-4
    if (nh < 4):
        h -= 4-nh
    if h > 0:
        print("\tTenemos", h, "horas extra registradas.\n")
    elif h < 0:
        print("\tDebemos", (h)*-1 , "horas.\n")
    else:
        print("\tNo hay diferencia de horas.\n")
    d +=  (d//5)*2 + (m * 28)
    md = datetime.now() + timedelta(days = d)
    # md = datetime.strptime("2018-06-01", "%Y-%m-%d") + timedelta(days = d)
    if (md.weekday() == 5):
        md += timedelta(days = 2)
    elif (md.weekday() == 6):
        md += timedelta(days = 1)
    print("\tFinal tentativo: ", md.strftime("%A %d, %b"), "\n\n")

def historial():
    with open(fhistorial,"r") as f:
        print(f.read())

def extras():
    h = fop.readf(fextras)
    if h > 0:
        print("\tTenemos", h, "horas extra registradas.\n\n")
    elif h < 0:
        print("\tDebemos", (h)*-1 , "horas.\n\n")
    else:
        print("\tNo hay diferencia de horas.\n\n")

def rfaltas():
    print("\tHace o dentro de cuantos dias fue/sera la falta? ")
    md = datetime.now() + timedelta(days = int(input("\t(-) para dias atras, sin signo para dias adelante: ")))
    hist = md.strftime("%A %d, %b") + "\n"
    fop.addf(ffaltas,hist)
    fop.writef(fnfaltas,fop.readf(fnfaltas)+1)
    print("\n\tNueva falta el dia", hist)
    print("\tLlevamos", fop.readf(fnfaltas), "faltas.\n")
    fop.writef(fextras,fop.readf(fextras)-4)


def cfaltas():
    with open(ffaltas,"r") as f:
        print(f.read())

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
