import os

imgPath = 'D:\\xxx1/new_aqd'
txtPath = 'D:\\xc\\lbl\\labels'


def change_img_name_to_sequence(img_path):  #没啥用，change_img_and_txt_name_to_sequence()的一代版本
    img_names = os.listdir(img_path)
    i = 0
    for name in img_names:
        try:
            path = os.path.join(img_path, name)
            os.rename(path, os.path.join(img_path, 'bag_' + str(i)) + '.jpg')
            i += 1
        except FileNotFoundError:
            continue


def change_img_and_txt_name_to_sequence(img_path, txt_path, prefix):    # 重新排序并命名img和txt,加上前缀
    img_names = os.listdir(img_path)
    txt_names = [n[:-4] + '.txt' for n in img_names]
    for i in range(len(img_names)):
        os.rename(os.path.join(img_path, img_names[i]), os.path.join(img_path, prefix + '_' + str(i) + '.jpg'))
        try:
            os.rename(os.path.join(txt_path, txt_names[i]), os.path.join(txt_path, prefix + '_' + str(i) + '.txt'))
        except FileNotFoundError:
            print('file ', img_names[i], i, 'does not exist! cannot change name')


def add_name_prefix(img_path, txt_path, prefix):    # 将txt和img同时加上prefix前缀
    img_names = os.listdir(img_path)
    txt_names = [n[:-4] + '.txt' for n in img_names]

    for i in range(len(img_names)):

        os.rename(os.path.join(img_path, img_names[i]), os.path.join(img_path, prefix + '_' + img_names[i]))
        try:
            os.rename(os.path.join(txt_path, txt_names[i]), os.path.join(txt_path, prefix + '_' + txt_names[i]))
        except FileNotFoundError:
            print('file ', img_names[i], i, 'does not exist! Can not add prefix！')


def delete_name_prefix(img_path, txt_path, prefix): # 将txt和img同时删除prefix前缀
    img_names = os.listdir(img_path)
    txt_names = [n[:-4] + '.txt' for n in img_names]
    #print(img_names)
    #print(txt_names)
    for i in range(len(img_names)):
        os.rename(os.path.join(img_path, img_names[i]), os.path.join(img_path, img_names[i].replace(prefix + '_', '')))
        os.rename(os.path.join(txt_path, txt_names[i]), os.path.join(txt_path, txt_names[i].replace(prefix + '_', '')))




def rename_img(img_path):
    imglist = os.listdir(img_path)
    i = 1
    for img in imglist:

        os.rename(os.path.join(img_path, img), os.path.join(img_path, 'new_'+str(i)+'.jpg'))
        i += 1
#delete_name_prefix(imgPath, txtPath, 'openHat')
# 删掉图片之后重新排序，要在delete之后手动删除多余文件！！
# add_name_prefix(imgPath, txtPath, 'a')


# change_img_and_txt_name_to_sequence(imgPath, txtPath, 'xc')    # this also adds the prefix


# swap the label
# change_label(txtPath, '0', '5')
# change_label(txtPath, '1', '0')
# change_label(txtPath, '5', '1')
if __name__ == '__main__':
    rename_img(imgPath)