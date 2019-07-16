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
	playerStats = {}
	#print startingLineup
	for index, row in startingLineup.iterrows():
		teamId = row["Team_id"]
		playerId = row["Person_id"]
		onCourt.setdefault(teamId, []).append(playerId)
		# As substitutions happen, need to update onCourt for each team

	gameRoster = byPeriod.get_group(0)
	activePlayers = gameRoster[gameRoster['status'] == 'A']

	for index, row in activePlayers.iterrows():
		teamId = row["Team_id"]
		playerId = row["Person_id"]
		playerStats[ playerId ] = {
			"teamId": teamId,
			"possesions": 0.0,
			"offense": 0.0,
			"defense": 0.0,
		}
	for index, row in sortedPlays.iterrows():
		eventType = row["Event_Msg_Type"]
		eventNum = row["Event_Num"]
		player1 = row["Person1"]
		player2 = row["Person2"]
		teamId = row["Team_id"]
		period = row["Period"]
		
		if eventType == EventTypes.startPeriod:
			if period > 1:
				onCourt = defaultdict(list)
				periodLineup = byPeriod.get_group( period )
				for index, row in periodLineup.iterrows():
					teamId = row["Team_id"]
					playerId = row["Person_id"]
					onCourt.setdefault(teamId, []).append(playerId)

		if eventType == EventTypes.substitution:
			
			for lineup in onCourt.values():
				if player1 not in lineup:
					print "player not in this lineup"
				else:
					print lineup
					lineup.remove(player1)
					lineup.append(player2)
					print "made sub"
					print lineup
			# if player1 not in onCourt[teamId]:
			# 	print "player not in game"
				
			# else:
			# 	#print onCourt[teamId]
			# 	#print player1, player2
			# 	onCourt[teamId].remove( player1 )
			# 	onCourt[teamId].append( player2 )
			# 	print "made sub"
			

	### Todo at the start of a new period set the lineup again? 

	#print playerStats
	if name == "006728e4c10e957011e1f24878e6054a":
		break;
	