import math

class Complex:
    def __init__(self, re: float, im: float) -> None:
        self.re = re
        self.im = im


    def __str__(self) -> str:
        if self.im < 0:
            return f"{self.re} - {-self.im}i"
        elif  self.im == 0:
            return str(self.re)
        else:
            return f"{self.re} + {self.im}i"


    def __eq__(self, other: object) -> bool:
        return (self.re == other.re) and (self.im == other.im)

    
    def __add__(self, other: object) -> object:
        return Complex(self.re + other.re, self.im + other.im)

    
    def __sub__(self, other: object) -> object:
        return Complex(self.re - other.re, self.im - other.im)


    def __mul__(self, other: object) -> object:
        return Complex(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)


    def __truediv__(self, other: object) -> object:
        return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2), 
            (self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))


    def abs(self) -> float:
        return math.sqrt(self.re**2 + self.im**2)
