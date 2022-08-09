import os
import shutil
allInOnePath = 'D:\\aa'

# 以'D:\\aa'为例，jsonChangeLabel()会修改aa文件夹下的所有文件夹之中的json文件
# 使用时注意修改allInOnePath,以及函数中的有关标签信息
def jsonChangeLabel(all_in_one_path):
    folders = os.listdir(all_in_one_path)
    print(folders)

    for dir in folders:
        print(dir)
        dir_path = os.path.join(all_in_one_path, dir)
        filelist = os.listdir(dir_path)
        json = ''

        for file in filelist:
            print(file)
            #if file[:-4] != json[:-5]:
                #new_name = file[:-3] + 'json'
            if file.endswith('json'):
                new_name = file[7:-4] + 'json'
                with open(os.path.join(dir_path, file), "r", encoding="utf-8") as f1, open(os.path.join(dir_path, new_name), "w", encoding="utf-8") as f2:
                    for line in f1:
                        a = line.split(':')
                        print(a[0])
                        if a[0] == '      "label"':
                            if a[1] == ' "righthang",\n':       # previous label
                                a[1] = ' "righthand",\n'     # label changed, the format is same

                        f2.write(':'.join(a))
                        os.remove(os.path.join(dir_path, file))
                        os.rename(new_name, file)



if __name__ == '__main__':
    jsonChangeLabel(allInOnePath)