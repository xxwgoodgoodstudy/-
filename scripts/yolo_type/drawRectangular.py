import cv2
import os

imgPath = 'D:\\xc\\lbl\\img'
imgNames = os.listdir(imgPath)
txtPath = 'D:\\xc\\lbl/labels'
txtNames = [n[:-4] + '.txt' for n in imgNames]
savePath = 'D:\\xc\\lbl/ROI'
print(imgNames)
print(txtNames)
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]        # one label corresponds to one color
'''


                    x = (float(lane[1]) - 0.5 * float(lane[3])) * w
                    y = (float(lane[2]) - 0.5 * float(lane[4])) * h
                    xx = (float(lane[1]) + 0.5 * float(lane[3])) * w
                    yy = (float(lane[2]) + 0.5 * float(lane[4])) * h 
'''


def draw_rectangle_and_save_to_original_image(img_path, txt_path):
    img_names = os.listdir(img_path)
    txt_names = [n[:-4] + '.txt' for n in img_names]

    for i in range(len(img_names)):
        img = cv2.imread(os.path.join(img_path, img_names[i]))
        h, w = int(img.shape[0]), int(img.shape[1])
        with open(os.path.join(txt_path, txt_names[i]), 'r') as f:
            for line in f:
                parameters = [float(i) for i in line.split(' ')]
                parameters[0] = int(parameters[0])

                top_left = (int(parameters[1]*w - 0.5*parameters[3]*w), int(parameters[2]*h - 0.5*parameters[4]*h))
                bottom_right = (int(parameters[1]*w + 0.5*parameters[3]*w), int(parameters[2]*h + 0.5*parameters[4]*h))
                print(top_left, bottom_right)
                draw_0 = cv2.rectangle(img, top_left, bottom_right, color[parameters[0]], 2)
                cv2.imwrite(os.path.join(img_path, img_names[i]), draw_0)

    kkkk = cv2.imread(os.path.join(img_path, img_names[i]))
    cv2.imshow('sdf', kkkk)


def getROI(img_path, txt_path, save_path):
    img_names = os.listdir(img_path)
    txt_names = [n[:-4] + '.txt' for n in img_names]
    index = 0
    for i in range(len(img_names)):
        img = cv2.imread(os.path.join(img_path, img_names[i]))
        h, w = int(img.shape[0]), int(img.shape[1])
        try:
            with open(os.path.join(txt_path, txt_names[i]), 'r') as f:
                for line in f:
                    parameters = [float(i) for i in line.split(' ')]
                    parameters[0] = int(parameters[0])
                    top_left = (int(parameters[1] * w - 0.5 * parameters[3] * w), int(parameters[2] * h - 0.5 * parameters[4] * h))
                    bottom_right = (int(parameters[1] * w + 0.5 * parameters[3] * w), int(parameters[2] * h + 0.5 * parameters[4] * h))

                    cut = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
                    cv2.imwrite(os.path.join(save_path, str(index)+'.jpg'), cut)
                    index += 1


        except FileNotFoundError:
            print('Image ', img_names[i], ' has no corresponding txt files.')

if __name__ == '__main__':
    getROI(imgPath, txtPath, savePath)