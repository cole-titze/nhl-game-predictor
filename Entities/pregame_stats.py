from dataclasses import dataclass

@dataclass
class PregameStats:
    id: int
    homeTeamName: str
    awayTeamName: str
    seasonStartYear: int
    gameDate: str
    homeWinRatio: float
    homeRecentWinRatio: float
    homeRecentGoalsAvg: float
    homeRecentConcededGoalsAvg: float
    homeRecentSogAvg: float
    homeRecentPpgAvg: float
    homeRecentHitsAvg: float
    homeRecentPimAvg: float
    homeRecentBlockedShotsAvg: float
    homeRecentTakeawaysAvg: float
    homeRecentGiveawaysAvg: float
    homeGoalsAvg: float
    homeGoalsAvgAtHome: float
    homeRecentGoalsAvgAtHome: float
    homeConcededGoalsAvg: float
    homeConcededGoalsAvgAtHome: float
    homeRecentConcededGoalsAvgAtHome: float
    awayWinRatio: float
    awayRecentWinRatio: float
    awayRecentGoalsAvg: float
    awayRecentConcededGoalsAvg: float
    awayRecentSogAvg: float
    awayRecentPpgAvg: float
    awayRecentHitsAvg: float
    awayRecentPimAvg: float
    awayRecentBlockedShotsAvg: float
    awayRecentTakeawaysAvg: float
    awayRecentGiveawaysAvg: float
    awayGoalsAvg: float
    awayGoalsAvgAtAway: float
    awayRecentGoalsAvgAtAway: float
    awayConcededGoalsAvg: float
    awayConcededGoalsAvgAtAway: float
    awayRecentConcededGoalsAvgAtAway: float
    winner: float
    isExcluded: bool
    
    def map_data(game)-> list:
        x = []
        x.append(game.homeWinRatio)
        x.append(game.homeRecentWinRatio)
        x.append(game.homeRecentGoalsAvg)
        x.append(game.homeRecentConcededGoalsAvg)
        x.append(game.homeRecentSogAvg)
        x.append(game.homeRecentPpgAvg)
        x.append(game.homeRecentHitsAvg)
        x.append(game.homeRecentPimAvg)
        x.append(game.homeRecentBlockedShotsAvg)
        x.append(game.homeRecentTakeawaysAvg)
        x.append(game.homeRecentGiveawaysAvg)
        x.append(game.homeGoalsAvg)
        x.append(game.homeGoalsAvgAtHome)
        x.append(game.homeRecentGoalsAvgAtHome)
        x.append(game.homeConcededGoalsAvg)
        x.append(game.homeConcededGoalsAvgAtHome)
        x.append(game.homeRecentConcededGoalsAvgAtHome)
        x.append(game.awayWinRatio)
        x.append(game.awayRecentWinRatio)
        x.append(game.awayRecentGoalsAvg)
        x.append(game.awayRecentConcededGoalsAvg)
        x.append(game.awayRecentSogAvg)
        x.append(game.awayRecentPpgAvg)
        x.append(game.awayRecentHitsAvg)
        x.append(game.awayRecentPimAvg)
        x.append(game.awayRecentBlockedShotsAvg)
        x.append(game.awayRecentTakeawaysAvg)
        x.append(game.awayRecentGiveawaysAvg)
        x.append(game.awayGoalsAvg)
        x.append(game.awayGoalsAvgAtAway)
        x.append(game.awayRecentGoalsAvgAtAway)
        x.append(game.awayConcededGoalsAvg)
        x.append(game.awayConcededGoalsAvgAtAway)
        x.append(game.awayRecentConcededGoalsAvgAtAway)

        return x
