'''
MAGICKÉ METODY, STATICKÉ METODY, DEKORÁTORY, VEKTOR

MAGICKÉ METODY
- volají se pouze jako metoda např. print(human)
- MAJÍ JASNĚ DANÉ, CO MAJJÍ MÍT ZA (SELF, ..) - NEMUZEME TAM NIC DÁVAT KROM TOHO, CO TAM MÁ BÝT
- např. method any
- metoda __new__ - vytváří nový atribut
- metoda __add__ - sčítáme, podporují operátor plus
- metoda __eq__ - porovnává dva objekty, equal
- metoda __str__ - vrací řetězec, reprezentaci, když voláme print
- metoda __repr__ - podobně jako str, používá ale spíš někdo, kdo převezme kod po nás
- metode __getitem__ - vytváří se ke změně iterovatelného objektu
- metoda __setitem__ - přepisuje objekty na libovolnéom indexu
- metoda __len__ - magická metoda, funguje i mimo string, zkrátka pro jakýkoli objekt
- metoda __hash__ - 

STATICKÉ METODY
- je i c++ a jiných, je to v jazycích založených na classach
- obecně to je metoda, která nepotřebuje využívat stav objektu
- self v metodě je tedy zbyzečný
- píše se jako @staticmethod
- decorator tridy je @classmethod

VECTOR
- help.vector - automaticky vygeneruje dokumentaci
- 
DEKORÁTOR
- metoda __dict__ - vypíše nám všehcny atribut, píše se za atribut. např. vector.__dict__
- property, setter
'''

# Task 1

class human:
    counter = 0
    # Jak dostat počet objektů v instanci - counter = 0 a pak ho dáme do init, kde jsou všechny instance
    def __init__(self, fn, bdate, cn, city, country, add):
        self.fn = fn
        self.bdate = bdate
        self.cn = cn
        self.city = city
        self.country = country
        self.add = add
        counter += 1
    
    def __repr__(self):
        return f"{self.fn}'s bday is {self.bdate}"
    
    def __str__(self, fn, city, country):
        print(f"{fn} live in {city} which is in {country}.")




# class sailor(human):
#     print("hello")
# class builder(human):
#     print("hello")
# class pilot(human):
#     print("hello")

# Task 2

from abc import ABC, abstractmethod

class shape:
    @abstractmethod
    def getArea(self):
        pass
    
class Square(shape):
    ...
class Triangle(shape):
    ...
class Rectangle(shape):
    ...



# class calculate:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def triangle(self):
#         x = self.a * self.b
#         return x
    
# Task 3

class args:
    @staticmethod
    def largest(a,b,c,d):
        x = [a,b,c,d]
        return max(x)
    @staticmethod
    def smallest(a,b,c,d):
        x = [a,b,c,d]
        return min(x)
    @staticmethod
    def average(a,b,c,d):
        x = [(a + b + c + d) / 4]
        return x
    @staticmethod
    def factorial(a,b,c,d):
        x = {a,b,c,d}
        for item in x:
            fact = 1
            for i in range(1, item+1):
                fact = fact * i
            print(f"Factorial of {item} is {fact}.") # POZOR! RETURN rovnou cutuje a vrací jen jeden řádek PRINT nám vyjede všechny řádky

result = args.average(1,4,20,8)
print(result)

result_1 = args.factorial(1,2,3,4)
print(result_1)