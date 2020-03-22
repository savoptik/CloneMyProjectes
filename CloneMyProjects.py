import os
print(os.uname())
print("привет мир")
with open("Repolinc") as file:
    arry = [row.strip() for  row in file]
    print(arry)