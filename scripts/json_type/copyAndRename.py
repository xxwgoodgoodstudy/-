import os
import shutil

allInOnePath = 'D:\\xxx1'


def copyRename(all_in_one_path):
    folders = os.listdir(all_in_one_path)
    print(folders)

    for dir in folders:
        print(dir)
        dir_path = os.path.join(all_in_one_path, dir)
        filelist = os.listdir(dir_path)

        # find the .json file
        json = ''
        for file in filelist:
            if file.endswith('json'):
                json = file
                filelist.remove(file)
                break

        #
        for file in filelist:
            print(file)
            if file[:-4] != json[:-5]:
                new_name = file[:-3] + 'json'
                with open(os.path.join(dir_path, json), "r", encoding="utf-8") as f1, open(os.path.join(dir_path, new_name), "w", encoding="utf-8") as f2:
                    for line in f1:
                        a = line.split(':')
                        #print(a[0])
                        if a[0] == '  "imagePath"':
                            a[1] = ' "'+file+'",\n'     # "video35 85.jpg",
                            print(new_name, ' changed to ', file)
                        f2.write(':'.join(a))





if __name__ == '__main__':
    copyRename(allInOnePath)