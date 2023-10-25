num = input("Введите натуральное число: ")
sum = 0

for i in num:
  i = int(i)
  if i % 2 == 1:
    n = i ** 2
  else:
    continue
  sum = sum + n
  
print(sum)