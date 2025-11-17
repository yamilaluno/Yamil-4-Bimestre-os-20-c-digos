num = 17
eh_primo = True
for i in range(2, num):
    if num % i == 0:
        eh_primo = False
        break
print('Primo?', eh_primo)
