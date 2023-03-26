from Entities import pregame_stats

def map_db_pregames_to_entities(game_list: list) -> list:
    pregame_list = []
    for game in game_list:
        pregame = pregame_stats.PregameStats(
            id=game[0],
            homeWinRatio=game[1],
            homeRecentWinRatio=game[2],
            homeRecentGoalsAvg=game[3],
            homeRecentConcededGoalsAvg=game[4],
            homeRecentSogAvg=game[5],
            homeRecentPpgAvg=game[6],
            homeRecentHitsAvg=game[7],
            homeRecentPimAvg=game[8],
            homeRecentBlockedShotsAvg=game[9],
            homeRecentTakeawaysAvg=game[10],
            homeRecentGiveawaysAvg=game[11],
            homeGoalsAvg=game[12],
            homeGoalsAvgAtHome=game[13],
            homeRecentGoalsAvgAtHome=game[14],
            homeConcededGoalsAvg=game[15],
            homeConcededGoalsAvgAtHome=game[16],
            homeRecentConcededGoalsAvgAtHome=game[17],
            homeHoursSinceLastGame=game[18],
            awayWinRatio=game[19],
            awayRecentWinRatio=game[20],
            awayRecentGoalsAvg=game[21],
            awayRecentConcededGoalsAvg=game[21],
            awayRecentSogAvg=game[23],
            awayRecentPpgAvg=game[24],
            awayRecentHitsAvg=game[25],
            awayRecentPimAvg=game[26],
            awayRecentBlockedShotsAvg=game[27],
            awayRecentTakeawaysAvg=game[28],
            awayRecentGiveawaysAvg=game[29],
            awayGoalsAvg=game[30],
            awayGoalsAvgAtAway=game[31],
            awayRecentGoalsAvgAtAway=game[32],
            awayConcededGoalsAvg=game[33],
            awayConcededGoalsAvgAtAway=game[34],
            awayRecentConcededGoalsAvgAtAway=game[35],
            homeRosterOffenseValue=game[36],
            homeRosterDefenseValue=game[37],
            homeRosterGoalieValue=game[38],
            awayRosterOffenseValue=game[39],
            awayRosterDefenseValue=game[40],
            awayRosterGoalieValue=game[41],
            awayHoursSinceLastGame=game[42],
            seasonStartYear=game[43],
            winner=game[44],
            gameDate=game[45]
        )
        
        pregame_list.append(pregame)

    return pregame_list


def map_db_pregames_to_entities_future(game_list: list) -> list:
    pregame_list = []
    for game in game_list:
        pregame = pregame_stats.PregameStats(
            id=game[0],
            homeTeamName=game[1],
            awayTeamName=game[2],
            seasonStartYear=game[3],
            gameDate=game[4],
            homeWinRatio=game[5],
            homeRecentWinRatio=game[6],
            homeRecentGoalsAvg=game[7],
            homeRecentConcededGoalsAvg=game[8],
            homeRecentSogAvg=game[9],
            homeRecentPpgAvg=game[10],
            homeRecentHitsAvg=game[11],
            homeRecentPimAvg=game[12],
            homeRecentBlockedShotsAvg=game[13],
            homeRecentTakeawaysAvg=game[14],
            homeRecentGiveawaysAvg=game[15],
            homeGoalsAvg=game[16],
            homeGoalsAvgAtHome=game[17],
            homeRecentGoalsAvgAtHome=game[18],
            homeConcededGoalsAvg=game[19],
            homeConcededGoalsAvgAtHome=game[20],
            homeRecentConcededGoalsAvgAtHome=game[21],
            homeHoursSinceLastGame=game[22],
            awayWinRatio=game[23],
            awayRecentWinRatio=game[24],
            awayRecentGoalsAvg=game[25],
            awayRecentConcededGoalsAvg=game[26],
            awayRecentSogAvg=game[27],
            awayRecentPpgAvg=game[28],
            awayRecentHitsAvg=game[29],
            awayRecentPimAvg=game[30],
            awayRecentBlockedShotsAvg=game[31],
            awayRecentTakeawaysAvg=game[32],
            awayRecentGiveawaysAvg=game[33],
            awayGoalsAvg=game[34],
            awayGoalsAvgAtAway=game[35],
            awayRecentGoalsAvgAtAway=game[36],
            awayConcededGoalsAvg=game[37],
            awayConcededGoalsAvgAtAway=game[38],
            awayRecentConcededGoalsAvgAtAway=game[39],
            homeRosterOffenseValue=game[40],
            homeRosterDefenseValue=game[41],
            homeRosterGoalieValue=game[42],
            awayRosterOffenseValue=game[43],
            awayRosterDefenseValue=game[44],
            awayRosterGoalieValue=game[45],
            awayHoursSinceLastGame=game[46],
            winner=-1,
            isExcluded=False)

        pregame_list.append(pregame)

    return pregame_list
