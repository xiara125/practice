seven = []
for i in range(9):
    seven.append(int(input()))

total_high = sum(seven)

for i, num1 in enumerate(seven):
    for j, num2 in enumerate(seven):
        if i != j and num1+num2 == total_high - 100 and len(seven)>7:
            seven.remove(num1)
            seven.remove(num2)
            break
    if len(seven) == 7:
        break
print(*sorted(seven))