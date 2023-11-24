score = 0   #We need to track the score, so we'll declare an empty board here.

with open('Day 2/rpsdata.txt', 'r') as cal: 
    for line in cal.readlines():
        enemy_move, my_move = line.split()      #this will divide the input lines into two separate values, one for the enemy move, one for mine.

        #Now we proceed to code the setup of the list. First the enemy's moves.

        if enemy_move == 'A':
            e_move = 'rock'
        elif enemy_move == 'B':
            e_move = 'paper'
        elif enemy_move == 'C':
            e_move = 'scissors'

        #Then mine's

        if my_move == 'X':
            m_move = 'rock'
        elif my_move == 'Y':
            m_move = 'paper'
        elif my_move == 'Z':
            m_move = 'scissors'

        #Now we proceed to code the rules of the match. Only the instances when you earn score, cause we don't care about the 0.

        if e_move == m_move:
            score += 3
        elif e_move == 'rock' and m_move == 'paper':
            score += 6
        elif e_move == 'paper' and m_move == 'scissors':
            score += 6
        elif e_move == 'scissors' and m_move == 'rock':
            score += 6

        #And now the flat scores.

        if m_move == 'rock':
            score += 1
        elif m_move == 'paper':
            score += 2
        elif m_move == 'scissors':
            score += 3

print(score)
