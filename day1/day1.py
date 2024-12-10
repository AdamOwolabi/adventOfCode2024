list1 = []
left = []
right = []

file_path = open("day1.txt", "r")
line = file_path.readline()


while line:
    print(line)
    line = line.split()
    left.append(line[0])
    right.append(line[1])
    line = file_path.readline()

distance = 0

# left = sorted(left)
# right = sorted(right)

for i in range(len(left)):
    count = right.count(left[i])
    distance +=  int(left[i]) * count

        
print(distance)
   
#3569916




# Loop through the rest of the file and print each line

