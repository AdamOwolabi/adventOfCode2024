#[2, 3, 5, 0]
#

def discardWild(line, increment):
    for i in range(0, len(line)):
        dif = abs(line[i-1] - line[i])
        if(dif != 1 and dif != 2 and dif != 3):
            dif1 = line[i] + increment
            if((line[i] + dif1) in line):
                line[i] = line[i] + increment
                return True
            elif(line[i] - dif1 in line):
                line[i] = line[i] - increment
                return True
    return False
           

file_path = open("day2.txt", "r")

line = file_path.readline()

levels = []
safe = 0
dif = 0
check = True

while line:
    line = line.strip()
    line = line.split(" ")

    for i in range(0,len(line)):
        line[i] = int(line[i])

     
    if sorted(line) != line or sorted(line, reverse=True) != line:
        discardWild(line, increment)
        

    
    if sorted(line) == line or sorted(line, reverse=True) == line:
        for i in range(1,len(line)):
            
            dif = abs(line[i-1] - line[i])
            
            if(dif != 1 and dif != 2 and dif != 3):
                check = False
                break
            else:
                print(line)
                print(line[i-1], line[i])
                print(dif)
                check = True
        if check:
            print(sorted(line), line)
            safe += 1

    line = file_path.readline()
            


print(safe)
