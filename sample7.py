#업다운 게임, -> 입력 횟수 제한, 계산기 프로그램 과제 가능..
from bangtal import *
import random

number = 0

#배경
scene1 = Scene("배경1", "image7/배경1.png")
scene2 = Scene("배경2", "image7/배경2.png")

#시작 버튼 생성
start = Object('image7/start.png')
start.locate(scene1, 580, 150)
start.show()

#종료 버튼 생성
end = Object('image7/end.png')
end.locate(scene1, 580, 100)
end.show()

#숫자키 버튼 생성
key = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
for i in range(3) :     #1~3
    key[i] = Object('image7/%d.png' % (i+1))
    key[i].locate(scene2, 500 + (i*90), 110)

for i in range(3) :     #4~6
    key[i+3] = Object('image7/%d.png' % (i+4))
    key[i+3].locate(scene2, 500 + (i*90), 180)

for i in range(3) :     #7~9
    key[i+6] = Object('image7/%d.png' % (i+7))
    key[i+6].locate(scene2, 500 + (i*90), 245)

#0
key[9] = Object('image7/10.png')
key[9].locate(scene2, 590, 45)
key[9].show()
#입력 버튼키
key[10] = Object('image7/11.png')
key[10].locate(scene2, 680, 45)
key[10].show()

#사용자 입력한 값을 저장하고 입력했는지 알기위한 isInput 변수를 선언한다.
input = 0
isInput = False

right = Object('image7/정답.png')
right.locate(scene2, 320, 380)

up = Object('image7/up.png')
up.locate(scene2, 320, 380)

down = Object('image7/down.png')
down.locate(scene2, 320, 380)


def onMouseActionDefault(object, x, y, action):
    global scene2, number, key, start, end, input, isInput, right, up, down

    right.hide()
    up.hide()
    down.hide()

    start.setImage('image7/restart.png')

    if object == start :    #시작 버튼을 클릭했다면
        #장면을 배경2로 바꾸고 배경2에 숫자 입력 판을 보여준다.
       
        enterScene(scene2)
    
        start.locate(scene2, 30, 150)
        end.locate(scene2, 30, 100)

        isInput = False

        number = random.randint(0,9)
        print(number)
        
        for i in range(11) :
            key[i].show()

    elif object == end :    #종료 버튼을 클릭했다면
        endGame()

    #숫자키를 클릭했다면 해당되는 수를 input에 저장.
    #isInput를 True 값으로 변경
    elif object == key[0] :
        input = 1
        isInput = True

    elif object == key[1] :
        input = 2
        isInput = True
    
    elif object == key[2] :
        input = 3
        isInput = True
    
    elif object == key[3] :
        input = 4
        isInput = True
    
    elif object == key[4] :
        input = 5
        isInput = True
    
    elif object == key[5] :
        input = 6
        isInput = True
    
    elif object == key[6] :
        input = 7
        isInput = True
    
    elif object == key[7] :
        input = 8
        isInput = True
    
    elif object == key[8] :
        input = 9
        isInput = True
    
    elif object == key[9] :
        input = 0
        isInput = True

    #입력키를 눌렀을때
    elif object == key[10] :
        if(isInput) :   #숫자키를 클릭하고 입력을 눌렀다면
            if (number == input) : 
                right.show()
            elif (number > input) :
                up.show()
            elif (number < input) :
                down.show()
        else :      #숫자키를 누르지 않고 입력값을 눌렀을 때
            showMessage("숫자를 클릭하고 입력 버튼을 눌러주세요.")

Object.onMouseActionDefault = onMouseActionDefault

startGame(scene1)
