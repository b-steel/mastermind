import random

class Computer():
    def __init__(self):
        self.first_guess = True
        self.possibilities = self.create_posibilities()
        self.remaining = self.possibilities.copy()

    def create_posibilities(self):
        s = []
        for a in range(1,10):
            for b in range(1,10):
                for c in range(1,10):
                    for d in range(1,10):
                        s.append([a,b,c,d])
        return s

    def guess(self):
        if self.first_guess:
            self.first_guess = False
            return [1,1,2,2]
        else: 
            return random.choice(self.remaining)
           

    def calculate_response(self, c, g):
        b,w = 0,0
        code = c.copy()
        guess = g.copy()
        for (i, n) in enumerate(guess):
            if code[i] == n:
                b+=1
                code[i] = 'x'
                guess[i] = 'y'
        for n in guess:
            if n in code:
                w +=1
                code[code.index(n)] = 'x'
                guess[guess.index(n)] = 'y'
        
        return [b,w]



    def learn(self, guess, b, w):
        filtered = list(filter(lambda code: True if self.calculate_response(code, guess) == [b,w] else False , self.remaining))
        self.remaining = filtered
        del self.possibilities[self.possibilities.index(guess)]


# c = Computer()
# print(c.calculate_response([1,2,3,4], [2,4,3,1]))

        


    

