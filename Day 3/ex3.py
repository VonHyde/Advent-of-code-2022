priotiries = 0 #Again, we have to give a number for result, so we have to keep score.

with open('/workspace/Advent-of-code-2022/Day 3/rackdata.txt', 'r') as cal: 
    for line in cal.readlines():
        l = line.strip()  #Strip it to make sure spaces won't bother.
        m = len(l)//2     #Lenght of each pocket.
        first = set(l[:m])
        second = set(l[m:])  #This two says to which pocket will go each half.
        common = list(first.intersection(second))[0] #So, we make i a list so we could ake just the first value in each iteration, we use the 'intersection' function to get the common values.
        x = ord(common) - 96   #The Unicode value of "a" is 97, so we have to add this to make it 1
        if x <= 0:
            x += 58            #If the result of X is a negative, it's cause is a Uppercase letter, so we add 56 to fix the priority set in the excersise.
        priotiries += x

print(priotiries)            