import sys
from queries import *

COMMAND_COUNT = 11
running = True

cursor = connect()
if cursor is None:
	print("Error: Unable to connect to the database")
	sys.exit()

while running:
	print("\n==========================IMDB COMMAND MENU===========================")
	print("| 1. GET NUMBER OF MOVIES IN A SELECTED GENRE                          |")
	print("| 2. GET NUMBER OF SELECTED GENRES IN A CERTAIN YEAR                   |")
	print("| 3. GET NUMBER OF ACTRESSES IN MOVIES FOR A CERTAIN YEAR              |")
	print("| 4. GET NUMBER OF MOVIES IN A CERTAIN YEAR                            |")
	print("| 5. WHICH YEAR HAD THE MOST MOVIES?                                   |")
	print("| 6. HOW MANY ACTORS STAR IN A SELECTED GENRE?                         |")
	print("| 7. HOW MANY ACTORS WITH A CERTAIN FIRST NAME ARE IN THE DATABASE?    |")
	print("| 8. WHICH GENRE PRODUCES THE MOST MOVEIS?                             |")
	print("| 9. WHICH MOVIES HAVE MORE THAN A SELECTED NUMBER OF GENRES?          |")
	print("| 10. HOW MANY ACTORS ARE KNOW BY MORE THAN A SELECTED NUMBER OF NAMES?|")
	print("| 11. EXIT 															  |")
	print("==============================================\n")
	choice = input("Select a Option: ")

	try:
		choice = int(choice)
		if choice > COMMAND_COUNT or choice <= 0:
			raise ValueError  
	except ValueError as err:
		print('Not a Valid Command.')
		continue
	
	if choice == 1:
		query_one(cursor)
	elif choice == 2:
		query_two(cursor)
	elif choice == 3:
		query_three(cursor)
	elif choice == 4:
		query_four(cursor)
	elif choice == 5:
		query_five(cursor)
	elif choice == 6:
		query_six(cursor)
	elif choice == 7:
		query_seven(cursor)
	elif choice == 8:
		query_eight(cursor)
	elif choice == 9:
		query_nine(cursor)
	elif choice == 10:
		query_ten(cursor)
	elif choice == 11:
		print('Exiting Command Menu...')
		running = False
