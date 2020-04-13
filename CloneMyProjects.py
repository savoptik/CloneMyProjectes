import os
import ConsoleCommandes as cc

def install(path):
    print("Установка зависимостей")
    os.chdir(os.getcwd() + path)
    if os.path.exists('./.gitmodules'):
        cc.gitSubmodule()
    if os.path.exists('./Podfile'):
        cc.podInstall()
    os.chdir('..')

with open("Repolinc") as file:
    arry = [row.strip() for  row in file]

for row in arry:
    dirName = row[row.rfind("/"):-4]
    if os.path.exists(os.getcwd() + dirName):
        print("папка " + dirName[1:] + " найдена")
        install(dirName)
    else:
        print("Папка " + dirName[1:] + " не найдена")
        print("Клонирую")
        cc.gitClone(row)
        install(dirName)