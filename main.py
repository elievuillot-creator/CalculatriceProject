class CALC():     # il va suffir ensuite de lacher des avec préalablement CALC = CALC() CALC.addition(a,b) pour avoir les résultats
    def __init__(self):
        None
    def addition(self,a,b):
        try:
            if not float(a).is_integer() or not float(b).is_integer() or a < 0 or b < 0:
                raise ValueError
        except ValueError:
            return "Erreur : seul les opérations sur des nombres entiers sont autorisés !"
        return a+b
    def soustraction(self,a,b):
        try:
            if not float(a).is_integer() or not float(b).is_integer() or a < 0 or b < 0:
                raise ValueError
        except ValueError:
            return "Erreur : seul les opérations sur des nombres entiers sont autorisés !"
        return a-b

    def multiplication(self,a,b):
        try:
            if not float(b).is_integer() or a < 0 or b < 0:
                raise ValueError
        except ValueError:
            return "Erreur : seul les opérations sur des nombres entiers sont autorisés !"
        n = float(a)
        if a == 0 or b == 0 :
            return 0
        else :
            for i in range(int(b)-1):
                n = n + float(a)
            return n

    def multipicationFLOAT(self,a, b):
        a = float(a)
        b = float(b)
        a = round(a,3)
        b = round(b,3)
        a2 = round(self.multiplication(a, 1000))
        b2 = round(self.multiplication(b, 1000))
        result = self.multiplication(a2,b2)
        result = self.division(result,1000000)
        return result

    def divisionEUC(self,a,b):
        try:
            if not float(a).is_integer() or not float(b).is_integer() or a < 0 or b < 0 or b == 0:
                raise ValueError
        except ValueError:
            return "Erreur : seul les opérations sur des nombres entiers sont autorisés !"
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
        try :
            if not float(a).is_integer() or not float(b).is_integer() or a<0 or b<0 or b==0 :
                raise ValueError
        except ValueError:
            return "Erreur : seul les opérations sur des nombres entiers sont autorisés !"
        try : #0
            if b==0:
                raise ZeroDivisionError
        except:
            return " Erreur : division par 0"

        q, n = self.divisionEUC(a,b)
        while (self.multiplication(q,b)-a) < 0:
            q = q + 0.01
        return q

    def fibonacci(self,a):
        try :
            if not float(a).is_integer() or a<0:
                raise ValueError
        except ValueError :
            return "Erreur : seul les opérations sur des nombres entiers sont autorisés !"
        fn2 = 1
        fn1 = 0
        for i in range(a):
            result= fn1 + fn2
            fn2=fn1
            fn1=result
        return result

    def puissance(self,a, n):
        try :
            if not float(a).is_integer() or not float(n).is_integer() or a<0 or n<0:
                raise ValueError
            result = 1
            for i in range(int(n)):
               result = self.multipicationFLOAT(result, a)
            return result
        except ValueError :
            return "Erreur, seul les opérations sur des entiers naturels sont autoisés !"


    def factoriel(self, n):
        try :
            if not float(n).is_integer() or n<0:
                raise ValueError
            a = 1
            for i in range(1,n+1):
                a = self.multiplication(a, i)
            return a
        except ValueError :
            return "Erreur : seul les opérations sur des entiers naturels sont autorisés !"

    def premier(self,a):
        try :
          if not float(a).is_integer() or a<0:
              raise ValueError
          for i in range(2, int(a)):
             x, y = self.divisionEUC(a,i)
             if y == 0:
                 return "Pas premier"
          return "premier"
        except ValueError :
            return "Erreur : seul les opérations sur des entiers naturels sont autorisés !"

    def exp(self, x):   # approximation d'exp ( plus précise pour des nombre petits )
        e = 2.718  # valeur approximative
        try :
          if x < 0 or not float(x).is_integer():  # vérifier que le x est conforme
              raise ValueError
          if x == 0:
              return 1.0
          elif x > 0:
              result = 1.0
              for _ in range(int(x)):
                  result = self.multipicationFLOAT(result, e)   # on fait e puissance x
              return result
        except ValueError :
            return "Erreur, seul les opérations sur les entiers naturels sont autorisés !"

