from random import randint
import random
import sys
import os

clear = lambda: os.system("cls")
pause = lambda: os.system("pause")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "'!@#$%¨&*()-=+_|/?~[}]{^.,;><"
numbers = "0123456789"

def justLetters(length):
	print("\t Just letters\n")
	print(" 1 - Lower case")
	print(" 2 - Upper case")
	print(" 3 - Both")
	print(" 4 - Return to menu\n")
	op = int(input(" Option: "))
	pwd = ""

	if op == 1:
		pos = lower
	elif op == 2:
		pos = upper
	elif op == 3:
		pos = lower + upper
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 4:
		clear()
		return False

	for i in range(0,length):
		rand = randint(0, len(pos)-1)
		pwd += pos[rand]

	clear()
	print("\t Your Password:\n")
	print(" " + pwd + "\n\n")
	print(" 1 - Generate another password")
	print(" 2 - Return to menu")
	print(" 3 - Exit\n")
	op2 = int(input(" Option: "))
	if op2 == 1:
		clear()
		justLetters(length)
	elif op2 == 2:
		clear()
		return False
	elif op2 == 3:
		sys.exit()

def justNumbers(length):
	print("\t Just numbers\n")
	pos = numbers
	pwd = ""
	for i in range(0,length):
		rand = randint(0, len(pos)-1)
		pwd += pos[rand]

	clear()
	print("\t Your Password:\n")
	print(" " + pwd + "\n\n")
	pause()
	clear()

def justSymbols(length):
	print("\t Just symbols")
	pos = symbols
	pwd = ""
	for i in range(0,length):
		rand = randint(0, len(pos)-1)
		pwd += pos[rand]

	clear()
	print("\t Your Password:\n")
	print(" " + pwd + "\n\n")
	print(" 1 - Generate another password")
	print(" 2 - Return to menu")
	print(" 3 - Exit\n")
	op2 = int(input(" Option: "))
	if op2 == 1:
		clear()
		justSymbols(length)
	elif op2 == 2:
		clear()
		return False
	elif op2 == 3:
		sys.exit()

def NumbersLetters(length):
	print("\t Numbers and letters\n")
	print(" Select types of letters:\n")
	print(" 1 - Lower case")
	print(" 2 - Upper case")
	print(" 3 - Both")
	print(" 4 - Return to menu\n")
	op = int(input(" Option: "))
	pwd = ""

	if op == 1:
		pos = lower + numbers
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 2:
		pos = upper + numbers
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 3:
		pos = lower + upper + numbers
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 4:
		clear()
		return False

	for i in range(0,length):
		rand = randint(0, len(pos)-1)
		pwd += pos[rand]

	clear()
	print("\t Your Password:\n")
	print(" " + pwd + "\n\n")
	print(" 1 - Generate another password")
	print(" 2 - Return to menu")
	print(" 3 - Exit\n")
	op2 = int(input(" Option: "))
	if op2 == 1:
		clear()
		NumbersLetters(length)
	elif op2 == 2:
		clear()
		return False
	elif op2 == 3:
		sys.exit()

def numbersSymbols(length):
	print("\t Numbers and symbols\n")
	pwd = ""
	pos = numbers + symbols
	l = list(pos)
	random.shuffle(l)
	pos = ''.join(l)

	for i in range(0,length):
		rand = randint(0, len(pos)-1)
		pwd += pos[rand]

	clear()
	print("\t Your Password:\n")
	print(" " + pwd + "\n\n")
	print(" 1 - Generate another password")
	print(" 2 - Return to menu")
	print(" 3 - Exit\n")
	op2 = int(input(" Option: "))
	if op2 == 1:
		clear()
		numbersSymbols(length)
	elif op2 == 2:
		clear()
		return False
	elif op2 == 3:
		sys.exit()

def lettersSymbols(length):
	print("\t Letters and symbols\n")
	print(" Select types of letters:\n")
	print(" 1 - Lower case")
	print(" 2 - Upper case")
	print(" 3 - Both")
	print(" 4 - Return to menu\n")
	op = int(input(" Option: "))
	pwd = ""

	if op == 1:
		pos = lower + symbols
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 2:
		pos = upper + symbols
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 3:
		pos = lower + upper + symbols
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 4:
		clear()
		return False

	for i in range(0,length):
		rand = randint(0, len(pos)-1)
		pwd += pos[rand]

	clear()
	print("\t Your Password:\n")
	print(" " + pwd + "\n\n")
	print(" 1 - Generate another password")
	print(" 2 - Return to menu")
	print(" 3 - Exit\n")
	op2 = int(input(" Option: "))
	if op2 == 1:
		clear()
		lettersSymbols(length)
	elif op2 == 2:
		clear()
		return False
	elif op2 == 3:
		sys.exit()

def all(length):
	print("\t All\n")
	print(" Select types of letters:\n")
	print(" 1 - Lower case")
	print(" 2 - Upper case")
	print(" 3 - Both")
	print(" 4 - Return to menu\n")
	op = int(input(" Option: "))
	pwd = ""

	if op == 1:
		pos = lower + symbols + numbers
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 2:
		pos = upper + symbols + numbers
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 3:
		pos = lower + upper + symbols + numbers
		l = list(pos)
		random.shuffle(l)
		pos = ''.join(l)
	elif op == 4:
		clear()
		return False

	for i in range(0,length):
		rand = randint(0, len(pos)-1)
		pwd += pos[rand]

	clear()
	print("\t Your Password:\n")
	print(" " + pwd + "\n\n")
	print(" 1 - Generate another password")
	print(" 2 - Return to menu")
	print(" 3 - Exit\n")
	op2 = int(input(" Option: "))
	if op2 == 1:
		clear()
		all(length)
	elif op2 == 2:
		clear()
		return False
	elif op2 == 3:
		sys.exit()

while (1):
	print("\t Password Generator 2.0 by Cripto S.a\n")
	print(" 1 - Generate Password")
	print(" 2 - Exit\n")
	op = int(input(" Option: "))
	if op == 1:
		clear()
		print("\t Generate Password\n")
		tam = int(input(" Length: "))
		print("\n 1 - Just letters")
		print(" 2 - Just numbers")
		print(' 3 - Just symbols')
		print(" 4 - Numbers and letters")
		print(" 5 - Numbers and symbols")
		print(" 6 - Letters and symbols")
		print(" 7 - All\n")
		op2 = int(input(" Option: "))
		if op2 == 1:
			clear()
			justLetters(tam)
		elif op2 == 2:
			clear()
			justNumbers(tam)
		elif op2 == 3:
			clear()
			justSymbols(tam)
		elif op2 == 4:
			clear()
			NumbersLetters(tam)
		elif op2 == 5:
			clear()
			numbersSymbols(tam)
		elif op2 == 6:
			clear()
			lettersSymbols(tam)
		elif op2 == 7:
			clear()
			all(tam)
	else:
		sys.exit()