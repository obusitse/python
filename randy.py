from os import system, name

def clear():
    if(name == 'nt'):
        _ = system('cls')

clear()

print('welcome to retro...\n')
answer = input('would you like to play a game?')

if(answer == 'Y'):
    print('Great, i know what we can play..')
    

elif(answer == 'N'):
    print("that's just too bad, maybe next time")