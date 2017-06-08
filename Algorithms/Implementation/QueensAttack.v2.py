import math

n,k = 5, 3
rQueen,cQueen = [4, 3]
right = abs(n - cQueen)
top = abs(n - rQueen)
bottom = abs(1 - rQueen)
left = abs(1 - cQueen)
topright = min(top, right)
topleft = min(left, top)
bottomleft = min(bottom, left)
bottomright = min(bottom, right)
# print (right, top, bottom, left, topright, topleft, bottomleft, bottomright)
obstacles = [(2, 5), (4, 2), (2, 3)]
count = 0
if len(obstacles) == 0:
	count = right + top + bottom + left + topright + topleft + bottomleft + bottomright
else:
	for a0 in obstacles:
	    rObstacle,cObstacle = a0[0], a0[1]
	    if cObstacle == cQueen:
	    	if rObstacle in range(1, rQueen): 
	    		print ("bottom")
	    		count = count + (abs(rObstacle - rQueen) - 1)
	    		bottom = count
	    	if rObstacle in range(rQueen + 1, n + 1):
	    		print ("top")
	    		count = count + (abs(rObstacle - rQueen) - 1)
	    		top = count
	    	continue
	    if rObstacle == rQueen:
	    	if cObstacle in range(1, cQueen):
	    		print ("left")
	    		count = count + (abs(cObstacle - cQueen) - 1)
	    		left = count
	    	if cObstacle in range(cQueen + 1, n + 1):
	    		print ("right")
	    		count = count + (abs(cObstacle - cQueen) - 1)
	    		right = count
	    	continue
	    if rObstacle - rQueen != 0:
	   		slope = (cObstacle - cQueen) / (rObstacle - rQueen)
	   		if (slope == 1) or (slope == -1):
	   			dist = abs (rQueen - rObstacle) - 1
	   			print ("distance ", dist)
	   			if rObstacle > rQueen and cObstacle > cQueen:
	   				topright = dist
	   			if rObstacle > rQueen and cObstacle < cQueen:
	   				topleft = dist
	   			if rObstacle < rQueen and cObstacle < cQueen:
	   				bottomleft = dist
	   			if rObstacle < rQueen and cObstacle > cQueen:
	   				bottomright = dist
	count = right + top + bottom + left + topright + topleft + bottomleft + bottomright
print (count)