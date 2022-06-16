import sqlite3
import time
import API_functions
from sqlite3 import Error


def sql_connection():
    try:
        bd_mtx_srt = sqlite3.connect('bd_mtx_srt.db')
        return bd_mtx_srt
    except Error:

        print(Error)

bd_mtx_srt = sql_connection()