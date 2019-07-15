from enum import Enum
from enum import IntEnum
from hackathonEnums import EventTypes, boxScoreIndexes, lineupIndexes
import pandas as pd
import numpy as np

playByPlay = pd.read_csv("playByPlay.csv")
lineups = pd.read_csv("gameLineup.csv")
print(playByPlay.head(5))

groupedPlays = playByPlay.groupby("Game_id")
groupedLineups = lineups.groupby("Game_id")

for name, group in groupedPlays:
	sortedPlays = group.sort_values(["Period", "PC_Time", "WC_Time", "Event_Num"], ascending=[True, False, True, True])
	lineup = groupedLineups.get_group(name)

	byPeriod = lineup.groupby("Period")
	startingLineup = byPeriod.get_group(1)
	gameRoster = byPeriod.get_group(0)
	
	# print startingLineup
	activePlayers = gameRoster[gameRoster['status'] == 'A']
	