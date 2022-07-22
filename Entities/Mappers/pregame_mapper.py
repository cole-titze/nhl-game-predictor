from Entities import pregame_stats

def map_db_pregames_to_entities(game_list: list) -> list:
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
            winner=game[47],
            isExcluded=game[48])
        
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
            awayWinRatio=game[22],
            awayRecentWinRatio=game[23],
            awayRecentGoalsAvg=game[24],
            awayRecentConcededGoalsAvg=game[25],
            awayRecentSogAvg=game[26],
            awayRecentPpgAvg=game[27],
            awayRecentHitsAvg=game[28],
            awayRecentPimAvg=game[29],
            awayRecentBlockedShotsAvg=game[30],
            awayRecentTakeawaysAvg=game[31],
            awayRecentGiveawaysAvg=game[32],
            awayGoalsAvg=game[33],
            awayGoalsAvgAtAway=game[34],
            awayRecentGoalsAvgAtAway=game[35],
            awayConcededGoalsAvg=game[36],
            awayConcededGoalsAvgAtAway=game[37],
            awayRecentConcededGoalsAvgAtAway=game[38],
            homeRosterOffenseValue=game[39],
            homeRosterDefenseValue=game[40],
            homeRosterGoalieValue=game[41],
            awayRosterOffenseValue=game[42],
            awayRosterDefenseValue=game[43],
            awayRosterGoalieValue=game[44],
            winner=-1,
            isExcluded=False)

        pregame_list.append(pregame)

    return pregame_list
