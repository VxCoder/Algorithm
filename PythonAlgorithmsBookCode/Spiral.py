DIRECTION = ((1, 0), (0, -1), (-1, 0), (0, 1))

def spiral(totalnum, poslist, direction, curStep, curChangeTime, maxStep):
	if totalnum <= len(poslist): return

	posList.append([posList[-1][0] + DIRECTION[direction][0], posList[-1][1] + DIRECTION[direction][1]])

	curStep -= 1
	if curStep == 0:
		direction = (direction + 1) % len(DIRECTION)
		curChangeTime -= 1
		if curChangeTime == 0:
			curChangeTime = 2
			maxStep += 1
		curStep = maxStep
			
 	spiral(totalnum, poslist, direction, curStep, curChangeTime, maxStep)

def showPos(poslist):
	minX, maxX = min(poslist, key=lambda pos: pos[0])[0], max(poslist, key=lambda pos: pos[0])[0]
	minY, maxY = min(poslist, key=lambda pos: pos[1])[1], max(poslist, key=lambda pos: pos[1])[1]
	strLen = len(str(len(poslist)))

	outList = [[" "*strLen for _ in range(maxX - minX+1)] for _ in range(maxY-minY+1)]

	for num , pos in enumerate(poslist):
		outList[pos[1]-minY][pos[0]-minX] = "{0:{width}}".format(num+1, width=strLen)

	print "\n".join([" ".join(row) for row in outList])

if __name__ == "__main__":
    posList = [(0,0)]
    spiral(5, posList, 0, 1, 2, 1)
    showPos(posList)
