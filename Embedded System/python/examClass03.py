class Calcul:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreCalcul(Calcul):
    def pow(self):
        result = self.first ** self.second
        return result

x = int(input("1st number : "))
y = int(input("2nd number : "))

a = MoreCalcul(x, y)


print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())
