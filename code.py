import colors as c
class Code():
    def __init__(self, code = [1,1,1,1]):
        self.code = code

    def guess(self, guess):
        g = guess.copy()
        code = self.code.copy()
        for (i, n) in enumerate(g):
            if code[i] == n:
                g[i] = 'b'
                code[i] = 'taken'
        for (i, n) in enumerate(g):
            if n in code:
                g[i] = 'w'
                code[code.index(n)] = 'taken'
        print( f'Your guess of {guess} returned {g.count("b")} Black Pegs and {g.count("w")} White Pegs\n')

        return (g == ['b']*4)
