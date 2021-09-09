class Hw1Q2:
    def monoSolve(self):
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        c = int(input('Enter c:'))
        x = (c + (2*b))/a
        return x
    def polySolve(self):
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        c = int(input('Enter c:'))
        x = ((c*c)-(2*b))/a
        return x
if __name__ == "__main__":
    test = Hw1Q2()
    print(test.monoSolve())
    print(test.polySolve())

