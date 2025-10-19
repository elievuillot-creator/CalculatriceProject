class CALC():     # il va suffir ensuite de lacher des avec préalablement CALC = CALC() CALC.addition(a,b) pour avoir les résultats
    def __init__(self):
        None
    def addition(self,a,b):
        return a+b
    def soustraction(self,a,b):
       return a-b
    def multiplication(self,a,b):
        n = float(a)
        if a == 0 or b == 0 :
            return 0
        else :
            for i in range(int(b)-1):
                n = n + float(a)
            return n

    def divisionEUC(self,a,b):
        n = int(a)
        PartInt = 0
        while n > 0:
            PartInt = PartInt +1
            n-=int(b)
        reste = int(a) - self.multiplication(b,PartInt)
        if not reste == 0 :
            PartInt = PartInt - 1
        return PartInt, abs(reste)

    def division(self, a, b):
        q, n = self.divisionEUC(a,b)
        while (self.multiplication(q,b)-a) < 0:
            q = q + 0.01
        return q

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
            result = self.multiplication(result, a)
        return (result)

    def factoriel(self, n):
        a = 1
        for i in range(1,n+1):
            a = self.multiplication(a, i)
        return a

    def exp(self, a):
        b = 1
        for n in range(1, 10):
            b = b + self.division(self.puissance(a, n),self.factoriel(n))
        return b

    def premier(self,a):
        for i in range(2, int(a)):
            x, y = self.division(a,i)
            if y == 0:
                print("Pas premier")
                break
        print("premier")

CALC = CALC()
print(CALC.exp(10))
