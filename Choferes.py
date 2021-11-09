import sqlite3
from datetime import date
from datetime import datetime
import csv
import random
import functools
import operator
conn = sqlite3.connect('choferes.db')
cur = conn.cursor()
conn.execute("""CREATE TABLE IF NOT EXISTS tablaid(
        PROVEEDOR,
        IDPROVEEDOR,
        CONDUCTOR,
        IDCONDUCTOR,
        UNIDAD,
        DOMINIO,
        IDDOMINIO,
        PESO,
        TELEFONO,
        DNI,
        PLANTA,
        RANKING,
        DISPONIBLE);
        """)

def tablaid():
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    que =input("Desea generar base de datos de los TTA?")
    if que == "si":
        with open('tta.csv','r') as fin:
          dr = csv.DictReader(fin)
          for i in dr:
              conn.execute("INSERT INTO tablaid(PROVEEDOR,IDPROVEEDOR,CONDUCTOR,IDCONDUCTOR,UNIDAD,DOMINIO,IDDOMINIO,PESO,TELEFONO,DNI,PLANTA,RANKING,DISPONIBLE) values (:PROVEEDOR,:IDPROVEEDOR,:CONDUCTOR,:IDCONDUCTOR,:UNIDAD,:DOMINIO,:IDDOMINIO,:PESO,:TELEFONO,:DNI,:PLANTA,:RANKING,:DISPONIBLE)", i)
    conn.commit()
    conn.close()
def nuevos():
    a=input("Ingrese Proveedor: \n")
    b=input("Ingrese ID del proveedor: \n")
    c=input("Ingrese Chofer: \n")
    d=input("Ingrese ID del chofer: \n")
    f=input("Ingrese Unidad: \n")
    g=input("Ingrese Dominio: \n")
    h=input("Ingrese ID del dominio: \n")
    i=input("Ingrese Peso: \n")
    j=input("Ingrese Telefono: \n")
    k=input("Ingrese DNI: \n")
    l=input("Ingrese PLANTA: \n")
    m=input("Ingrese RANKING: \n")
    n=input("Puede tomar servicio: \n")
    conn.execute("INSERT INTO tablaid(PROVEEDOR,IDPROVEEDOR,CONDUCTOR,IDCONDUCTOR,UNIDAD,DOMINIO,IDDOMINIO,PESO,TELEFONO,DNI,PLANTA,RANKING,DISPONIBLE) values (?,?,?,?,?,?,?,?,?,?,?,?,?)", (a,b,c,d,f,g,h,i,j,k,l,m,n))
    conn.commit()
    conn.close()
