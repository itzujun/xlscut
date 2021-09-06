# coding=utf-8

if __name__ == "__main__":
    file_name = "save-202108"
    file = open(file_name + ".txt")
    temp = ""
    for line in file:
        line = line.replace("|", ",")
        temp = temp + line
    f = open("./files/" + file_name + ".csv", 'w')
    f.write(temp)
    f.close()
