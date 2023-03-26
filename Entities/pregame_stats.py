from dataclasses import dataclass

import numpy as np

@dataclass
class PregameStats:
    id: int
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
    homeHoursSinceLastGame: float
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
    homeRosterOffenseValue: float
    homeRosterDefenseValue: float
    homeRosterGoalieValue: float
    awayRosterOffenseValue: float
    awayRosterDefenseValue: float
    awayRosterGoalieValue: float
    awayHoursSinceLastGame: float
    winner: float

    def map_data(self) -> np.array:
        x = [float(self.homeWinRatio), float(self.homeRecentWinRatio), float(self.homeRecentGoalsAvg),
             float(self.homeRecentConcededGoalsAvg), float(self.homeRecentSogAvg), float(self.homeRecentPpgAvg),
             float(self.homeRecentHitsAvg), float(self.homeRecentPimAvg), float(self.homeRecentBlockedShotsAvg),
             float(self.homeRecentTakeawaysAvg), float(self.homeRecentGiveawaysAvg), float(self.homeGoalsAvg),
             float(self.homeGoalsAvgAtHome), float(self.homeRecentGoalsAvgAtHome), float(self.homeConcededGoalsAvg),
             float(self.homeConcededGoalsAvgAtHome), float(self.homeRecentConcededGoalsAvgAtHome),
             float(self.homeHoursSinceLastGame), float(self.awayWinRatio), float(self.awayRecentWinRatio),
             float(self.awayRecentGoalsAvg), float(self.awayRecentConcededGoalsAvg), float(self.awayRecentSogAvg),
             float(self.awayRecentPpgAvg), float(self.awayRecentHitsAvg), float(self.awayRecentPimAvg),
             float(self.awayRecentBlockedShotsAvg), float(self.awayRecentTakeawaysAvg),
             float(self.awayRecentGiveawaysAvg), float(self.awayGoalsAvg), float(self.awayGoalsAvgAtAway),
             float(self.awayRecentGoalsAvgAtAway), float(self.awayConcededGoalsAvg),
             float(self.awayConcededGoalsAvgAtAway), float(self.awayRecentConcededGoalsAvgAtAway),
             float(self.homeRosterOffenseValue), float(self.homeRosterDefenseValue), float(self.homeRosterGoalieValue),
             float(self.awayRosterOffenseValue), float(self.awayRosterDefenseValue), float(self.awayRosterGoalieValue),
             float(self.awayHoursSinceLastGame)]

        return np.asarray(x)
