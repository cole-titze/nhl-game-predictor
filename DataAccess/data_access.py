import pyodbc
from Entities.Mappers import pregame_mapper

server = 'nhl-game.database.windows.net'
database = 'Games'
username = 'console'
password = '{duvton-qofDic-1runxi}'
driver = '{ODBC Driver 18 for SQL Server}'

def get_cleaned_pregames(start_year: int) -> list:
    pregame_list = []
    # Grab all entries from sql
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM CleanedGame WHERE seasonStartYear >= " + str(start_year))
            row = cursor.fetchone()
            while row:
                pregame_list.append(row)
                row = cursor.fetchone()
    return pregame_mapper.map_db_pregames_to_entities(pregame_list)

def get_future_games() -> list:
    pregame_list = []
    # Grab all entries from sql
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password) as conn:
        with conn.cursor() as cursor:
            query = "SELECT * FROM FutureCleanedGame WHERE 1=1"
            cursor.execute(query)
            row = cursor.fetchone()
            while row:
                pregame_list.append(row)
                row = cursor.fetchone()
    return pregame_mapper.map_db_pregames_to_entities_future(pregame_list)

def store_probabilities(game_id, home_prob, away_prob):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password) as conn:
        with conn.cursor() as cursor:
            query = "UPDATE PredictedGame SET modelHomeOdds = " + str(home_prob) + ", modelAwayOdds = " + str(away_prob) + "WHERE id = " + str(game_id)
            cursor.execute(query)