
n = 10
m = 3

a = 0
b = 0

for x in list(range(1,n+1)):
    if x % m != 0:
        num1 = a + x
        a = num1

    else:
       num2 = b + x
       b = num2

print(f'{num1-num2}')
