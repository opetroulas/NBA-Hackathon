from enum import Enum
from enum import IntEnum
from hackathonEnums import EventTypes, boxScoreIndexes, lineupIndexes


# with open ("Play_by_Play.txt", "r") as myfile:
#     playByPlay=myfile.readlines()
# print ( "num lines - " + str(len(playByPlay )))


def readFile( name ):
	with open ( name , 'r' ) as myfile:
		data = myfile.readlines()
	return data 

def readLine( line ):
	return line.replace("\n", "").replace( "\r", "" ).replace('"', "").split('\t');

def writeToFile ( lines ):
	with open ( 'test.txt', 'a') as file:
		file.writelines( lines )

playByPlay = readFile( "Play_by_Play.txt" )
gameLineup = readFile( "Game_Lineup.txt" )

numLines = len(gameLineup)
print numLines
currentGameId = "006728e4c10e957011e1f24878e6054a"

# for i in range( 1, 3 ): 
# 	line = gameLineup[i]
# 	print line[1: len(currentGameId) + 1]
# 	print currentGameId
# i = 1;
teamAid = teamBid = ""

teamA = teamB = {}

i = numTeams = 1

while ( True ):
	
	lineSplit = readLine( playByPlay[i] )	
	gameId = lineSplit[boxScoreIndexes.gameId]
	
	if not teamAid and not teamBid:
		roster = []
		print "getting roster"
		for item in gameLineup:
			if item[1: len( currentGameId ) + 1 ] == currentGameId:
				roster.append( item )
		for line in roster:
			clean = readLine( line )
			teamId = clean[ lineupIndexes.teamId ]
			playerId = clean[ lineupIndexes.playerId ]
			if not teamAid:
				teamAid = teamId
				
			elif not teamBid:
				teamBid = teamId
				
			if teamId == teamAid:
				teamA[ playerId ] = (0.0, 0.0)
			elif teamId == teamBid:
				teamB[ playerId ] = (0.0, 0.0)


	if gameId != currentGameId :

		print ( "new game " + gameId )
		
		lines = [];
		for player in teamA:
			line = currentGameId + '\t' + player + '\t' + str(teamA[player][0]/100.0) + '\t' + str(teamA[player][1]/100.0) + '\n'
			lines.append( line ) 
		for player in teamB:
			line = currentGameId + '\t' + player + '\t' + str(teamB[player][0]/100.0) + '\t' + str(teamB[player][1]/100.0) + '\n'
			lines.append( line ) 
		writeToFile ( lines )
		
		
		teamAid = teamBid = ""
		teamA = teamB = {}
		currentGameId = gameId;
		numTeams += 1

	else:
		# calculate efficiencies 
		i += 1

	if numTeams > 3:
		# remove when done debugging 
		break;

