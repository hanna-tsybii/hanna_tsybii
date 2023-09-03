num = int(input("Введіть число: "))

print("| num | num ^ 2 | num ^ 3 |")
print("|-----|---------|---------|")

for i in range(1, num):
    square = i ** 2
    cube = i ** 3
    print("| {:<4} | {:<7} | {:<7} |".format(i, square, cube))
