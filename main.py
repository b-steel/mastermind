import game
import colors as c

finished = False
while True:
    if not finished:
        game_mode = input('Please Choose a Game-Mode: [1] Guess the Code, [2] Create the Code\n')
        if game_mode=='1':
            g = game.Game(mode=1)
            finished = g.play()
        elif game_mode == '2':
            g = game.Game(mode=2)
            finished = g.play()
        else:
            print(f'{c.bcolors.WARNING}HMM... That wasn\'t a valid number...{c.bcolors.ENDC}')
    else: 
        again = input(f'\n {c.bcolors.FAIL}Would you like to play again? Enter Y/N {c.bcolors.ENDC} \n')
        if again == 'Y' or again == 'y':
           finished = False
        elif again =='N' or again == 'n':
            break
print(f'{c.bcolors.HEADER}Thanks for playing, come back anytime! {c.bcolors.ENDC}')
