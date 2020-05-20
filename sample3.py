#사진앨범 만들기
from bangtal import *

scene1 = Scene('배경', 'image3/배경.jpg')

rightArrow = Object('image3/오른쪽_화살표.png')
rightArrow.locate(scene1, 1190, 320)
rightArrow.setScale(0.3)
rightArrow.show()

leftArrow = Object('image3/왼쪽_화살표.png')
leftArrow.locate(scene1, 0, 320)
leftArrow.setScale(0.3)
leftArrow.show()

imageList = [' ', ' ', ' ', ' ', ' ']      # 빈 리스트 생성
index = 0

#사진 이미지 생성
for i in range(5):
	imageList[i] = Object('image3/%d.jpg' % (i+1))
	imageList[i].locate(scene1, 530, 250)

#오른쪽 화살표 버튼 이벤트
def onMouseAction_rightArrow(x, y, action):
	global index

	if index!=4 :
		imageList[index].hide()
		imageList[index+1].show()
		index = index + 1

#왼쪽 화살표 버튼 이벤트
def onMouseAction_leftArrow(x, y, action):
	global index

	if index!=0 :
		imageList[index].hide()
		imageList[index-1].show()
		index = index - 1

rightArrow.onMouseAction = onMouseAction_rightArrow
leftArrow.onMouseAction = onMouseAction_leftArrow

imageList[index].show()
startGame(scene1)
