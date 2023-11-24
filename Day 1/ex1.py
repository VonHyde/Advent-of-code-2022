#Set an empty list to put results, also a counter to do the sum

elves=[]
temp=0

#Use the with open command to read the data, the 'r' is for the mode.

with open('/workspace/Advent-of-code-2022/Day 1/elfdata.txt', 'r') as cal: 
    for line in cal.readlines():    #readlines returns a list containing each line as a list item
        if not line.strip():
            elves.append(temp)
            temp = 0                #So, this will count every single item and sum it to temp, if it founds an empty space (not line.strip()) it'll reset temp to 0, put the result in [elves] and continue.
            continue
        x = int(line)
        temp += x

#Now the list must have the sum of calories of every elf. Just need to print the max value.

print(max(elves))

#To get the Top 3, we must sort the list in descending order (reverse), then print the sum of the top 3.

elves.sort(reverse=True)

print(sum(elves[:3]))
