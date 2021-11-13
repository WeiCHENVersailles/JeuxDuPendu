import random
from typing import Counter

def game():
    mots = ['rumsteck', 'edulcorant', 'veterinaire']
    mot = mots[random.randint(0, len(mots) - 1)]
    #print(mot)
    mot_copy = mot[0]
    i = len(mot) - 2
    while(i > 0):
        mot_copy = mot_copy + '_'
        i = i - 1
    mot_copy = mot_copy + mot[-1]
    print(mot_copy)
    vie = 5

    while(vie > 0):
        lettre = input('Entrer un lettre:')
        guess = mot.index(lettre)
        #print(guess)
        #if(guess):
            #mot_copy[guess] = lettre
            #print(mot_copy)

def correction_game():
    list_worlds_game = ['rumsteck', 'edulcorant', 'veterinaire']
    world_chosen = list_worlds_game[random.randint(0, len(list_worlds_game) - 1)]
    print(world_chosen)
    size_world_chosen = len(world_chosen)
    print(size_world_chosen)
    vie = 5
    replay = ''
    #for i in range(size_world_chosen):
        #print(i)
    guess_world = '_,' * size_world_chosen
    guess_world = guess_world.split(',')
    del(guess_world[-1])
    #print(guess_world)
    #print(world_chosen[0])
    guess_world[0] = world_chosen[0]
    guess_world[-1] = world_chosen[-1]
    #print(type(guess_world[0]), type(world_chosen[0]))
    #guess_world = guess_world.replace(guess_world[0], world_chosen[0], 1)
    #print(guess_world.replace(guess_world[0], world_chosen[0], 1))
    #guess_world = guess_world.replace(guess_world[-1], world_chosen[-1], 1)
    print(''.join(guess_world))

    while(True):
            
        letter = input('Entrer un lettre:')
        counter = 0
        if letter in world_chosen:
            for i in world_chosen:
                if i == letter:
                    guess_world[counter]= i
                counter += 1
            if ''.join(guess_world) == world_chosen:
                print('YOU WON!')
                break
        else:
            print(letter, 'is not in the world' )
            vie -= 1
            if vie <= 0 :
                print('YOU DIE')
                break
            else:
                print('you have ', vie, ' lifes')

        print(''.join(guess_world))
        #guess = world_chosen.index(letter)
        #print(guess)
        #for i in (guess):
            #guess_world[guess] = letter
            #print(guess_world)
        
    while  replay != 'YES' or replay != 'NO':      
        replay = input('Continue? YES/NO :')
        if replay == 'YES':
            correction_game()
        elif replay == 'NO':
            exit(1)




def main():
    #game()
    correction_game()

main()