def horario_sarandi():
    canp = 0
    can = int(input("Cantidad de citados en SARANDI: "))
    cannoci = (distos - can)
    plan = (input(f"Hay {cannoci} transportista sin citar en SARANDI.Desea citarlo para otras plantas(LA PLATA,SOLDATI, OTTO)? "))
    if plan =='LA PLATA'or plan =='SOLDATI' or plan =='OTTO':
        canp = int(input(f"Cuantas camionetas desea citar para {plan}? "))
        horp = (input(f"En que horario desea citarlos para {plan}? "))
    else:
        canp = 0
    conn = sqlite3.connect('choferes.db')
    cannoci = (distos - can - canp)
    cur = conn.cursor()
    i = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND PESO='MOTOVEHICULO'  AND DISPONIBLE='SI'")
    motod = len(i.fetchall())
    print(f"La cantidad de MOTOVEHICULOS disponibles son: {motod}")
    moto = int(input("Cantidad de MOTOVEHICULOS citados en SARANDI: "))
    i = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND PESO='UNIDAD GRANDE'  AND DISPONIBLE='SI'")
    volud = len(i.fetchall())
    print(f"La cantidad de UNIDADES GRANDES disponibles son: {volud}")
    volu = int(input("Cantidad de UNIDADES GRANDES citados en SARANDI: "))
    conn.execute(f"""CREATE TABLE IF NOT EXISTS tabladeldia{aa}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Fecha TEXT,
            Chofer TEXT,
            Horario TEXT,
            Planta TEXT,
            Mensaje TEXT,
            Citacion TEXT,
            Confirmacion TEXT,
            Planta TEXT,
            Domino TEXT,
            Ranking TEXT,
            Peso TEXT,)
            """)
    i = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND RANKING ='I' AND DISPONIBLE='SI'")   
    sietey = 0
    ocho = 0
    ochoy = 0
    nueve = 0
    nuevey = 0
    diez = 0
    cansietey = 38
    canocho = 38
    canochoy = 38
    cannueve = 38
    cannuevey = 38
    candiez = 38
    cmoto = 0
    cvolu = 0
    cc = 0
    op = 0
    ir = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND RANKING ='I' AND DISPONIBLE='SI' ")
    print(f"La cantidad en el I son {len(ir.fetchall())}")
    irp = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.P8'")
    irp=len(irp.fetchall())
    ochoy = ochoy + irp
    irpii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kgI'")
    irpii=len(irpii.fetchall())
    irpi = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.I'")
    irpi=len(irpi.fetchall())
    sietey = sietey + irpii + irpi
    irpi = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.P93'")
    irpi=len(irpi.fetchall())
    nuevey = irpi + nuevey
    irpi = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.P9'")
    irpi=len(irpi.fetchall())
    nueve = nueve + irpi
    i = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND RANKING ='I' AND DISPONIBLE='SI'")
    for b in i.fetchall():
        t = b[0]
        y = b[1]
        d = b[2]
        ran = b[3]
        c="2"
        if y =="800kg" or y =="MOTOVEHICULO":
            r = "Distribucion"
            if y == "MOTOVEHICULO" and cmoto < moto :
                n = random.randint(0,2)
                if n == 0 :
                    c ="9:00"
                    cmoto = cmoto + 1
                elif n == 1 :
                    c ="9:00"
                    cmoto = cmoto + 1
                else:
                    c = "NO CITADO"
            elif y == "MOTOVEHICULO":
                c = "NO CITADO"
        elif y == "800kg.P8":
            r = "Distribucion Pick It"
            c = "8:30"
            cc = cc+ 1
        elif y == "800kg.P9":
            r = "Distribucion Pick It"
            c = "9:00"
            cc = cc+ 1
        elif y == "800kg.P93":
            r = "Distribucion Pick It"
            c = "9:30"
            cc = cc+ 1
        elif y == "800kg.I":
            r = "Distribucion IBUE"
            c = "7:30"
            cc = cc+ 1
        elif y == "800kgI":
            r = "Distribucion"
            c = "7:30"
            cc = cc+ 1
        elif y == "UNIDAD GRANDE" and cvolu < volu:
                n = random.randint(0,2)
                if n == 0 :
                    c ="9:00"
                    cvolu = cvolu + 1
                    r = "VOLUMETRIA"
                elif n == 1 :
                    c ="9:00"
                    cvolu = cvolu + 1
                    r = "VOLUMETRIA"
                else:
                    c = "NO CITADO"
                    r = "VOLUMETRIA"
        if ran == "I" and c=="2":
            while True:
                n = random.randint(0,1)
                if n == 0 and sietey < cansietey:
                    sietey = sietey + 1
                    c = "7:30"
                    cc = cc+ 1
                    break
                elif n == 1 and ocho < canocho:
                    ocho = ocho + 1
                    c = "8:00"
                    cc = cc+ 1
                    break
                elif ocho == canocho and sietey == cansietey:
                    while True:
                        n = random.randint(0,1)
                        if n == 0 and ochoy < canochoy:
                            ochoy = ochoy + 1
                            c = "8:30"
                            cc = cc+ 1
                            break
                        elif n == 1 and nueve < cannueve:
                            nueve = nueve + 1
                            c = "9:00"
                            cc = cc+ 1
                            break
                        elif ochoy == canochoy and nueve == cannueve:
                            while True:
                                n = random.randint(0,1)
                                if n == 0 and nuevey < cannuevey:
                                    nuevey = nuevey + 1
                                    c = "9:30"
                                    cc = cc+ 1
                                    break
                                elif n == 1 and diez < candiez:
                                    diez = diez + 1
                                    c = "10:00"
                                    cc = cc+ 1
                                    break
        f = "SI"
        g = "SI"
        if c == "NO CITADO":
            f = "NO"
            g = "NO"
            e = (f"{t}, en relación al servicio de transporte que usted le presta a OCASA, el dia {a} no contaremos con carga para asignarle. En caso de que, hipotéticamente, esta situación se revierta, nos podremos en contacto con usted a primera hora del dia para coordinar, de ser posible, la prestación del servicio. Saludos.")
        else:
            e = (f"Contestar SI o NO. {t} el dia {a} esta citado para {r} en la planta {d} a las {c}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        conn.execute(f"INSERT INTO tabladeldia{aa}(Fecha,Chofer,Horario,Planta,Mensaje,Citacion,Confirmacion) values (?,?,?,?,?,?,?)", (a,t,c,d,e,f,g))   
    ir = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND RANKING ='II' AND DISPONIBLE='SI' ")
    print(f"La cantidad en el II son {len(ir.fetchall())}")
    ii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND RANKING ='II' AND DISPONIBLE='SI'")
    for b in ii.fetchall():
        t = b[0]
        y = b[1]
        d = b[2]
        ran = b[3]
        c="2"
        if y =="800kg" or y =="MOTOVEHICULO":
            r = "Distribucion"
            if y == "MOTOVEHICULO" and cmoto < moto :
                n = random.randint(0,2)
                if n == 0 :
                    c ="9:00"
                    cmoto = cmoto + 1
                elif n == 1 :
                    c ="9:00"
                    cmoto = cmoto + 1
                else:
                    c = "NO CITADO"
            elif y == "MOTOVEHICULO":
                c = "NO CITADO"
        elif y == "800kg.P8":
            r = "Distribucion Pick It"
            c = "8:30"
            cc = cc+ 1
        elif y == "800kg.P9":
            r = "Distribucion Pick It"
            c = "9:00"
            cc = cc+ 1
        elif y == "800kg.P93":
            r = "Distribucion Pick It"
            c = "9:30"
            cc = cc+ 1
        elif y == "800kg.I":
            r = "Distribucion IBUE"
            c = "7:30"
            cc = cc+ 1
        elif y == "800kgI":
            r = "Distribucion"
            c = "7:30"
            cc = cc+ 1
        elif y == "UNIDAD GRANDE" and cvolu < volu:
                n = random.randint(0,2)
                if n == 0 :
                    c ="9:00"
                    cvolu = cvolu + 1
                    r = "VOLUMETRIA"
                elif n == 1 :
                    c ="9:00"
                    cvolu = cvolu + 1
                    r = "VOLUMETRIA"
                else:
                    c = "NO CITADO"
                    r = "VOLUMETRIA"
        if ran == "II" and c=="2":
            tt = True
            while tt:
                n = random.randint(0,1)
                if n == 0 and sietey < cansietey and cc < can :
                    sietey = sietey + 1
                    c = "7:30"
                    cc = cc+ 1
                    tt = False
                    break
                elif n == 1 and ocho < canocho and cc < can:
                    ocho = ocho + 1
                    c = "8:00"
                    cc = cc+ 1
                    tt = False
                    break
                elif ocho == canocho and sietey == cansietey and cc < can:
                    while tt:
                        n = random.randint(0,1)
                        if n == 0 and ochoy < canochoy and cc < can:
                            ochoy = ochoy + 1
                            c = "8:30"
                            cc = cc+ 1
                            tt = False
                            cc= cc+1
                            break
                        elif n == 1 and nueve < cannueve and cc < can:
                            nueve = nueve + 1
                            c = "9:00"
                            cc = cc+ 1
                            tt = False
                            break
                        elif ochoy == canochoy and nueve == cannueve and cc < can:
                            while tt:
                                n = random.randint(0,2)
                                if n == 0 and nuevey < cannuevey and cc < can:
                                    nuevey = nuevey + 1
                                    c = "9:30"
                                    cc = cc+ 1
                                    tt = False
                                    break
                                elif n == 1 and diez < candiez and cc < can:
                                    diez = diez + 1
                                    c = "10:00"
                                    cc = cc+ 1
                                    tt = False
                                    break
                                elif n == 2 and op < canp:
                                    op = op + 1
                                    c = horp
                                    d = plan
                                    tt = False
                                    break
                                elif nuevey == cannuevey and diez == candiez and op == canp :
                                    c = "NO CITADO"
                                    tt = False
                        elif ochoy == canochoy and nueve == cannueve and op < canp :
                           op = op + 1
                           c = horp
                           d = plan
                           tt = False
                           break
                        else:
                            c = "NO CITADO"
                            tt = False
                elif ocho == canocho and sietey == cansietey and op < canp :
                    op = op + 1
                    c = horp
                    d = plan
                    tt = False
                    break
                else:
                    c = "NO CITADO"
                    tt = False
        f = "SI"
        g = "SI"
        if c == "NO CITADO":
            f = "NO"
            g = "NO"
            e = (f"{t}, en relación al servicio de transporte que usted le presta a OCASA, el dia {a} no contaremos con carga para asignarle. En caso de que, hipotéticamente, esta situación se revierta, nos podremos en contacto con usted a primera hora del dia para coordinar, de ser posible, la prestación del servicio. Saludos.")
        else:
            e = (f"Contestar SI o NO. {t} el dia {a} esta citado para {r} en la planta {d} a las {c}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        conn.execute(f"INSERT INTO tabladeldia{aa}(Fecha,Chofer,Horario,Planta,Mensaje,Citacion,Confirmacion) values (?,?,?,?,?,?,?)", (a,t,c,d,e,f,g))
    ir = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND RANKING ='III' AND DISPONIBLE='SI' ")
    print(f"La cantidad en el II son {len(ir.fetchall())}")
    iii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND RANKING ='III' AND DISPONIBLE='SI'")
    for b in iii.fetchall():
        t = b[0]
        y = b[1]
        d = b[2]
        ran = b[3]
        c="2"
        if y =="800kg" or y =="MOTOVEHICULO":
            r = "Distribucion"
            if y == "MOTOVEHICULO" and cmoto < moto :
                n = random.randint(0,2)
                if n == 0 :
                    c ="9:00"
                    cmoto = cmoto + 1
                elif n == 1 :
                    c ="9:00"
                    cmoto = cmoto + 1
                else:
                    c = "NO CITADO"
            elif y == "MOTOVEHICULO":
                c = "NO CITADO"
        elif y == "800kg.P8":
            r = "Distribucion Pick It"
            c = "8:30"
            cc = cc+ 1
        elif y == "800kg.P9":
            r = "Distribucion Pick It"
            c = "9:00"
            cc = cc+ 1
        elif y == "800kg.P93":
            r = "Distribucion Pick It"
            c = "9:30"
            cc = cc+ 1
        elif y == "800kg.I":
            r = "Distribucion IBUE"
            c = "7:30"
            cc = cc+ 1
        elif y == "800kgI":
            r = "Distribucion"
            c = "7:30"
            cc = cc+ 1
        elif y == "UNIDAD GRANDE" and cvolu < volu:
                n = random.randint(0,2)
                if n == 0 :
                    c ="9:00"
                    cvolu = cvolu + 1
                    r = "VOLUMETRIA"
                elif n == 1 :
                    c ="9:00"
                    cvolu = cvolu + 1
                    r = "VOLUMETRIA"
                else:
                    c = "NO CITADO"
                    r = "VOLUMETRIA"
        if ran == "III" and c=="2":
            tt = True
            while tt:
                n = random.randint(0,1)
                if n == 0 and sietey < cansietey and cc < can:
                    sietey = sietey + 1
                    c = "7:30"
                    cc = cc+ 1
                    tt = False
                    break
                elif n == 1 and ocho < canocho and cc < can:
                    ocho = ocho + 1
                    c = "8:00"
                    cc = cc+ 1
                    tt = False
                    break
                elif ocho == canocho and sietey == cansietey and cc < can:
                    while tt:
                        n = random.randint(0,1)
                        if n == 0 and ochoy < canochoy and cc < can:
                            ochoy = ochoy + 1
                            c = "8:30"
                            cc = cc+ 1
                            tt = False
                            break
                        elif n == 1 and nueve < cannueve and cc < can:
                            nueve = nueve + 1
                            c = "9:00"
                            cc = cc+ 1
                            tt = False
                            break
                        elif ochoy == canochoy and nueve == cannueve and cc < can:
                            while tt:
                                n = random.randint(0,2)
                                if n == 0 and nuevey < cannuevey and cc < can:
                                    nuevey = nuevey + 1
                                    c = "9:30"
                                    cc = cc+ 1
                                    tt = False
                                    break
                                elif n == 1 and diez < candiez and cc < can:
                                    diez = diez + 1
                                    c = "10:00"
                                    cc = cc+ 1
                                    tt = False
                                    break
                                elif n == 2 and op < canp:
                                    op = op + 1
                                    c = horp
                                    d = plan
                                    tt = False
                                    break
                                elif nuevey == cannuevey and diez == candiez and op == canp :
                                    c = "NO CITADO"
                                    tt = False
                        elif ochoy == canochoy and nueve == cannueve and op < canp :
                           op = op + 1
                           c = horp
                           d = plan
                           tt = False
                           break
                        else:
                            c = "NO CITADO"
                            tt = False
                elif ocho == canocho and sietey == cansietey and op < canp :
                    op = op + 1
                    c = horp
                    d = plan
                    tt = False
                    break
                else:
                    c = "NO CITADO"
                    tt = False
        f = "SI"
        g = "SI"
        if c == "NO CITADO":
            f = "NO"
            g = "NO"
            e = (f"{t}, en relación al servicio de transporte que usted le presta a OCASA, el dia {a} no contaremos con carga para asignarle. En caso de que, hipotéticamente, esta situación se revierta, nos podremos en contacto con usted a primera hora del dia para coordinar, de ser posible, la prestación del servicio. Saludos.")
        else:
            e = (f"Contestar SI o NO. {t} el dia {a} esta citado para {r} en la planta {d} a las {c}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        conn.execute(f"INSERT INTO tabladeldia{aa}(Fecha,Chofer,Horario,Planta,Mensaje,Citacion,Confirmacion) values (?,?,?,?,?,?,?)", (a,t,c,d,e,f,g))
    conn.commit()
    conn.close()
def horario_laplata():
    canp = 0
    can = int(input("Cantidad de citados en LA PLATA: "))
    cannoci = (disto - can)
    plan = (input(f"Hay {cannoci} transportista sin citar en LA PLATA.Desea citarlo para otras plantas(SARANDI,SOLDATI, OTTO)? "))
    if plan == 'SARANDI'or plan =='SOLDATI' or plan =='OTTO':
        canp = int(input(f"Cuantas camionetas desea citar para {plan}? "))
        horp = (input(f"En que horario desea citarlos para {plan}? "))
    conn = sqlite3.connect('choferes.db')
    cannoci = (disto - can - canp)
    cur = conn.cursor()
    conn.execute(f"""CREATE TABLE IF NOT EXISTS tabladeldia{aa}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Fecha TEXT,
            Chofer TEXT,
            Horario TEXT,
            Planta TEXT,
            Mensaje TEXT,
            Citacion TEXT,
            Confirmacion TEXT,
            Plantac TEXT,
            Dominio TEXT,
            Ranking TEXT,
            Peso TEXT)
            """)
    canocho = round(((can*40)/100))
    cannueve = round(((can*55)/100))
    ocho = 0
    nueve = 0
    noci  = 0
    canpp = 0
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    ir = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND RANKING ='I' AND DISPONIBLE='SI' ")
    print(f"La cantidad en el I son {len(ir.fetchall())}")
    irp = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND DISPONIBLE='SI' AND PESO='800kg.P'")
    irp=len(irp.fetchall())
    ocho = ocho + irp
    i = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING, DOMINIO FROM tablaid WHERE PLANTA ='LA PLATA' AND RANKING ='I' AND DISPONIBLE='SI'")
    for b in i.fetchall():
        t = b[0]
        y = b[1]
        d = b[2]
        ran = b[3]
        do = b[4]
        c="2"
        if y =="800kg" or y =="MOTOVEHICULO":
            r = "Distribucion"
        elif y == "800kg.P":
            r = "Distribucion Pick It"
            c = "8:00"
            plan = "A049"
        elif y == "800kgP":
            r = "Distribucion"
            c = "8:00"
            plan = "A049"
        elif y == "800kg.C":
            r = "Distribucion Clearing"
            c="7:00"
            plan = "A049"
        elif y == "800kg.P10":
            r = "Distribucion Pick It"
            c = "9:30"
            plan = "A049"
        elif y == "UNIDAD GRANDE":
            r = "Volumetria"
            c = "10:00"
            plan = "A049"
        if ran == "I" and c=="2":
            while True:
                n = random.randint(0,2)
                if n == 0 and ocho < canocho:
                    ocho = ocho + 1
                    c = "8:00"
                    plan = "A049"
                    break
                elif n == 1 and nueve < cannueve:
                    nueve = nueve + 1
                    c = "9:30"
                    plan = "A049"
                    break
        f = "SI"
        g = "SI"
        e = (f"Contestar SI o NO. {t} el dia {a} esta citado para {r} en la planta {d} a las {c}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        conn.execute(f"INSERT INTO tabladeldia{aa}(Fecha,Chofer,Horario,Planta,Mensaje,Citacion,Confirmacion,Plantac,Dominio,Ranking,Peso) values (?,?,?,?,?,?,?,?,?,?,?)", (a,t,c,d,e,f,g,plan,do,ran,y))
    ii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND RANKING ='II' AND DISPONIBLE='SI' ")
    print(f"La cantidad en el II son {len(ii.fetchall())}")
    ii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING, DOMINIO FROM tablaid WHERE PLANTA ='LA PLATA' AND RANKING ='II' AND DISPONIBLE='SI'")
    for b in i.fetchall():
        t = b[0]
        y = b[1]
        d = b[2]
        ran = b[3]
        do = b[4]
        c="2"
        if y =="800kg" or y =="MOTOVEHICULO":
            r = "Distribucion"
        elif y == "800kg.P":
            r = "Distribucion Pick It"
            c = "8:00"
            plan = "A049"
        elif y == "800kg.C":
            r = "Distribucion Clearing"
            c="7:00"
            plan = "A049"
        elif y == "800kg.P10":
            r = "Distribucion Pick It"
            c = "9:30"
            plan = "A049"
        elif y == "UNIDAD GRANDE":
            r = "Volumetria"
            c = "10:00"
            plan = "A049"
        if ran == "II" and c=="2":
            while True:
                n = random.randint(0,3)
                if n == 0 and ocho < canocho:
                    ocho = ocho + 1
                    c = "8:00"
                    plan = "A049"
                    break
                elif n == 1 and nueve < cannueve:
                    nueve = nueve + 1
                    c = "9:30"
                    plan = "A049"
                    break
                elif n == 2 and noci < cannoci:
                    noci = noci + 1
                    c = "NO CITADO"
                    plan = "NO"
                    break
                elif n == 3 and canpp < canp:
                    canpp = canpp + 1
                    d = plan
                    c = horp
                    plan = "A049"
                    break
        f = "SI"
        g = "SI"
        if c == "NO CITADO":
            f = "NO"
            g = "NO"
            e = (f"{t}, en relación al servicio de transporte que usted le presta a OCASA, el dia {a} no contaremos con carga para asignarle. En caso de que, hipotéticamente, esta situación se revierta, nos podremos en contacto con usted a primera hora del dia para coordinar, de ser posible, la prestación del servicio. Saludos.")
        else:
            e = (f"Contestar SI o NO. {t} el dia {a} esta citado para {r} en la planta {d} a las {c}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        conn.execute(f"INSERT INTO tabladeldia{aa}(Fecha,Chofer,Horario,Planta,Mensaje,Citacion,Confirmacion,Plantac,Dominio,Ranking,Peso) values (?,?,?,?,?,?,?,?,?,?,?)", (a,t,c,d,e,f,g,plan,do,ran,y))
    iii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND RANKING ='III' AND DISPONIBLE='SI'")
    print(f"La cantidad en el III son {len(iii.fetchall())}")
    iii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING, DOMINIO FROM tablaid WHERE PLANTA ='LA PLATA' AND RANKING ='III' AND DISPONIBLE='SI'")
    for b in i.fetchall():
        t = b[0]
        y = b[1]
        d = b[2]
        ran = b[3]
        do = b[4]
        c="2"
        if y =="800kg" or y =="MOTOVEHICULO":
            r = "Distribucion"
        elif y == "800kg.P":
            r = "Distribucion Pick It"
            c = "8:00"
            plan = "A049"
        elif y == "800kg.C":
            r = "Distribucion Clearing"
            c="7:00"
            plan = "A049"
        elif y == "800kg.P10":
            r = "Distribucion Pick It"
            c = "9:30"
            plan = "A049"
        elif y == "UNIDAD GRANDE":
            r = "Volumetria"
            c = "10:00"
            plan = "A049"
        if ran == "III" and c=="2":
            while True:
                n = random.randint(0,3)
                if n == 0 and ocho < canocho:
                    ocho = ocho + 1
                    c = "8:00"
                    plan = "A049"
                    break
                elif n == 1 and nueve < cannueve:
                    nueve = nueve + 1
                    c = "9:30"
                    plan = "A049"
                    break
                elif n == 2 and noci < cannoci:
                    noci = noci + 1
                    c = "NO CITADO"
                    plan = "NO"
                    break
                elif n == 3 and canpp < canp:
                    canpp = canpp + 1
                    d = plan
                    c = horp
                    plan = "A049"
                    break
        f = "SI"
        g = "SI"
        if c == "NO CITADO":
            f = "SI"
            g = "NO"
            e = (f"{t}, en relación al servicio de transporte que usted le presta a OCASA, el dia {a} no contaremos con carga para asignarle. En caso de que, hipotéticamente, esta situación se revierta, nos podremos en contacto con usted a primera hora del dia para coordinar, de ser posible, la prestación del servicio. Saludos.")
        else:
            e = (f"Contestar SI o NO. {t} el dia {a} esta citado para {r} en la planta {d} a las {c}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        conn.execute(f"INSERT INTO tabladeldia{aa}(Fecha,Chofer,Horario,Planta,Mensaje,Citacion,Confirmacion,Plantac,Dominio,Ranking,Peso) values (?,?,?,?,?,?,?,?,?,?,?)", (a,t,c,d,e,f,g,plan,do,ran,y))
    conn.commit()
    conn.close()
    return a , aa
def modificar():
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    que = input("Que desea modificar?")
    mod = input("¿Que chofer desea modificar, escriba el ID completo?")
    i = cur.execute(f"SELECT CONDUCTOR FROM tablaid WHERE IDCONDUCTOR = '{mod}' ")
    i = i.fetchone()
    i = functools.reduce(operator.add, (i))
    print(f"Va a modificar {que} de {i}")
    if que == "PLANTA":
        dis = input(f"¿Escriba la nueva {que} de {mod}?")
    elif que == "DISPONIBLE":
        dis = input(f"¿Esta {que} {mod}?")
    else:
        dis = input(f"¿Escriba el nuevo {que} de {i}?")
    cur.execute(f"UPDATE  tablaid SET '{que}' = '{dis}' WHERE IDCONDUCTOR = '{mod}'")
    conn.commit()
    conn.close()
def data_entry():
    conn = sqlite3.connect('choferes.db')
    cursor2=conn.execute("SELECT CONDUCTOR, PESO, PLANTA FROM tablaid")
    for b in cursor2.fetchall():
        t = b[0]
        y = b[1]
        d = b[2]
        if y =="800kg" or y =="MOTOVEHICULO":
            r = "Distribucion"
        elif y == "800kg.P":
            r = "Distribucion Pick It"
        elif y == "800kg.C":
            r = "Distribucion Clearing"
        elif y == "UNIDAD GRANDE":
            r = "Volumetria"
        #c= input('Ingrese Horario')
        c = "8:30"
        horario_laplata()
        e = (f"Contestar SI o NO. {t} el dia {a} esta citado para {r} en la planta {d} a las {c}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        print(e)
        conn.execute(f"INSERT INTO tabladeldia{aa}(Fecha,Chofer,Horario,Planta,Mensaje) values (?,?,?,?,?)", (a,t,c,d,e))
        continue
    conn.commit()
    conn.close()
def eliminar():
    while True:
        conn = sqlite3.connect('choferes.db')
        cur = conn.cursor()
        eli = input("¿Que chofer desea eliminar, escriba el ID del Chofer?")
        i = cur.execute(f"SELECT CONDUCTOR FROM tablaid WHERE IDCONDUCTOR = '{eli}' ")
        i2 = i.fetchone()
        i3 = functools.reduce(operator.add, (i2))
        k =input(f"Desea eliminar a {i3}?")
        if k =="SI":    
            cur.execute(f"DELETE FROM tablaid WHERE IDCONDUCTOR = '{eli}'")
            conn.commit()
            conn.close()
            return False       
def disponibles_laplata():
    global disto
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    i = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND DISPONIBLE='SI' AND PESO='800kg'")
    i1 = len(i.fetchall())
    ii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND DISPONIBLE='SI' AND PESO='800kg.P'")  
    i2 = len(ii.fetchall())
    iii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND DISPONIBLE='SI' AND PESO='800kg.P10'")  
    i3 = len(iii.fetchall())
    iiii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='LA PLATA' AND DISPONIBLE='SI' AND PESO='800kg.C'")  
    i4 = len(iiii.fetchall())
    disto = i1 + i2 + i3 + i4
    print(f"La cantidad de TTAS de 800KG disponibles son: {disto}")
    conn.commit()
    conn.close()
def disponibles_sarandi():
    global distos
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    i = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg'")
    i1 = len(i.fetchall())
    ii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.I'")  
    i2 = len(ii.fetchall())
    iii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.P8'")  
    i3 = len(iii.fetchall())
    iiii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.P9'")  
    i4 = len(iiii.fetchall())
    iiiii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kg.P93'")  
    i5 = len(iiiii.fetchall())
    iiiiii = cur.execute("SELECT CONDUCTOR, PESO, PLANTA, RANKING FROM tablaid WHERE PLANTA ='SARANDI' AND DISPONIBLE='SI' AND PESO='800kgI'")  
    i6 = len(iiiiii.fetchall())
    distos = i1 + i2 + i3 + i4 + i5 + i6
    print(f"La cantidad de TTAS de 800KG disponibles son: {distos}")
    conn.commit()
    conn.close()
def modificar_fecha():
    #now = datetime.now()
    #hoy = now.strftime('%d-%m-%y')
    v = input("Ingrese la fecha de citacion: ")
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    cur.execute(f"""
    UPDATE  tablaid 
    SET DISPONIBLE = 'SI' 
    WHERE DISPONIBLE < '{v}'
    """)
    conn.commit()
    conn.close()

def run():
    global a , aa
    tablaid()
    while True:
        nuevo = input("¿Que desea realiizar(Agregar ttas, Modificar, Eliminar, Actualizar o Citar)?")
        if nuevo == "Agregar":
            nuevos()
        elif nuevo =="Eliminar":
            eliminar()
        elif nuevo =="Modificar":
            modificar()
        elif nuevo == "Actualizar":
            modificar_fecha()
        elif nuevo == "Citar":
            a = input("Ingrese Fecha de citacion:")
            aa = a.split('-')
            aa="".join(aa)
            while True:
                donde=input("Para que planta desea citar(SARANDI, LA PLATA)?")
                if donde == "SARANDI":
                    disponibles_sarandi()
                    horario_sarandi()
                elif donde == "LA PLATA":
                    disponibles_laplata()
                    horario_laplata()
                else:
                    break
        elif nuevo == "Salir":
            return False
run()

