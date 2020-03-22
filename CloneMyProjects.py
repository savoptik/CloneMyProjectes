import os
print(os.uname())

with open("Repolinc") as file:
    arry = [row.strip() for  row in file]
for row in  arry:
    dirName = row[row.rfind("/"):-4]
    print(dirName)
    if os.path.exists("/users/artemsemenov/projects/myprojects/" + dirName):
        print("папка найдена")
    else:
        print("папка не найдена")