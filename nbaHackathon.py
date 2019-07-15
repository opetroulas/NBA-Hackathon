from enum import Enum
from enum import IntEnum
from hackathonEnums import EventTypes, boxScoreIndexes, lineupIndexes
import pandas as pd
import numpy as np
from collections import defaultdict

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
	onCourt = defaultdict(list)

	print startingLineup
	for index, row in startingLineup.iterrows():
		teamId = row["Team_id"]
		playerId = row["Person_id"]
		print onCourt
		onCourt.setdefault(teamId, []).append(playerId)
	gameRoster = byPeriod.get_group(0)
	print onCourt
	activePlayers = gameRoster[gameRoster['status'] == 'A']
	#print activePlayers

	if name == "006728e4c10e957011e1f24878e6054a":
		break;
	