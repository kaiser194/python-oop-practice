class Computation:
    def __init__(self):
        pass

    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def naturalSum(self, n):
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    def testPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def testPrims(self, a, b):
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return False
        return True

    def tableMult(self, n):
        for i in range(1, 11):
            print(n, "*", i, "=", n * i)

    def allTablesMult(self):
        for i in range(1, 10):
            self.tableMult(i)
            print()

    @staticmethod
    def listDiv(n):
        Ldiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                Ldiv.append(i)
        return Ldiv

    @staticmethod
    def listDivPrim(n):
        prime_divs = []

        for d in Computation.listDiv(n):
            if d <= 1:
                continue

            is_prime = True
            for i in range(2, int(d**0.5) + 1):
                if d % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_divs.append(d)

        return prime_divs
        
obj = Computation()

print("Factorial of 5:", obj.factorial(5))
print("Natural sum till 10:", obj.naturalSum(10))

print("Is 7 prime?", obj.testPrime(7))
print("Is 9 prime?", obj.testPrime(9))

print("Are 4 and 9 coprime?", obj.testPrims(4, 9))
print("Are 6 and 9 coprime?", obj.testPrims(6, 9))

print("\nMultiplication table of 5:")
obj.tableMult(5)

print("\nAll tables from 1 to 9:")
obj.allTablesMult()

print("Divisors of 12:", Computation.listDiv(12))
print("Prime divisors of 12:", Computation.listDivPrim(12))
