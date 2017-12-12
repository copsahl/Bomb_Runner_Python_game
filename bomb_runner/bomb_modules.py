import time, os, msvcrt

def module_one():
	'''Wires'''
	os.system('cls')
	wires_cut = 0
	wires = [
		['|','|','|','|','|'],
		['|','|','|','|','|'],
		['|','|','|','|','|'],
		['|','|','|','|','|'],
		['1','2','3','4','5']
	]
	def print_wires(array):
		for y in range(0,5):
			for x in range(0,5):
				print(array[y][x] + ' ', end = '')
			print()
	print_wires(wires)
	print("You must cut three wires in the correct order to pass!")
	print("HINT: ADD these three numbers from smallest to largest,")
	print("and they equal 8")
	while wires_cut < 3:
		if wires_cut == 0:
			wire = input("Cut wire: ")
			if wire == '1':
				print("correct")
				time.sleep(1)
				wires[2][0] = '*'
				wires_cut += 1
				os.system('cls')
				print_wires(wires)
			else:
				time.sleep(2)
				print("BOOM!")
				return False
		if wires_cut == 1:
			wire = input("Cut wire: ")
			if wire == '2':
				print("correct")
				time.sleep(1)
				wires[2][1] = '*'
				wires_cut += 1
				os.system('cls')
				print_wires(wires)
			else:
				time.sleep(1)
				print("BOOM!")
				return False
		if wires_cut == 2:
			wire = input("Cut wire: ")
			if wire == '5':
				time.sleep(2)
				print("correct")
				time.sleep(1)
				wires[2][4] = '*'
				wires_cut += 1
				os.system('cls')
				print_wires(wires)
			else:
				time.sleep(2)
				print("BOOM!")
				return False
		if wires_cut == 3:
			print("BOMB DEFUSED")
			time.sleep(2)
			return True

def module_two():
	'''NMAP MODULE'''
	os.system('cls')
	attempts = 1
	print("what port is closed?")
	time.sleep(3)
	os.system("cls")
	while attempts <= 3:
		nmap_cmd = input("root@kali:~# ")
		if nmap_cmd == 'nmap localhost' or nmap_cmd == 'nmap 127.0.0.1':
			print("PORT      STATE:  SERVICE")
			print("21/tcp    OPEN    ftp")
			print("23/tcp    OPEN    telnet")
			print("80/tcp    OPEN    http")
			print("420/tcp   CLOSED  abyss")
			print("1337/tcp  OPEN    hax.exe")
			print("3306/tcp  OPEN    mysql")
			print("\nType the port number then hit enter")
			while attempts <=3:
				kill_cmd = input("root@kali:~# ")
				if kill_cmd == '420':
					print("CORRECT")
					time.sleep(1)
					print("BOMB DEFUSED")
					time.sleep(1)
					return True
				else:
					print("Invalid input")
					time.sleep(1)
					attempts += 1
		else:
			print("Wrong Input!")
			time.sleep(1)
			attempts +=1
	print("BOOM")
	time.sleep(1)
	return False

def module_three():
	"""ALGEBRA PROBLEM"""
	print("Solve this quadratic using any method,")
	print("x^2 - 9x + 18 = 0")
	x1 = input("x = ")
	x2 = input("x = ")
	if x1 == '-6':
		if x2 == '-3':
			print("CORRECT")
			print("BOMB DEFUSED")
			time.sleep(1)
			return True
		else:
			return False
			
	if x1 == '-3':
		if x2 == '-6':
			print("CORRECT")
			print("BOMB DEFUSED")
			time.sleep(1)
			return True
		else:
			print("BOOM")
			time.sleep(1)
			return False
	
	if x1 != '-6' and x1 != '-3':
		print("BOOM")
		time.sleep(1)
		return False
		

