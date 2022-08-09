import os

filePath = 'E:\\fxpfinal\\testdeleteimgdata'       # 路径可以为包含图片和标注文件的文件夹

def delete_image_data(file_path):
    filelist = os.listdir(file_path)
    for file in filelist:
        if file.endswith('json'):
            with open(os.path.join(file_path, file), "r", encoding="utf-8") as f1, open(os.path.join(file_path, 'temp.json'), "w", encoding="utf-8") as f2:
                for line in f1:
                    a = line.split(':')
                    #print(a[0])
                    if a[0] == '  "imageData"' and a[1] != ' null,\n':
                        a[1] = ' null,\n'
                        print(file, "'s image data has been deleted!")

                    f2.write(':'.join(a))
            os.remove(os.path.join(file_path, file))
            os.rename(os.path.join(file_path, 'temp.json'), os.path.join(file_path, file))





if __name__ == '__main__':
    delete_image_data(filePath)