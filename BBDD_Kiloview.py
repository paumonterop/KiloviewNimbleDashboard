import sqlite3
import time
import API_functions
from sqlite3 import Error


def sql_connection():
    try:
        bd_kv = sqlite3.connect('bd_kv.db')
        return bd_kv
    except Error:

        print(Error)


# Create table
def sql_table(con):
    cur = bd_kv.cursor()
    cur.execute("CREATE TABLE Kiloviews(id integer PRIMARY KEY, ob text, name text, bitrate int, port int)")
    bd_kv.commit()


bd_kv = sql_connection()
#sql_table(bd_kv)


def sql_insert(con, entities):
    cur = bd_kv.cursor()
    cur.execute('INSERT OR REPLACE INTO Kiloviews(id, ob, name, bitrate, port) VALUES(?, ?, ?, ?, ?)', entities)

    bd_kv.commit()


while True:
    # ================================
    # NAS
    # ================================
    nas_bd = []
    last_ip_digit = 31
    for i in range(10):
        ip = ('10.17.146.{}'.format(last_ip_digit))
        port = API_functions.getPort(ip)
        bitrate = API_functions.getBitrate(ip)
        last_ip_digit = last_ip_digit + 1
        nas = (i, 'NAS', 'NAS{}'.format(i + 1), bitrate, port)
        nas_bd.append(nas)

    for nas_bd in nas_bd:
        sql_insert(bd_kv, nas_bd)

    # ================================
    # OB23
    # ================================
    ob23_bd = []
    last_ip_digit = 11
    for i in range(8):
        ip = ('10.28.66.{}'.format(last_ip_digit))
        port = API_functions.getPort(ip)
        bitrate = API_functions.getBitrate(ip)
        last_ip_digit = last_ip_digit + 1
        ob23 = (10 + i, 'OB23', 'OB23-{}'.format(i + 1), bitrate, port)
        ob23_bd.append(ob23)

    for ob23_bd in ob23_bd:
        sql_insert(bd_kv, ob23_bd)

    # ================================
    # OB39
    # ================================
    ob39_bd = []
    last_ip_digit = 11
    for i in range(8):
        ip = ('10.28.64.{}'.format(last_ip_digit))
        port = API_functions.getPort(ip)
        bitrate = API_functions.getBitrate(ip)
        last_ip_digit = last_ip_digit + 1
        ob39 = (18 + i, 'OB39', 'OB39-{}'.format(i + 1), bitrate, port)
        ob39_bd.append(ob39)

    for ob39_bd in ob39_bd:
        sql_insert(bd_kv, ob39_bd)

    # ================================
    # OB40
    # ================================
    ob40_bd = []
    last_ip_digit = 11
    for i in range(8):
        ip = ('10.28.67.{}'.format(last_ip_digit))
        port = API_functions.getPort(ip)
        bitrate = API_functions.getBitrate(ip)
        last_ip_digit = last_ip_digit + 1
        ob40 = (26 + i, 'OB40', 'OB40-{}'.format(i + 1), bitrate, port)
        ob40_bd.append(ob40)

    for ob40_bd in ob40_bd:
        sql_insert(bd_kv, ob40_bd)

    # ================================
    # OB53
    # ================================
    ob53_bd = []
    last_ip_digit = 11
    for i in range(8):
        ip = ('10.28.63.{}'.format(last_ip_digit))
        port = API_functions.getPort(ip)
        bitrate = API_functions.getBitrate(ip)
        last_ip_digit = last_ip_digit + 1
        ob53 = (34 + i, 'OB53', 'OB53-{}'.format(i + 1), bitrate, port)
        ob53_bd.append(ob53)

    for ob53_bd in ob53_bd:
        sql_insert(bd_kv, ob53_bd)

    # ================================
    # OB86
    # ================================
    ob86_bd = []
    last_ip_digit = 11
    for i in range(8):
        ip = ('10.28.68.{}'.format(last_ip_digit))
        port = API_functions.getPort(ip)
        bitrate = API_functions.getBitrate(ip)
        last_ip_digit = last_ip_digit + 1
        ob86 = (42 + i, 'OB86', 'OB86-{}'.format(i + 1), bitrate, port)
        ob86_bd.append(ob86)

    for ob86_bd in ob86_bd:
        sql_insert(bd_kv, ob86_bd)

    # ================================
    # OB89
    # ================================
    ob89_bd = []
    last_ip_digit = 11
    for i in range(8):
        ip = ('10.28.42.{}'.format(last_ip_digit))
        port = API_functions.getPort(ip)
        bitrate = API_functions.getBitrate(ip)
        last_ip_digit = last_ip_digit + 1
        ob89 = (50 + i, 'OB89', 'OB89-{}'.format(i + 1), bitrate, port)
        ob89_bd.append(ob89)

    for ob89_bd in ob89_bd:
        sql_insert(bd_kv, ob89_bd)

    time.sleep(60)  # Delay for 1 minute (60 seconds).
