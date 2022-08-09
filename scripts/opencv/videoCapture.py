import cv2
import os

videoPath = 'D:\\fxp\\dusk'
videos = os.listdir(videoPath)
videoNames = []
for video in videos:
    if video.lower().endswith('.mp4'):
        videoNames.append(video)

step = 25            # 帧数:每25帧取一张图
print(videoNames)


def save_image(image, addr, imgname):
    address = addr + '/' + imgname + '.jpg'         # 路径 + 命名
    cv2.imwrite(address, image)


videoNum = 80
for videoName in videoNames:
    cap = cv2.VideoCapture(videoPath + '/' + videoName); ';;lpp0'
    videoNum += 1
    ret = cap.grab()            # 获取下一帧
    i = 0
    count = 0
    while ret:
        i += 1
        if i % step == 0:
            r, frame = cap.retrieve()           # frame 是获取的图像
            # print(i)
            count += 1
            save_image(frame, 'D:\\fxp\\2', 'video' + str(videoNum) + ' ' + str(count))

        ret = cap.grab()


