from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
import re
from unicodedata import normalize
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
import datetime
import csv, operator
from Choferes import *
import functools
import operator
from os import remove
from os import path

global w
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=\driver\data")
driver = webdriver.Chrome(executable_path=r"C:\Users\romer\OneDrive\Escritorio\Programacion\chromedriver_win32\chromedriver.exe", options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(20)
respuesta =[]
conn = sqlite3.connect('choferes.db')
cur = conn.cursor()
irpp = cur.execute(f"SELECT Chofer FROM tabladeldia{aa} ")
for w in range(len(irpp.fetchall())+1):
    irp = cur.execute(f"SELECT CHOFER FROM tabladeldia{aa} WHERE ID='{w}'")
    contactos2 = irp.fetchone()
    irr = cur.execute(f"SELECT Mensaje FROM tabladeldia{aa} WHERE ID='{w}'")
    mensa1 = irr.fetchone()
    if w != 0:
        contacto = functools.reduce(operator.add, (contactos2))
        mensaj = functools.reduce(operator.add, (mensa1))
        with open("./resource/contacto.txt", mode='a+', encoding='utf-8') as f:
            f.write(contacto + "\n")
        with open("./resource/mensaje.txt", mode='a+', encoding='utf-8') as ff:
            ff.write(mensaj + "\n")

with open("./resource/contacto.txt", mode='r', encoding='utf-8') as archivo:
    with open("./resource/mensaje.txt", mode='r', encoding='utf-8') as ar:
        contactos = [linea.rstrip() for linea in archivo]
        mensa = [linea.rstrip() for linea in ar]

def envio_de_mensajes ():
    element = driver.find_element_by_xpath('//div[@class ="_13NKt copyable-text selectable-text"]')
    for name , m in zip(contactos, mensa):
        element.send_keys(name + Keys.ENTER)
        chatbox2 = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
        re = ( m + "\n")
        chatbox2.send_keys(re)
        contactos.remove(name)
        mensa.remove(m)
        break
def no():
    global iii , mensa1 , ii
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    i = cur.execute(f"SELECT PLANTA FROM tabladeldia{aa} WHERE Chofer ='{name2}'")
    i = i.fetchone()
    i = functools.reduce(operator.add, (i))
    h = cur.execute(f"SELECT HORARIO FROM tabladeldia{aa} WHERE Chofer = '{name2}'")
    h = h.fetchone()
    h = functools.reduce(operator.add, (h))
    ii = cur.execute(f"SELECT ID FROM tabladeldia{aa} WHERE HORARIO = 'NO CITADO' AND PLANTA ='{i}'")
    ii = ii.fetchall()
    if len(ii) == 0 :    
        ii = 0
        cur.execute(f"""UPDATE tabladeldia{aa} 
        SET Horario = 'NO' 
        WHERE CHOFER = '{name2}'""")
    else:
        ii = functools.reduce(operator.add, (ii))
        n = random.choice(ii)
        iii = cur.execute(f"SELECT CHOFER FROM tabladeldia{aa} WHERE ID = '{n}'")
        iii = iii.fetchone()
        iii = functools.reduce(operator.add, (iii))
        pa = cur.execute(f"SELECT PESO FROM tablaid WHERE CONDUCTOR = '{name2}'")
        pa = pa.fetchone()
        pa = functools.reduce(operator.add, (pa))
        if pa == "UNIDAD GRANDE":
            pa = "VOLUMETRIA"
        else:
            pa = "DISTRIBUCION" 
        mensa1 = (f"Contestar SI o NO. {iii} el dia {a} esta citado para {pa} en la planta {i} a las {h}. Confirmar la citacion a este numero y al llegar al planta avisar al : 1160064527 . Muchas Gracias.")
        cur.execute(f"""
        UPDATE tabladeldia{aa} 
        SET Horario = '{h}' 
        WHERE Chofer ='{iii}'""")
        cur.execute(f"""
        UPDATE tabladeldia{aa} 
        SET MENSAJE = '{mensa1}' 
        WHERE Chofer ='{iii}'""")
        cur.execute(f"""UPDATE tabladeldia{aa} 
        SET Horario = 'NO' 
        WHERE CHOFER = '{name2}'""")
        cur.execute(f"""
        UPDATE tabladeldia{aa} 
        SET CONFIRMACION = 'NO' 
        WHERE CHOFER = '{name2}'""")
        cur.execute(f"""
        UPDATE tabladeldia{aa} 
        SET CONFIRMACION = 'SI' 
        WHERE Chofer ='{iii}'""")
        cur.execute(f"""
        UPDATE tabladeldia{aa} 
        SET CITACION = 'SI' 
        WHERE Chofer ='{iii}'""")
        conn.commit()
        conn.close()

def envio_de_negacion ():
    element = driver.find_element_by_xpath('//div[@class ="_13NKt copyable-text selectable-text"]')
    if ii == 0:
        o = "2"
    else:
        name = iii
        element.send_keys(name + Keys.ENTER)
        chatbox2 = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
        m = str(mensa1)
        re = ( m + "\n")
        chatbox2.send_keys(re)

def buscar_chats():
    print("BUSCANDO CHATS")
    if len(driver.find_elements_by_class_name("zaKsw")) == 0:
        print("CHAT ABIERTO")
        message = identificar_mensaje()
        
        if message != None:
            return True

    chats = driver.find_elements_by_class_name("_3m_Xw")
    for chat in chats:
        print("DETECTANDO MENSAJES SIN LEER")

        chats_mensajes = chat.find_elements_by_class_name("_23LrM")

        if len(chats_mensajes) == 0:
            print("CHATS ATENDIDOS")
            continue

        element_name = chat.find_elements_by_class_name('_3q9s6')
        name = element_name[0].text.upper().strip()

        print("IDENTIFICANDO CONTACTO")
        
        #with open("./resource/contactos_autorizados.txt", mode='r', encoding='utf-8') as archivo:
        #   contactos = [linea.rstrip() for linea in archivo]
        #   if name not in contactos:
        #       print("CONTACTO NO AUTORIZADO : ", name)
        #       continue
        #
        #print(name, "AUTORIZADO PARA SER ATENDIDO POR BOT")
        
        chat.click()
        return True
    return False

def normalizar(message: str):
    # -> NFD y eliminar diacríticos
    message = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", message), 0, re.I
    )

    # -> NFC
    return normalize( 'NFC', message)

