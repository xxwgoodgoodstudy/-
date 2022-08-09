import os
import re

'''
def checkLegalName(fixed_name, file_names):
    for name in file_names:
        if not re.search()
'''

def change_label(filepath, before, after):      # before and after should be str type    将txt文件中的特定label改为指定值after
    file_names = os.listdir(filepath)  # name lists of all txt files
    # checkLegalName(fixed_name, file_names)
    print(file_names)
    for name in file_names:                  # go through every file
        # print(name)
        file = os.path.join(filepath, name)
        with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
            for line in f1:
                a = line.split(' ')
                if a[0] == before:
                    a[0] = after
                f2.write(' '.join(a))
        os.remove(file)
        os.rename("%s.bak" % file, file)

# 下面两个函数想要使用的话，需要修改
def delete_label(delete):               # delete is a list containing the labels wants to delete
    for name in fileNames:                  # go through every file
        print(name)
        file = os.path.join(filePath, name)
        with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
            for line in f1:
                a = line.split(' ')
                if a[0] not in delete:
                    f2.write(' '.join(a))
        os.remove(file)
        os.rename("%s.bak" % file, file)


def keep_label(keep):               # keep is a list containing the labels wants to keep
    for name in fileNames:                  # go through every file
        print(name)
        file = os.path.join(filePath, name)
        with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
            for line in f1:
                a = line.split(' ')
                if a[0] in keep:
                    f2.write(' '.join(a))
        os.remove(file)
        os.rename("%s.bak" % file, file)



