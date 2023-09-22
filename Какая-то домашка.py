from random import *
number = randint(1,100)
print('Угадайте число от 1 до 100')
guess = int(input())
counter = 1
while guess != number:
	if guess > number:
		print('Слишком много ,попробуйте ещё!')
		guess = int(input())
		counter += 1
	elif guess < number:
		print('Слишком мало, попробуйте ещё!')
		guess = int(input())
		counter += 1
print('Вы угадали!' + 'Количество ваших попыток:' + str(counter))