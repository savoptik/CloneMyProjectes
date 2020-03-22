import os
import ConsoleCommandes as cc

print(os.uname())

with open("Repolinc") as file:
    arry = [row.strip() for  row in file]

def install(path):
    cc.cdDirIn(path)
    if os.path.exists(os.getcwd() + '.gitmodules'):
        cc.gitSubmodule()
    if os.path.exists(os.getcwd() + "Podfile"):
        cc.podInstall()
    cc.cdDirOut()

for row in arry:
    dirName = row[row.rfind("/"):-4]
    print(dirName)
    if os.path.exists(os.getcwd() + dirName):
        print("папка найдена")
        install(dirName)
    else:
        print("папка не найдена")
        print("Клонирую")
        cc.gitClone(row)
        install(dirName)