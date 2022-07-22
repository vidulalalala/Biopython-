#Rock, paper, scissors!

import random

def game():
    player = input("Let's play Rock, Paper and Scissors!\n Press 'r' for rock, 'p' for paper and 's' for scissors.\n")
    choose = random.choice(['r','p','s'])
    
    if choose == player:
        return("Damn, it's a tie!!!")
        
    if result(player, choose):
        return("You win!")
        
    return("Awh, sorry, you lost!")
        
def result(pla, cho):
    if (pla == 'r' and cho == 's') or (pla == 's' and cho == 'p') or (pla == 'p' and cho == 'r'):
        return True
        
print(game())   
    