def cal_def(i, k, p):
    if p == '+':
        print(i+k)
    elif p == '-':
        print(i-k)
    elif p == '*':
        print(i*k)
    elif p == '/':
        print(i/k)

x = int(input("input 1st number : "))
y = int(input("input 2nd number : "))
z = input("input arithmetic operator(+, -, *, /) : ")

cal_def(x, y, z)
