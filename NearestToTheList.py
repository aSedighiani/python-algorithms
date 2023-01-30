l = [1,6,8,12,15,36,38]
num = int(input("enter a num: "))
a = min(l) + abs(num) + 1
closest_num = -1
for i in l:
    if abs(i - num) < a:
        a = abs(i - num)
        closest_num = i
print(closest_num)