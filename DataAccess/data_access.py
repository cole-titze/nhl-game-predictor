import pytds
from Entities.Mappers import pregame_mapper
import os

def get_server():
    return '192.168.1.19'
def get_database():
    return os.environ["SQL_DATABASE"]
def get_username():
    return os.environ["SQL_USERNAME"]
def get_password():
    return os.environ["SQL_PASSWORD"]
def get_cleaned_pregames(start_year: int) -> list:
    pregame_list = []
    # Grab all entries from sql
    with pytds.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT CleanedGame.*, Game.seasonStartYear, Game.winner, Game.gameDate FROM CleanedGame "
                           "LEFT JOIN Game on gameId = Game.id WHERE seasonStartYear >=" + str(start_year))
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
    with pytds.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_games_to_predict_query())
            row = cursor.fetchone()
            while row:
                games.append(row)
                row = cursor.fetchone()
    return pregame_mapper.map_db_pregames_to_entities(games)

def store_probabilities(game_id, home_prob, away_prob):
    with pytds.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            query = "IF NOT EXISTS (SELECT * FROM GameOdds WHERE gameId = " + str(game_id) + ") INSERT INTO GameOdds(" \
                    "gameId, modelHomeOdds, modelAwayOdds) VALUES(" + str(game_id) + "," + str(home_prob) + "," \
                    + str(away_prob) + ") ELSE UPDATE GameOdds SET modelHomeOdds = " + str(home_prob) \
                    + ", modelAwayOdds = " + str(away_prob) + " WHERE gameId = " + str(game_id)
            cursor.execute(query)
            conn.commit()
            conn.close()

def store_model(model_data):
    model_id = 1
    with pytds.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            query = "IF NOT EXISTS (SELECT * FROM ClassificationModel WHERE id = " + str(model_id) \
                    + ") INSERT INTO ClassificationModel(id, modelFile) VALUES(" + str(model_id) + ",'" \
                    + str(model_data) + "') ELSE UPDATE ClassificationModel SET modelFile = '" \
                    + str(model_data) + "' WHERE id = " + str(model_id)
            cursor.execute(query)
            conn.commit()
            conn.close()

def get_model():
    model_id = 1
    with pytds.connect(server=get_server(), user=get_username(), password=get_password(), database=get_database()) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT modelFile FROM ClassificationModel WHERE id = " + str(model_id))
            model_data = cursor.fetchone()[0]
    return model_data
