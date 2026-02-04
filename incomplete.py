
class Computation :
    def __init__(self):
        pass
    def Factorial(self,n):
        fact = 1
        for i in range(n,0,-1):
            fact*=i
        
        return fact
    def naturalSum(self,n):
        sum=0
        for i in range(1,n+1):
            sum+=i
            
        return sum
    def testPrime(self,n):
        if n <= 1:
         return False
        for i in range(2,int(n**0.5)+1):
            if n%i ==0:
                return False
        return True
    def testPrims(self,a,b):
        for i in range(2,min(a,b)+1):
            if a%i==0 and b%i==0:
                return False
            return True
    def tableMult():
        pass
    @staticmethod
    def listDiv(n):
        pass
    
obj = Computation()
print(obj.testPrime(12))
