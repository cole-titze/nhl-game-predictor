import pyodbc

server = 'nhl-game.database.windows.net'
database = 'Games'
username = 'console'
password = '{duvton-qofDic-1runxi}'
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 id FROM Game")
        row = cursor.fetchone()
        while row:
            print(str(row[0]))
            row = cursor.fetchone()
