priotiries = 0 #Again, we have to give a number for result, so we have to keep score.

with open('/workspace/Advent-of-code-2022/Day 3/rackdata.txt', 'r') as cal:
    lines = cal.readlines()
    t = len(lines) // 3  # With this, we split the groups.

    for i in range (t):
        a, b, c = set(lines[3*i].strip()), set(lines[3*i+1].strip()), set(lines[3*i+2].strip()) #Designate each line as a variable.
        common = list(a & b & c)[0]
        x = ord(common) - 96   #The Unicode value of "a" is 97, so we have to add this to make it 1
        if x <= 0:
            x += 58            #If the result of X is a negative, it's cause is a Uppercase letter, so we add 56 to fix the priority set in the excersise.
        priotiries += x

print(priotiries)