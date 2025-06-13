n = (input("add : "))
l = []
while True :
    for i in n :
        i = int(i)
        l.append(i)
    sum_of_digit = sum (l)
    if sum_of_digit >= 10 :
        n = sum_of_digit
        n = str(n)
        l.clear()
    else :
        break

print(sum_of_digit)