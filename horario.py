#import Choferes
#import sqlite3
#from datetime import date
#from datetime import datetime
#import csv
#conn = sqlite3.connect('choferes.db')
#cur = conn.cursor()
#i = cur.execute("SELECT * FROM tablaid WHERE PLANTA ='LPG' AND RANKING ='I'")
##iii = cur.execute("SELECT * FROM tablaid WHERE PLANTA ='LPG' AND RANKING ='III'")
#data = i.fetchall()
#[print(row) for row in data]
#ii = cur.execute("SELECT * FROM tablaid WHERE PLANTA ='LPG' AND RANKING ='II'")
#data2 = ii.fetchall()
##data3 = iii.fetchall()
#[print(row2) for row2 in data2]
##[print(row3) for row3 in data3]
from datetime import date
from datetime import datetime

#Día actual
now = datetime.now()
format = now.strftime('%d-%m-%y')
if "29-07-21"<format:
    print("se puede")
print(format)