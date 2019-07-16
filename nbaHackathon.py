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
	# startingLineup = byPeriod.get_group(1)
	# onCourt = defaultdict(list)
	playerStats = {}
	onCourt = []
	#print startingLineup
	# for index, row in startingLineup.iterrows():
	# 	teamId = row["Team_id"]
	# 	playerId = row["Person_id"]
	# 	onCourt.setdefault(teamId, []).append(playerId)
		# As substitutions happen, need to update onCourt for each team

	gameRoster = byPeriod.get_group(0)
	activePlayers = gameRoster[gameRoster['status'] == 'A']
	teamIds = gameRoster['Team_id'].unique()
	print teamIds
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
			onCourt = []
			possesions = 0.0
			score = {
				teamIds[0]: 0.0,
				teamIds[1]: 0.0,
			}

		# Loop through each play, if a basket occured, increment the appropriate score,
		# and increment offense or defensive stats for all players in onCourt
		# At the end of each possession, increment # of possessions
		# and increment possessions for all players in onCourt
		# period timers will be added to players who were subbed out because

		if eventType == EventTypes.substitution:
			if player1 not in onCourt:
				# not in our lineup so we give them the stats from the start of the period
				stats = playerStats[ player1 ]
				playerTeam = stats["teamId"]
				oppositeTeam = next( item for item in teamIds if item != playerTeam )
				stats["offense"] += score[ playerTeam ]
				stats["defense"] += score[ oppositeTeam ]
				stats["possesions"] += possesions
				
			else:
				# the players will already be accounted for because theyre on court
				onCourt.remove( player1 )
				onCourt.append( player2 )

	if name == "006728e4c10e957011e1f24878e6054a":
		break;
	