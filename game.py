import strategy, random, secretcode, computer

import colors as c
class Game():
    def __init__(self, mode=1):
        self._mode = mode
        self._round = 0
        self._code = []
        self._maxrounds = 10
        self._computer = computer.Computer()

    def get_code(self):
        entered = False
        while not entered:
            p_code = list(input('Enter a 4 digit code (no zero\'s!) without spaces\n'))
            if len(p_code) != 4:
                print(f'{c.bcolors.WARNING}HMM... That wasn\'t a valid code, please try again...{c.bcolors.ENDC}')
            else:
                entered = True
        return [int(item) for item in p_code]

    def get_guess(self):
        entered = False
        while not entered:
            guess = list(input('Enter your 4 digit guess without spaces\n'))
            if len(guess) != 4:
                print(f'{c.bcolors.WARNING}HMM... That wasn\'t a valid guess, please try again...{c.bcolors.ENDC}')
            else:
                entered = True
        return [int(item) for item in guess]

    def create_code(self):
        return [random.randint(1,9) for _ in range(4)]

    def play(self):
        if self._mode == 1:
           return self.play_as_guesser()
        elif self._mode == 2:
            return self.play_as_codemaster()
        
    def play_as_codemaster(self):
        print(f'{c.bcolors.HEADER}\n\t\t\t===========================\n\t\t\t---WELCOME TO MASTERMIND--- \n\t\t\t===========================\n{c.bcolors.ENDC}\n \nRules: A Black Peg represents a {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} number in the {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} spot.\n       A White Peg represents a {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} number in the {c.bcolors.FAIL}incorrect{c.bcolors.ENDC} spot.\n \nExample: your code is [1 2 3 4] and your opponent guesses [1 4 5 5].  You return one Black Peg (for the 1 in the correct spot) and one White Peg (for the 4 that is correct, but in the wrong spot)\n {c.bcolors.OKGREEN} GOOD LUCK!{c.bcolors.ENDC}')
            
        self._code = secretcode.Code(self.get_code())
        game_over = False
        while not game_over:
            self._round += 1
            comp_guess = self._computer.guess()
            print(f'Round {self._round} of {self._maxrounds}')
            print(f'The computer guessed {comp_guess}\nYour code is {self._code.code}')
            black_pegs= int(input(f'How many {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} numbers in the {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} positions are there?\n'))
            white_pegs = int(input(f'How many {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} numbers in the {c.bcolors.FAIL}incorrect{c.bcolors.ENDC} positions are there?\n'))
            self._computer.learn(comp_guess, black_pegs, white_pegs)
            if black_pegs == 4:
                game_over = True
                print(f'{c.bcolors.HEADER}\t\t\t---YOU LOSE--- {c.bcolors.ENDC}\nAww Shucks, the computer guessed your secret code!')
            if self._round >= self._maxrounds:
                print(f'{c.bcolors.HEADER}\t\t\t---YOU WIN--- {c.bcolors.ENDC}\nThe computer reached the maximum number of rounds ({self._maxrounds}) without solving the code! You\'re a Code MASTER')
                game_over = True
             
        return game_over




    def play_as_guesser(self):
        print(f'{c.bcolors.HEADER}\n\t\t\t===========================\n\t\t\t---WELCOME TO MASTERMIND--- \n\t\t\t===========================\n{c.bcolors.ENDC}\n \nRules: A Black Peg represents a {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} number in the {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} spot.\n       A White Peg represents a {c.bcolors.OKGREEN}correct{c.bcolors.ENDC} number in the {c.bcolors.FAIL}incorrect{c.bcolors.ENDC} spot.\n \nExample: the code is [1 2 3 4] and you guess [1 4 5 5].  You recieve one Black Peg (for the 1 in the correct spot) and one White Peg (for the 4 that is correct, but in the wrong spot)\n {c.bcolors.OKGREEN} GOOD LUCK!{c.bcolors.ENDC}')

        self._code = secretcode.Code(self.create_code())
       
        game_over = False
        while not game_over:
            print(f'Round {self._round} of {self._maxrounds}')
            self._round += 1
            game_over = self._code.guess(self.get_guess())
            if self._round >= self._maxrounds:
                print(f'{c.bcolors.HEADER}\t\t\t---GAME OVER--- {c.bcolors.ENDC}\n You reached the maximum number of rounds ({self._maxrounds}) without solving the code. Better luck next time!')
                print(f'The secret code was {c.bcolors.HEADER}{self._code.code}{c.bcolors.ENDC}')
                break
        return True
        