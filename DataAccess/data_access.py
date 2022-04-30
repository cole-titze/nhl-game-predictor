import pyodbc
import sys
from Entities.Mappers import pregame_mapper
from dataclasses import field

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
            cursor.execute("SELECT * FROM CleanedGame")
            row = cursor.fetchone()
            while row:
                pregameList.append(row)
                row = cursor.fetchone()
    return pregame_mapper.map_db_pregames_to_entities(pregameList)

def get_train_test_data(game_list, test_year):
    x_test = []
    y_test = []
    x_train = []
    y_train = []
    test = []
    train = []

    for game in game_list:
        if game.seasonStartYear == test_year:
            test.append(game)
        elif game.isExcluded == False:
            train.append(game)
    
    for game in test:
        y_test.append(game.winner)
        x_test.append(game.map_data())
    for game in train:
        y_train.append(game.winner)
        x_train.append(game.map_data())

    
    
    return x_train, y_train, x_test, y_test