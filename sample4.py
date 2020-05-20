#로또 생성하기
from bangtal import *
import random

#배경
scene1 = Scene("배경1", "image4/배경1.png")
scene2 = Scene("배경2", "image4/배경2.png")

#로또번호 생성
number = [' ', ' ', ' ', ' ', ' ', ' ', ' ']      # 빈 리스트 생성(더 좋은 코드가 무엇?)

#시작 버튼 생성
start = Object('image4/start.png')
start.locate(scene1, 580, 150)
start.show()

#종료 버튼 생성
end = Object('image4/end.png')
end.locate(scene1, 580, 100)
end.show()

#시작 버튼 이벤트
def onMouseAction_start(x, y, action):
    global scene2, number, lotto
    enterScene(scene2)

    lotto = random.sample(range(1, 46), 7)
    print(lotto)

    #시작 버튼을 누를때마다 로또 번호가 생성된다.
    for i in range(7):
        number[i] = Object('image4/%d.png' % (lotto[i]))
        number[i].locate(scene2,22 + (i*180), 300)
        number[i].show()
    
    #장면을 배경2로 바꾸고 배경2에 로또 번호를 보여준다.
    start.locate(scene2, 580, 150)
    start.setImage('image4/restart.png')
    start.show()
    end.locate(scene2, 580, 100)
    end.show()

#종료 버튼 이벤트
def onMouseAction_end(x, y, action):
    endGame()

start.onMouseAction = onMouseAction_start
end.onMouseAction = onMouseAction_end

startGame(scene1)