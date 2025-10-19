class CALC():     # il va suffir ensuite de lacher des avec préalablement CALC = CALC() CALC.addition(a,b) pour avoir les résultats
    def __init__(self):
        None
    def addition(self,a,b):
        return a+b
    def soustraction(self,a,b):
       return a-b
    def multiplication(self,a,b):
        n=1
        for i in range(int(b)):
            n += a
    def division(self,a,b):
        n = int(a)
        PartInt = 0
        while n > 0:
            PartInt = PartInt +1
            n-=int(b)
        reste = int(a) - self.multiplication(b,PartInt)
        return PartInt, reste

    def fibonacci(self,a):
        fn2 = 1
        fn1 = 0
        for i in range(a):
            result= fn1 + fn2
            fn2=fn1
            fn1=result
        return result

    def puissance(self,a, n):
        result = 1
        for i in range(int(n)):
            result = self.multiplication(result,a)

    def exp(self, a):
        self.puissance(2.7, a)

    def premier(self,a):
        for i in range(2, int(a)):
            x, y = self.division(a,i)
            if y = 0:
                print("Pas premier")
                break
        print("premier")

CALC = CALC()
print(CALC.puissance(2,8))