def identificar_mensaje():
    sleep(1)
    element_box_message = driver.find_elements_by_class_name("Nm1g1")
    posicion = len(element_box_message) - 1

    color = element_box_message[posicion].value_of_css_property(
        "background-color")

    if color == "rgba(220, 248, 198, 1)" or color == "rgba(5, 97, 98, 1)":
        print("CHAT ATENDIDO")
        return
    sleep(1)
    element_message = element_box_message[posicion].find_elements_by_class_name(
        "_1Gy50")
    message = element_message[0].text.upper().strip()
    massage = message
    message = message.split('-')
    message = message[0]
    sleep(2)
    try:
        message = int(message)
    except ValueError:
        message = message
    print("MENSAJE RECIBIDO :", message)
    sleep(2)
    return message, massage

def preparar_respuesta(message, massage):
    global name2
    print("PREPARANDO RESPUESTA")
    conn = sqlite3.connect('choferes.db')
    cur = conn.cursor()
    if message == "NO":
        response = "Si solamente se va ausentar mañana no enviar aclaraciones o fechas, si es mas de un dia indicar solamente la fecha de regreso en el siguiente formato: DIA-MES-AÑO 28-08-21. Gracias. \n"
        driver2 = driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[4]')
        name2 = driver2.find_element_by_xpath(
            '//*[@id="main"]/header/div[2]/div/div/span').text
        respuesta.append(name2 + ";" + message)
        cur.execute(f"UPDATE  tabladeldia{aa} SET CONFIRMACION ='NO'  WHERE Chofer = '{name2}'")
        conn.commit()
        conn.close()
    elif type(message) == int:
        response = (f"Muchas gracias, no sera citado hasta: {massage} \n")
        driver2 = driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[4]')
        name2 = driver2.find_element_by_xpath(
            '//*[@id="main"]/header/div[2]/div/div/span').text
        respuesta.append(name2 + ";" + "NO" + ";" + massage)
        massage = str(massage)
        cur.execute(f"UPDATE  tablaid SET DISPONIBLE ='{massage}'  WHERE CONDUCTOR = '{name2}'")
        conn.commit()
        conn.close()
    elif message == "SI" or message == "SÍ" or message == "Sí" or message == "sí" or message == "si" or message == "OK" or message == "Ok" or message == "ok" :
        response = "Muchas gracias. Que tenga un buen dia. \n"
        driver2 = driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[4]')
        name2 = driver2.find_element_by_xpath(
            '//*[@id="main"]/header/div[2]/div/div/span').text
        respuesta.append(name2 + ";" + message)
        #cur.execute(f"UPDATE  tabladeldia{aa} SET CONFIRMACION ='SI'  WHERE Chofer = '{name2}'")
    elif message == "MENU":
        text1 = open("./resource/respuesta1.txt", mode='r', encoding='utf-8')
        response = text1.readlines()
        text1.close()
    elif message == "INHABILITADO":
        response = "Estimado se encuentra inhabilitado revise sus documentos si alguno se encuentra vencido o se vence mañana. De ser asi suba de nuevo el documento, tiene tiempo hasta las 18hs. \n"
    elif message == "IGUALMENTE" or message == "GRACIAS" or message == "GRACIAS IGUALMENTE" or message == "MUCHAS GRACIAS" or message == "MUCHAS GRACIAS IGUALMENTE" or message == "IGUALMENTE GRACIAS" or message == "GRACIAS!":
        response = " De nada \n"
    elif message == "CONSULTA":
        response = "Aguarde unos minutos ya lo atenderemos. \n"
    else:
        response = "Estimado por favor responder SI o NO a la citacion, si no se encuentra citado no responder nada,si esta en desacuerdo con la citacion, tenga en cuenta que la planta u horario no se modificaran excepto que la operacion lo requiera. Si es por otra consulta mande un mail atenciontransportistas-ar@ocasa.com o envie CONSULTA para ser atendido por este medio. \n"
    return response

def procesar_mensaje(message :str , massage):
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    response = preparar_respuesta(message, massage)
    chatbox.send_keys(response)

def whatsapp_boot_init():
    b = 0
    n = ""
    while True:
        envio_de_mensajes()
        b = 1 + b 
        if b >= 140 and n == "si":
            b = 0
            n = ""
        if b == 140:
            n = input("Desea continuar?")
            if n == "no":
                return False
        if not buscar_chats():
            sleep(2)
            continue
        if identificar_mensaje() != None:
            message, massage= identificar_mensaje()    
        if message == None:
            continue
        procesar_mensaje(message , massage)
        #if message == "NO":
        #    no()
        #    envio_de_negacion()
whatsapp_boot_init()

if path.exists("./resource/contacto.txt"):
    remove('./resource/contacto.txt')

if path.exists("./resource/mensaje.txt"):
    remove('./resource/mensaje.txt')
    
with open("out.csv","w") as f:
    wr = csv.writer(f,delimiter="\n")
    wr.writerow(respuesta)
