class Racional:    
    def __init__(self, __numerador: int, __denominador: int) -> None:
        
        #validação para garantir que são primos entre si
        for i in range(min(__numerador, __denominador), 1, -1):
            if __numerador % i == 0 and __denominador % i == 0:
                __numerador //= i
                __denominador //= i
                break
            
        
        self.__numerador = __numerador
        self.__denominador = __denominador
    
    def __str__(self) -> str:
        return f"{self.__numerador}/{self.__denominador}"
    
    def razao(self) -> float:
        return self.__numerador / self.__denominador
    
    def sum(self, r1) -> "Racional":
        numerador = (r1.__numerador * self.__denominador) + (self.__numerador * r1.__denominador)
        denominador = self.__numerador * self.__denominador
        return Racional(numerador, denominador)
    
    def sub(self, r1) -> "Racional":
        numerador = (r1.__numerador * self.__denominador) - (self.__numerador * r1.__denominador)
        denominador = self.__numerador * self.__denominador
        return Racional(numerador, denominador)
    
    def mult(self, r1) -> "Racional":
        numerador = self.__numerador * r1.__numerador
        denominador = self.__denominador * r1.__denominador
        return Racional(numerador, denominador)
    

        