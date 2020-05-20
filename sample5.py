#가위 바위 보 게임
from bangtal import *
import random

scene1 = Scene('배경', 'image5/배경.jpg')

rock = Object('image5/묵.png')
rock.locate(scene1, 250, 300)

sissors = Object('image5/찌.png')
sissors.locate(scene1, 550, 300)

paper = Object('image5/빠.png')
paper.locate(scene1, 850, 300)

rock_left = Object('image5/묵_왼쪽.png')
rock_left.locate(scene1, 0, 300)
rock_left.setScale(0.7)

sissors_left = Object('image5/가위_왼쪽.png')
sissors_left.locate(scene1, 0, 300)
sissors_left.setScale(0.7)

paper_left = Object('image5/보_왼쪽.png')
paper_left.locate(scene1, 0, 300)
paper_left.setScale(0.7)

rock_right = Object('image5/묵_오른쪽.png')
rock_right.locate(scene1, 770, 300)
rock_right.setScale(0.7)

sissors_right = Object('image5/가위_오른쪽.png')
sissors_right.locate(scene1, 770, 300)
sissors_right.setScale(0.7)

paper_right = Object('image5/보_오른쪽.png')
paper_right.locate(scene1, 770, 300)
paper_right.setScale(0.7)

start = Object('image5/start.png')
start.locate(scene1, 580, 150)
start.show()

end = Object('image5/end.png')
end.locate(scene1, 580, 100)
end.show()

computer = 0

#주먹 이벤트
def onMouseAction_rock(x, y, action):
    global computer

    rock.hide()
    sissors.hide()
    paper.hide()

    if computer == 0:
        rock_left.show()
        rock_right.show()

        showMessage('비겼습니다.')
    
    elif computer == 1:
        sissors_left.show()
        rock_right.show()

        showMessage('이겼습니다.')
    else:
        paper_left.show()
        rock_right.show()

        showMessage('졌습니다.')

    start.setImage('image5/restart.png')
    start.show()
    end.show()

#가위 이벤트
def onMouseAction_sissors(x, y, action):
    global computer

    rock.hide()
    sissors.hide()
    paper.hide()

    if computer == 0:
        rock_left.show()
        sissors_right.show()

        showMessage('졌습니다.')
    
    elif computer == 1:
        sissors_left.show()
        sissors_right.show()

        showMessage('비겼습니다..')
    else:
        paper_left.show()
        sissors_right.show()

        showMessage('이겼습니다..')

    start.setImage('image5/restart.png')
    start.show()
    end.show()

#보 이벤트
def onMouseAction_paper(x, y, action):
    global computer

    rock.hide()
    sissors.hide()
    paper.hide()

    if computer == 0:
        rock_left.show()
        paper_right.show()

        showMessage('이겼습니다..')
    
    elif computer == 1:
        sissors_left.show()
        paper_right.show()

        showMessage('졌습니다..')
    else:
        paper_left.show()
        paper_right.show()

        showMessage('비겼습니다..')

    start.setImage('image5/restart.png')
    start.show()
    end.show()

#시작 버튼 이벤트
def onMouseAction_start(x, y, action):
    global computer
    
    start.hide()
    end.hide()
    rock_left.hide()
    sissors_left.hide()
    paper_left.hide()
    rock_right.hide()
    sissors_right.hide()
    paper_right.hide()

    rock.show()
    sissors.show()
    paper.show()

    showMessage('묵찌빠 중 하나를 골라주세요.')

    computer = random.randint(0, 2)

#종료 버튼 이벤트
def onMouseAction_end(x, y, action):
    endGame()

start.onMouseAction = onMouseAction_start
end.onMouseAction = onMouseAction_end
rock.onMouseAction = onMouseAction_rock
sissors.onMouseAction = onMouseAction_sissors
paper.onMouseAction = onMouseAction_paper

startGame(scene1)
