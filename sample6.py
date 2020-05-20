#방탈출 중급 - 시계를 12번 클릭하면 12시간 지나가고 방의 밝기가 바뀐다.
from bangtal import *
import time

scene1 = Scene("룸1", "image6/배경-1.png")
scene2 = Scene("룸2", "image6/배경-2.png")

door1 = Object("image6/문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()

door2 = Object("image6/문-왼쪽-닫힘.png")
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object("image6/문-오른쪽-닫힘.png")
door3.locate(scene2, 900, 270)
door3.show()

key = Object("image6/열쇠.png")
key.locate(scene1, 600, 150)
key.setScale(0.2)

flowerpot = Object("image6/화분.png")
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

keypad = Object("image6/키패드.png")
keypad.locate(scene2, 885, 420)
keypad.show()

clock = Object("image6/12.png")
clock.locate(scene2, 920, 600)
clock.show()

password = Object("image6/암호.png")
password.locate(scene2, 450, 100)

closed1 = True
closed2 = True
closed3 = True

moved = False

locked1 = True

night = True
click = 1

#문1 이벤트
def onMouseAction_door1(x, y, action):
	global closed1
	if closed1 == True :
		if getHandObject() == key :
			door1.setImage( "image6/문-오른쪽-열림.png")
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
		door2.setImage("image6/문-왼쪽-열림.png")
		closed2 = False
	else : 
		enterScene(scene1)

#문3 이벤트
def onMouseAction_door3(x, y, action):
	global closed3, locked1

	if locked1 == True :
		showMessage("잠겨 있네. 어떻게 열지?")
		
	elif closed3 == True :
		door3.setImage("image6/문-오른쪽-열림.png")
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

#키패드 이벤트
def onMouseAction_keypad(x, y, action):

	showKeypad("BANGTAL", door3)

#키패드
def onKeypad() :
	global locked1

	locked1 = False;
	showMessage("잠금 해제!!!");

#시계 이벤트 (12시간 마다 밤 낮이 바뀐다.)
def onMouseAction_clock(x, y, action):
	global night, click

	clock.setImage("image6/%d.png" % click)
	click = click + 1

	if click == 13 :
		click = 1
		night = not night;	

	if (night == True) and (click == 7) :
		scene2.setLight(0.3)
		password.show()

	elif (night == False) and (click == 7) :
		scene2.setLight(1.0)
		password.hide()

door1.onMouseAction = onMouseAction_door1
door2.onMouseAction = onMouseAction_door2
door3.onMouseAction = onMouseAction_door3
key.onMouseAction = onMouseAction_key
flowerpot.onMouseAction = onMouseAction_flowerpot
keypad.onMouseAction = onMouseAction_keypad
door3.onKeypad = onKeypad
clock.onMouseAction = onMouseAction_clock

startGame(scene1)