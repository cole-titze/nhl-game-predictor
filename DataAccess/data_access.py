import pymssql
from Entities.Mappers import pregame_mapper
import os

def get_server():
    return 'nhl-game.database.windows.net'
def get_database():
    return os.environ["SQL_DATABASE"]
def get_username():
    return os.environ["SQL_USERNAME"]
def get_password():
    return os.environ["SQL_PASSWORD"]
def get_cleaned_pregames(start_year: int) -> list:
    pregame_list = []
    # Grab all entries from sql
    with pymssql.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM CleanedGame WHERE seasonStartYear >= " + str(start_year))
            row = cursor.fetchone()
            while row:
                pregame_list.append(row)
                row = cursor.fetchone()
    return pregame_mapper.map_db_pregames_to_entities(pregame_list)

def get_games_to_predict_query():
    predicted_games_query = "SELECT [dbo].[PredictedGame].[id],[CleanedGame].[homeTeamId],[CleanedGame].[awayTeamId]," \
                            "[seasonStartYear],[CleanedGame].[gameDate],[homeWinRatio],[homeRecentWinRatio]," \
                            "[homeRecentGoalsAvg],[homeRecentConcededGoalsAvg],[homeRecentSogAvg],[homeRecentPpgAvg]," \
                            "[homeRecentHitsAvg],[homeRecentPimAvg],[homeRecentBlockedShotsAvg]," \
                            "[homeRecentTakeawaysAvg],[homeRecentGiveawaysAvg],[homeGoalsAvg],[homeGoalsAvgAtHome]," \
                            "[homeRecentGoalsAvgAtHome],[homeConcededGoalsAvg],[homeConcededGoalsAvgAtHome]," \
                            "[homeRecentConcededGoalsAvgAtHome],[homeHoursSinceLastGame],[awayWinRatio]," \
                            "[awayRecentWinRatio],[awayRecentGoalsAvg],[awayRecentConcededGoalsAvg],[awayRecentSogAvg]," \
                            "[awayRecentPpgAvg],[awayRecentHitsAvg],[awayRecentPimAvg],[awayRecentBlockedShotsAvg]," \
                            "[awayRecentTakeawaysAvg],[awayRecentGiveawaysAvg],[awayGoalsAvg],[awayGoalsAvgAtAway]," \
                            "[awayRecentGoalsAvgAtAway],[awayConcededGoalsAvg],[awayConcededGoalsAvgAtAway]," \
                            "[awayRecentConcededGoalsAvgAtAway],[homeRosterOffenseValue],[homeRosterDefenseValue]," \
                            "[homeRosterGoalieValue],[awayRosterOffenseValue],[awayRosterDefenseValue]," \
                            "[awayRosterGoalieValue],[awayHoursSinceLastGame],[winner],[isExcluded],[hasBeenPlayed] " \
                            "FROM [dbo].[PredictedGame] " \
                            "INNER JOIN dbo.CleanedGame cleanedGame ON cleanedGame.id = [PredictedGame].[id]"
    return predicted_games_query

def get_games_to_predict() -> list:
    games = []
    # Grab all entries from sql
    with pymssql.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_games_to_predict_query())
            row = cursor.fetchone()
            while row:
                games.append(row)
                row = cursor.fetchone()
    return pregame_mapper.map_db_pregames_to_entities(games)

def store_probabilities(game_id, home_prob, away_prob):
    with pymssql.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            query = "UPDATE PredictedGame SET modelHomeOdds = " + str(home_prob) + ", modelAwayOdds = " + str(away_prob) + "WHERE id = " + str(game_id)
            cursor.execute(query)
            conn.commit()
            conn.close()