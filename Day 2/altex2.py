#"Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

score = 0   #We need to track the score, so we'll declare an empty board here.

with open('Day 2/rpsdata.txt', 'r') as cal: 
    for line in cal.readlines():
        enemy_move, my_move = line.split()          

        if enemy_move == 'A':
            e_move = 'rock'
        elif enemy_move == 'B':
            e_move = 'paper'
        elif enemy_move == 'C':
            e_move = 'scissors'

    #Now we have to set the new rule given. Here: X = Lose, Y = Draw, Z = Win

        if my_move == 'X':
            if e_move == 'rock':
                m_move = 'scissors'
            if e_move == 'scissors':
                m_move = 'paper'
            if e_move == 'paper':
                m_move = 'rock'
        elif my_move == 'Y':
            m_move = e_move
        elif my_move == 'Z':
            if e_move == 'rock':
                m_move = 'paper'
            if e_move == 'scissors':
                m_move = 'rock'
            if e_move == 'paper':
                m_move = 'scissors'

        if e_move == m_move:
            score += 3
        elif e_move == 'rock' and m_move == 'paper':
            score += 6
        elif e_move == 'paper' and m_move == 'scissors':
            score += 6
        elif e_move == 'scissors' and m_move == 'rock':
            score += 6


        if m_move == 'rock':
            score += 1
        elif m_move == 'paper':
            score += 2
        elif m_move == 'scissors':
            score += 3

    print(f"True {score}")