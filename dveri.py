#task 1
temperature = float(input("Введіть температуру (°C): "))
humidity = float(input("Введіть відносну вологість (%): "))

if temperature > 30 and humidity > 70:
    print("Активація системи охолодження")
else:
print("Умови нормальні")

#task 2

number = int(input("Введіть число: "))
if 1 <= number <= 100:
    print("Число знаходиться в допустимому діапазоні")
else:
print("Помилковий ввід")

#task 3

age = int(input("Введіть вік кандидата: "))
experience = int(input("Введіть кількість років досвіду: "))
qualification = input("Чи має кандидат спеціальну кваліфікацію? (True/False): ").lower() == "true"

if 25 <= age <= 50 and (experience >= 3 or qualification):
    print("Кандидат відповідає вимогам")
else:
print("Кандидат не відповідає вимогам")
