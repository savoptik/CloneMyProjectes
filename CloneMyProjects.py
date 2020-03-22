import os
import ConsoleCommandes as cc

print(os.uname())

with open("Repolinc") as file:
    arry = [row.strip() for  row in file]

def install(path):
    print("Установка зависимостей")
    os.chdir(os.getcwd() + path)
    if os.path.exists('./.gitmodules'):
        cc.gitSubmodule()
    if os.path.exists('./Podfile'):
        cc.podInstall()
    os.chdir('..')

for row in arry:
    dirName = row[row.rfind("/"):-4]
    if os.path.exists(os.getcwd() + dirName):
        print("папка" + dirName + "найдена")
        install(dirName)
    else:
        print("папка" + dirName + "не найдена")
        print("Клонирую")
        cc.gitClone(row)
        install(dirName)