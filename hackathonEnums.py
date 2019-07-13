from enum import Enum
from enum import IntEnum

class EventTypes(IntEnum):
	madeShot = 1
	missedShot = 2
	freeThrow = 3
	rebound = 4
	turnover = 5
	foul = 6
	violation = 7
	substitution = 8
	timout = 9
	jumpBall = 10
	ejection = 11
	startPeriod = 12
	endPeriod = 13
	memo = 15
	stoppage = 20

class boxScoreIndexes(IntEnum):
	gameId = 0
	eventNum = 1
	eventType = 2
	period = 3
	actionType = 6
	option1 = 7
	option2 = 8
	option3 = 9
	teamId = 10
	person1Id = 11
	person2Id = 12
	person3Id = 13
	teamIdType = 14
	person1Type = 15
	person2Type = 16
	person3Type = 17

class lineupIndexes(IntEnum):
	gameId = 0
	period = 1
	playerId = 2
	teamId = 3

class freeThrowTypes(IntEnum):
	and1 = 10
	firstof2 = 11
	secondof2 = 12
	firstof3 = 13
	thirdof3 = 15
	technical = 16
	flagrant1 = 18
	flagrant2 = 19
	flagrantSingle = 20
	clearPath1 = 25
	clearPath2 = 26


class foulTypes(IntEnum):
	technical = 11
	shooting = 2
	clearPath = 9
	doublePersonal = 10
	technical = 11
	nonUnsportsmanlikeTechnical = 12
	hangingTechnical = 13
	flagrant1 = 14
	flagrant2 = 15


