#방탈출(입문)

from bangtal import *

scene1 = Scene("룸1", "image1/배경-1.png")

door1 = Object("image1/문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()

closed1 = True

#문1 이벤트
def onMouseAction_door1(x, y, action):
	global closed1
	if closed1 == True :
		door1.setImage("image1/문-오른쪽-열림.png")
		closed1 = False;
		showMessage("문이 열렸습니다.")
	else : 
		endGame()

door1.onMouseAction = onMouseAction_door1

startGame(scene1)
