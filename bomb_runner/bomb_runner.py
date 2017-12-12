import os
import random
import time
import bomb_modules as bm
import msvcrt

gameBoard = [
	['+','+','+','+','+','+','+','+','+','+','+','+','+'], # x 1-11
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'], # y 1-3
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
	['+','+','+','+','+','+','+','+','+','+','+','+','+'], # 1-11
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'], # y 6 or 7
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
	['+','+','+','+','+','+','+','+','+','+','+','+','+'], # x 1-11
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'], # y 10 or 11
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
	['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
	['+','+','+','+','+','+','+','+','+','+','+','+','+']
]

'''Global Variables'''
modules = [1,2,3,4,5]
plyr_x = 6
plyr_y = 12
bombs_defused = 0
lives = 3
flag = 1

bomb1x = random.randrange(1,12)
bomb1y = random.randrange(10,12)	
bomb2x = random.randrange(1,12)
bomb2y = random.randrange(6,8)	
bomb3x = random.randrange(1,12)
bomb3y = random.randrange(1,4)	


def intro():
	os.system('cls')
	print("__________              ___.     __________                                  ")
	print("\______   \ ____   _____\_ |__   \______   \__ __  ____   ____   ___________ ")
	print(" |    |  _//  _ \ /     \| __ \   |       _/  |  \/    \ /    \_/ __ \_  __ \\")
	print(" |    |   (  <_> )  Y Y  \ \_\ \  |    |   \  |  /   |  \   |  \  ___/|  | \/")
	print(" |______  /\____/|__|_|  /___  /  |____|_  /____/|___|  /___|  /\___  >__|   ")
	print("        \/             \/    \/          \/           \/     \/     \/       \n\n")
	print("    ____           ________                       ____                   __    __")
	print("   / __ )__  __   / ____/ /_  ____ _________     / __ \____  _________ _/ /_  / /")
	print("  / __  / / / /  / /   / __ \/ __ `/ ___/ _ \   / / / / __ \/ ___/ __ `/ __ \/ / ")
	print(" / /_/ / /_/ /  / /___/ / / / /_/ (__  )  __/  / /_/ / /_/ (__  ) /_/ / / / / /  ")
	print("/_____/\__, /   \____/_/ /_/\__,_/____/\___/   \____/ .___/____/\__,_/_/ /_/_/   ")
	print("      /____/                                       /_/                           \n\n")
	input("Press ENTER to start!")


def bomb_init():
		global bombs_defused, flag
		global bomb1x, bomb1y, bomb2x, bomb2y, bomb3x, bomb3y
		gameBoard[bomb1y][bomb1x] = '#'		
		gameBoard[bomb2y][bomb2x] = '#'
		gameBoard[bomb3y][bomb3x] = '#'

def bomb_change_sprite():
	global bomb1x, bomb1y
	global bombs_defused
	
	if bombs_defused == 1:
		gameBoard[bomb1y][bomb1x] = '*'
	if bombs_defused == 2:
		gameBoard[bomb2y][bomb2x] = '*'	
	if bombs_defused == 3:
		gameBoard[bomb3y][bomb3x] = '*'
	
def print_gameboard():
	print("W = up\nS = down\nA = left\nD = right")
	print("Lives: " + str(lives) + "      Bombs Defused: " + str(bombs_defused))
	for y in range(0 ,14):
		for x in range(0,13):
			if y == plyr_y and x == plyr_x:
				print("P ", end = '')
			else:
				print(gameBoard[y][x] + " ", end = "")
		
		print()

def move_player():
	global plyr_x, plyr_y
	direction = msvcrt.getwch()
	if direction == 'W' or direction == 'w':
		if gameBoard[plyr_y - 1][plyr_x] != '+':
			plyr_y -= 1
	elif direction == 'S' or direction == 's':
		if gameBoard[plyr_y + 1][plyr_x] != '+':
			plyr_y += 1
	elif direction == 'A' or direction == 'a':
		if gameBoard[plyr_y][plyr_x - 1] != '+':
			plyr_x -= 1
	elif direction == 'D' or direction == 'd':
		if gameBoard[plyr_y][plyr_x + 1] != '+':
			plyr_x += 1

def check_for_bombs():
	global plyr_x, plyr_y
	os.system("cls")
	print_gameboard()
	if gameBoard[plyr_y - 1][plyr_x]=='#' or gameBoard[plyr_y + 1][plyr_x]=='#' or gameBoard[plyr_y][plyr_x - 1]=='#' or gameBoard[plyr_y][plyr_x + 1]=='#':
		defuse = input("There's a bomb! Type 'DEFUSE': ").upper()
		if defuse == "DEFUSE":
			return True
		elif defuse != "DEFUSE":
			return False

def defuse_bomb():
	global bombs_defused, lives, modules
	select_bomb = random.choice(modules)
	for n in modules:
		if select_bomb == n:
			select_bomb = random.choice(modules)
	
	if check_for_bombs() == True:
		if select_bomb == 1:
			if bm.module_one() == True:
				bombs_defused += 1
				modules.remove(select_bomb)
			else:
				lives -= 1
		elif select_bomb == 2:
			if bm.module_two() == True:
				bombs_defused += 1
				modules.remove(select_bomb)
			else:
				lives -= 1
		elif select_bomb == 3:
			if bm.module_three() == True:
				bombs_defused += 1
				modules.remove(select_bomb)
			else:
				lives -= 1
		elif select_bomb == 4:
			if bm.module_four() == True:
				bombs_defused += 1
				modules.remove(select_bomb)
			else:
				lives -= 1
		elif select_bomb == 5:
			if bm.module_five() == True:
				bombs_defused += 1
				modules.remove(select_bomb)
			else:
				lives -= 1
				
	if bombs_defused == 1:
		gameBoard[9][6] = " "
	elif bombs_defused == 2:
		gameBoard[5][6] = " "
								
def check_if_won():
	global bombs_defused
	if bombs_defused == 3:
		os.system("cls")
		print_gameboard()
		print("Congrats! You saved the world!")
		time.sleep(2)
		return True
	else:
		return False

def main():
	global lives
	flag = 0
	bomb_init()
	intro()
	while lives > 0:
		os.system("cls")
		print_gameboard()
		move_player()
		defuse_bomb()
		bomb_change_sprite()
		if check_if_won() == True:
			return True
	
	os.system('cls')
	print("You died!")
	print("Lives: " + str(lives) + "      Bombs Defused: " + str(bombs_defused))
	time.sleep(1)	
main()
