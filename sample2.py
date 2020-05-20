#방탈출(초급)
from bangtal import *

scene1 = Scene("룸1", "image2/배경-1.png")
scene2 = Scene("룸2", "image2/배경-2.png")

door1 = Object("image2/문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()

door2 = Object("image2/문-왼쪽-닫힘.png")
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object("image2/문-오른쪽-닫힘.png")
door3.locate(scene2, 900, 270)
door3.show()

key = Object("image2/열쇠.png")
key.locate(scene1, 600, 150)
key.setScale(0.2)

flowerpot = Object("image2/화분.png")
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

closed1 = True
closed2 = True
closed3 = True

moved = False

locked1 = True

#문1 이벤트
def onMouseAction_door1(x, y, action):
	global closed1
	if closed1 == True :
		if getHandObject() == key :
			door1.setImage("image2/문-오른쪽-열림.png")
			closed1 = False;
			showMessage("문이 열렸습니다.")
		else : 
			showMessage("문을 열기위해서 키를 사용해야합니다.")
	else : 
		enterScene(scene2)

#문2 이벤트
def onMouseAction_door2(x, y, action):
	global closed2

	if closed2 == True :
		door2.setImage("image2/문-왼쪽-열림.png")
		closed2 = False
	else : 
		enterScene(scene1)

#문3 이벤트
def onMouseAction_door3(x, y, action):
	global closed3
		
	if closed3 == True :
		door3.setImage("image2/문-오른쪽-열림.png")
		closed3 = False
		
	else : 
		endGame()

#열쇠 이벤트
def onMouseAction_key(x, y, action):

	key.pick();

#화분 이벤트
def onMouseAction_flowerpot(x, y, action):
	global moved

	if action == MouseActionType.DRAG_LEFT :
		flowerpot.locate(scene1, 450, 150)
		moved = True

	elif action == MouseActionType.DRAG_RIGHT :
		flowerpot.locate(scene1, 650, 150)
		moved = True

	if moved :
		key.show()

door1.onMouseAction = onMouseAction_door1
door2.onMouseAction = onMouseAction_door2
door3.onMouseAction = onMouseAction_door3
key.onMouseAction = onMouseAction_key
flowerpot.onMouseAction = onMouseAction_flowerpot

startGame(scene1)