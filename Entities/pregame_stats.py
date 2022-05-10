from dataclasses import dataclass

import numpy as np


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
    
    def map_data(self) -> np.array:
        x = []
        x.append(float(self.homeWinRatio))
        x.append(float(self.homeRecentWinRatio))
        x.append(float(self.homeRecentGoalsAvg))
        x.append(float(self.homeRecentConcededGoalsAvg))
        x.append(float(self.homeRecentSogAvg))
        x.append(float(self.homeRecentPpgAvg))
        x.append(float(self.homeRecentHitsAvg))
        x.append(float(self.homeRecentPimAvg))
        x.append(float(self.homeRecentBlockedShotsAvg))
        x.append(float(self.homeRecentTakeawaysAvg))
        x.append(float(self.homeRecentGiveawaysAvg))
        x.append(float(self.homeGoalsAvg))
        x.append(float(self.homeGoalsAvgAtHome))
        x.append(float(self.homeRecentGoalsAvgAtHome))
        x.append(float(self.homeConcededGoalsAvg))
        x.append(float(self.homeConcededGoalsAvgAtHome))
        x.append(float(self.homeRecentConcededGoalsAvgAtHome))
        x.append(float(self.awayWinRatio))
        x.append(float(self.awayRecentWinRatio))
        x.append(float(self.awayRecentGoalsAvg))
        x.append(float(self.awayRecentConcededGoalsAvg))
        x.append(float(self.awayRecentSogAvg))
        x.append(float(self.awayRecentPpgAvg))
        x.append(float(self.awayRecentHitsAvg))
        x.append(float(self.awayRecentPimAvg))
        x.append(float(self.awayRecentBlockedShotsAvg))
        x.append(float(self.awayRecentTakeawaysAvg))
        x.append(float(self.awayRecentGiveawaysAvg))
        x.append(float(self.awayGoalsAvg))
        x.append(float(self.awayGoalsAvgAtAway))
        x.append(float(self.awayRecentGoalsAvgAtAway))
        x.append(float(self.awayConcededGoalsAvg))
        x.append(float(self.awayConcededGoalsAvgAtAway))
        x.append(float(self.awayRecentConcededGoalsAvgAtAway))

        return np.asarray(x)
