import csv

points = 0

with open('Задание.csv', newline='') as zxcvb:
  reader = csv.reader(zxcvb, delimiter=';')
  for row in reader:
    print(row[0])
    print(row[1], row[2], row[3])
    i = input("Выберите вариант ответа(a, b, c): ")

    if i == 'a':
      if row[1] == row[4]:
        print("Правильно!")
        points += 5
      else:
        print("Неправильно!")
    elif i == 'b':
      if row[2] == row[4]:
        print("Правильно!")
        points += 5
      else:
        print("Неправильно!")
    elif i == 'c':
      if row[3] == row[4]:
        print("Правильно!")
        points += 5
      else:
        print("Неправильно!")
    else:
      print("не существует!")

if points == 100:
  print("Ваша оценка: A")
elif points >= 95:
  print("Ваша оценка: A-")
elif points >= 90:
  print("Ваша оценка: B+")
elif points >= 85:
  print("Ваша оценка: B")
elif points >= 80:
  print("Ваша оценка: B-")
elif points >= 75:
  print("Ваша оценка: C+")
elif points >= 70:
  print("Ваша оценка: C")
elif points >= 65:
  print("Ваша оценка: C-")
elif points >= 60:
  print("Ваша оценка: D")
else:
  print("Ваша оценка: F")