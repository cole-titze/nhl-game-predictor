from dataclasses import dataclass

@dataclass
class PregameStats:
    home_team_name: str
    away_team_name: str
    season_start_year: int
    home_win_ratio: float
    home_recent_win_ratio: float
    home_recent_goals_avg: float
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
    awayRecentConcededGoals: float # should be avg
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
