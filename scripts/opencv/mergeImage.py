import cv2 as cv
import numpy as np
import PIL.Image as Img
import os

# 将多张图片合并为每行column张的一张图片， 默认大小为
def merge_image(column, img_path, size=(256, 256)):  # column 是每一行里图片的数量
    img_list = get_img_from_current_folder(img_path)
    # print(img_list)
    # result是最终需要的那一张图， 此处用np.empty(size)建立一个空的数组，方便下面for循环最后一步的连接
    result = np.empty((0, size[1]*column, 3), dtype=np.uint8)
    for i in range(len(img_list)//column+1):
        # temp是每一行合成的图片，由column张图片经过resize后组成
        temp = cv.cvtColor(np.zeros((size[0], size[1]*column), dtype=np.uint8), cv.COLOR_GRAY2BGR)
        # print(temp.shape)
        for j in range(column):
            if i*column+j >= len(img_list):     # 判断索引参数是否超过要合成的图片数量
                break
            img = cv.imread(os.path.join(img_path, img_list[i*column+j]))
            # print(os.path.join(img_path, img_list[i*column+j]))
            img = cv.resize(img, size)          # 将图片变为默认的size大小

            temp[:, j*size[1]:(j+1)*size[1], :] = img.copy()    # 将resize后的图片复制在相应位置上
        # 将temp连接到已经连接好的图片上
        result = np.vstack((result, temp))

    cv.imshow('result', result)
    cv.waitKey(0)

# image_clone 没啥用，不用看
def img_clone(source, destination, point, size, flag=cv.MIXED_CLONE, mask=None):    # 获取source的部分区域，将其贴到destination相应位置
    if not mask:
        mask = 255*np.ones(src.shape, dtype=np.uint8)
    cv.resize(source, size)
    return cv.seamlessClone(source, destination, mask, point, flags=flag)


def get_img_from_current_folder(img_path, img_type='.jpg'): # 仅从当前文件夹中获取图片， 返回图片名称的list
    img_list = os.listdir(img_path)
    ls = []
    for img in img_list:
        if img.lower().endswith(img_type):
            # print(img)
            ls.append(img)
    return ls if ls else None


def get_all_img_under_folder(img_path, img_type='.jpg'):        # 获取当前文件夹及其子文件夹的所有图片， 返回dict， key为路径，value为key对应路径文件夹下的图片名称list
    img_dict = {}
    for root, directory, files in os.walk(img_path):
        img_list = []
        for file in files:
            if file.lower().endswith(img_type):
                img_list.append(file)
        if len(img_list) > 0:
            img_dict.update({root: img_list})
    return img_dict if img_dict else None


if __name__ == '__main__':

    # merge_image(COLUMN_NUM, img_path=imgPath)
    src = cv.imread('C:/Users/Administrator/Desktop/test/1.png')
    dst = cv.imread('C:/Users/Administrator/Desktop/test/2.png')
    mixed = img_clone(src, dst, (dst.shape[0]//2, dst.shape[1]//2))
    cv.imshow('sdf', mixed)
    cv.waitKey(0)