x_нач = int(input("Введите x_нач: "))
x_кон = int(input("Введите x_кон: "))
dx = int(input("Введите dx: "))

print("Лабораторная работа №3\nТема: Использование циклов и условий\nВариант 5")
for i in range(x_нач, x_кон, dx):
  if i < 0:
    y = -0.5 * i - 3
  elif 0 <= i <= 3:
    y = -((9-i*i)**0.5)
  elif 3 < i <= 6:
     y=-((9-(i-6)**2)**0.5)
  print(i, " ", y)