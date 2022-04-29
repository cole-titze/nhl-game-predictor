import pyodbc
import sys
from Entities.Mappers import pregame_mapper

server = 'nhl-game.database.windows.net'
database = 'Games'
username = 'console'
password = '{duvton-qofDic-1runxi}'
driver = '{ODBC Driver 17 for SQL Server}'

def get_cleaned_pregames() -> list:
    pregameList = []
    # Grab all entries from sql
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM CleanedGame WHERE isExcluded = 0")
            row = cursor.fetchone()
            while row:
                pregameList.append(row)
                row = cursor.fetchone()
    return pregame_mapper.map_db_pregames_to_entities(pregameList)
