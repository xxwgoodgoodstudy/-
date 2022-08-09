import cv2 as cv
import numpy as np


def write_camera_video():
    cap = cv.VideoCapture('C:\\Users\\Administrator\\Desktop\\test\\202205141210.mp4')

    fourcc = cv.VideoWriter_fourcc(*'mp4v') # *'XVID' is .avi format
    ret, frame = cap.read()
    print(frame.shape)
    vw = cv.VideoWriter('C:\\Users\\Administrator\\Desktop\\test\\sdfoutput.mp4v', fourcc, 30.0, (1920, 1080))
    i = 0
    while ret:
        ret, frame = cap.read()
        if not ret or i > 200:
            break

        vw.write(frame)
        cv.imshow('frame', frame)
        i += 1
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    vw.release()
    cv.destroyAllWindows()


def mouse_control():
    # 名字可以随便取，顺序不能乱
    def mouse_callback(event, x, y, flags, userdata):
        print(event, x, y, flags, userdata)

    cv.namedWindow('mouse', cv.WINDOW_NORMAL)
    cv.resizeWindow('mouse', 640, 360)

    cv.setMouseCallback('mouse', mouse_callback, '123')

    img = np.zeros((360, 640, 3), dtype=np.uint8)
    while True:
        cv.imshow('mouse', img)
        key = cv.waitKey(1)
        if key == ord('q'):
            break

    cv.destroyAllWindows()


def trackbar_control():
    cv.namedWindow('trackbar', cv.WINDOW_NORMAL)
    cv.resizeWindow('trackbar', 640, 480)


    # 回调函数
    def callback_red(value):
        print('red: ', value)
    def callback_green(value):
        print('green: ', value)
    def callback_blue(value):
        print('blue: ', value)

    cv.createTrackbar('R', 'trackbar', 0, 255, callback_red)
    cv.createTrackbar('G', 'trackbar', 0, 255, callback_green)
    cv.createTrackbar('B', 'trackbar', 0, 255, callback_blue)

    #背景图
    img = np.zeros((480, 640, 3), np.uint8)

    while True:
        r = cv.getTrackbarPos('R', 'trackbar')
        g = cv.getTrackbarPos('G', 'trackbar')
        b = cv.getTrackbarPos('B', 'trackbar')

        img[:] = [b, g, r]
        cv.imshow('trackbar', img)

        key = cv.waitKey(10)
        if key == ord('q'):
            break

    cv.destroyAllWindows()


def change_color_space():
    def callback():
        pass
    cv.namedWindow('color', cv.WINDOW_NORMAL)
    cv.resizeWindow('color', 640, 480)

    img = cv.imread('C:\\Users\\Administrator\\Desktop\\aa\\openHat_4.jpg')
    colorspaces=[
        cv.COLOR_BGR2RGBA,
        cv.COLOR_BGR2GRAY,
        cv.COLOR_BGR2HLS,
        cv.COLOR_BGR2HSV,
        cv.COLOR_BGR2YUV
    ]

    cv.createTrackbar('trackbar', 'color', 0, 4, callback)

    while True:
        index = cv.getTrackbarPos('trackbar', 'color')
        cvt_img = cv.cvtColor(img, colorspaces[index])

        cv.imshow('color', cvt_img)
        key = cv.waitKey(10)

        if key == ord('q'):
            break

    cv.destroyAllWindows()


if __name__ == '__main__':
    write_camera_video()