import time
import fop
import utilities as u
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
        nh = u.add()
        if (nh > 0):
            h = resumen(nh)
            fop.writef(fhoras,h)
            hist = time.strftime("%A %d, %b")+" "*(20 - len(time.strftime("%A %d, %b")))+str(nh)+"\t"+str(h)+"\n"
            fop.addf(fhistorial,hist)
            if nh != 4:
                fop.writef(fextras,fop.readf(fextras) + (nh-4 if nh > 4 else -(4-nh)))
        else:
            print("\tNo se pueden agregar horas negativas o 0.\n\n")

def resumen(nh = 0):
    h = fop.readf(fhoras) + nh
    m = int(((480 - h) / 4) // 20)
    d = int(((480 - h) / 4) % 20)
    hr = 480 - h - ((m*20*4) + (d*4))
    print("\tTotal de horas cubiertas:", h)
    u.prestante(480 - h, m, d, hr)
    print("\tLlevamos", fop.readf(fnfaltas), "faltas.")
    u.extras(nh if nh != 0 else 4)
    u.drestante(d, hr)
    return h

def simulacion():
    nh = u.add()
    resumen(nh)

def historial():
    with open(fhistorial,"r") as f:
        print(f.read())

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
