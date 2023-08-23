import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


def conn_db( query, columns ):
    with sqlite3.connect("C:/Program Files/DB Browser for SQLite/databases/Northwind.db") as conn:
        
        cursor = conn.cursor()
        cursor.execute( query )
        results = cursor.fetchall()
        df = pd.DataFrame( results, columns=columns )
    
    return df

