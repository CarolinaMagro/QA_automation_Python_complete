import random
import os


dirlist=os.listdir(".")
finaldirlist=[]
for files in dirlist:
    if(files[-3:]=="csv"):
        finaldirlist.append(files)
        

for filename in finaldirlist:
    f = open(filename, "r")

    lines=f.readlines()
    makefinal=""

    makefinal=makefinal+lines[0]

    for i in range(1,len(lines)):
        # print(lines[i])
        row=(lines[i]).strip().split(",")
        print(row[0])
        apporvedornot=""
        num1 = random.randint(1, 2)
        if num1==1:
            apporvedornot="approved"
        else:
            apporvedornot="rejected"
        makefinal=makefinal+row[0]+","+apporvedornot+"\n"



    text_file = open(filename, "w+")
    n = text_file.write(makefinal)



# f = open("demofile.txt", "r")
# print(f.read()) 



# print(num1)