def module_four():
	'''Song Lyric Guess'''
	# try to shorten with for loop
	os.system("cls")
	print("Complete the song by filling in the blanks:\n")
	print("Somebody once told me the _____ is gonna roll me,")
	print("I ain't the ________ tool in the shed.")
	print("She was looking kinda dumb with her _______ and her thumb")
	print("in the _____ of an L on her _________\n")
	w1 = input("Enter the word that goes in the 1st blank: ").lower()
	w2 = input("Enter the word that goes in the 2nd blank: ").lower()
	w3 = input("Enter the word that goes in the 3rd blank: ").lower()
	w4 = input("Enter the word that goes in the 4th blank: ").lower()
	w5 = input("Enter the word that goes in the 5th blank: ").lower()
	
	if w1 == 'world' and w2 == 'sharpest' and w3 == 'finger' and w4 == 'shape' and w5 == 'forehead':
		os.system("cls")
		print("YOU ARE CORRECT\nAll Star By Smashmouth\n")
		print("Somebody once told me the '{}' is gonna roll me,".format(w1))
		print("I ain't the '{}' tool in the shed.".format(w2))
		print("She was looking kinda dumb with her '{}' and her thumb".format(w3))
		print("in the '{}' of an L on her '{}'".format(w4,w5))
		time.sleep(2)
		print("BOMB DEFUSED")
		return True
	else:
		print("Incorrct")
		time.sleep(1)
		print("BOOM")
		time.sleep(1)
		return False
	
	
def module_five():
	'''What are the missing numbers in the fibonacci sequence'''
	os.system('cls')
	print("What are the missing numbers? ")
	print("0, 1, 1, 2, 3, 5, 8, __, 21, __, 55, __, 144,... ")
	
	num1 = input("Enter 1st num: ")
	num2 = input("Enter 2nd num: ")
	num3 = input("Enter 3rd num: ")
	
	if num1 == '13' and num2 == '34' and num3 == '89':
		print("Correct")
		print("BOMB DEFUSED")
		time.sleep(1)
		return True
	else:
		print("Incorrct")
		time.sleep(1)
		print("BOOM")
		time.sleep(1)
		return False
'''Start of Module 6'''
turns = 0
plyr_x = 0
plyr_y = 1
maze = [
		['+','+','+','+','+','+','+','+','+','+','+','+','+'],
		['S',' ',' ','+',' ',' ',' ',' ',' ',' ',' ',' ','+'],
		['+',' ',' ','+',' ','+','+','+',' ','+','+','+','+'],
		['+',' ',' ',' ',' ',' ','+','+',' ',' ',' ',' ','+'],
		['+',' ','+',' ','+',' ','+','+','+','+','+',' ','+'],
		['+',' ','+',' ','+',' ','+',' ',' ',' ','+',' ','+'],
		['+',' ','+',' ',' ',' ','+',' ','+',' ','+',' ','+'],
		['+',' ','+',' ','+','+',' ',' ','+',' ','+',' ','+'],
		['+',' ','+',' ','+','+','+','+','+',' ','+',' ','+'],
		['+',' ','+',' ',' ',' ',' ',' ',' ',' ','+',' ','E'],
		['+','+','+','+','+','+','+','+','+','+','+','+','+']
]

def module_six():
	
	def print_maze(arr):
		os.system("cls")
		print("Solve the maze in 24 steps!     Steps: {}".format(turns))
		for y in range(0 ,11):
			for x in range(0, 13):
				if x == plyr_x and y == plyr_y:
					print('P ', end = '')
				else:
					print(arr[y][x] + ' ', end = '')
			print()

	def move_player(arr):
		global plyr_x, plyr_y, turns
		direction = msvcrt.getwch()
		if direction == 'W' or direction == 'w':
			if arr[plyr_y - 1][plyr_x] != '+':
				plyr_y -= 1

		elif direction == 'S' or direction == 's':
			if arr[plyr_y + 1][plyr_x] != '+':
				plyr_y += 1
		elif direction == 'A' or direction == 'a':
			if arr[plyr_y][plyr_x - 1] != '+':
				plyr_x -= 1
		elif direction == 'D' or direction == 'd':
			if arr[plyr_y][plyr_x + 1] != '+':
				plyr_x += 1
		elif direction == 'q':
			quit()
		turns += 1

	def check_if_won():
		global plyr_x, plyr_y, maze
		if plyr_x == 12 and plyr_y == 9:
			print_maze(maze)
			print("YOU DID IT!!")
			time.sleep(2)
			return True
	while turns <= 24:
		print_maze(maze)
		move_player(maze)
		if turns == 24:
			if check_if_won() == True:
				return True
			else:
				print_maze(maze)
				print("Sorry you failed!")
				time.sleep(1)
				return False
	print_maze(maze)
	print("Sorry you failed!")
	time.sleep(1)
	return False	
	
