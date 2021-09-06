# coding=utf-8

import time

if __name__ == "__main__":
    begin_time = time.time()
    file_name = "save-202108"
    file = open(file_name + ".txt")
    temp = ""
    for line in file:
        li = line.split("|")
        if str(li[2]).__contains__("2"):
            li[2] = "'" + li[2]
        if str(li[3]).__contains__("2"):
            li[3] = "'" + li[3]
        if str(li[4]).__contains__("2"):
            li[4] = "'" + li[4]
        if str(li[5]).__contains__("2"):
            li[5] = "'" + li[5]
        s = ",".join(li)
        temp = temp + s
    f = open("./files/" + file_name + ".csv", 'w')
    f.write(temp)
    f.close()
    end_time = time.time()
    print("耗时： {}(秒)".format(round(end_time - begin_time, 2)))
