# Desc
# Opens a file of the user's choice and appends to it.

from pathlib import Path

while True:
	usr_inp=input("Enter file name:__")

		

	try:
		# searches current dir
		file=Path(usr_inp)

	except FileNotFoundError as e:
		print(e)

	except ValueError as e:
		print(e)

	else:

		usr_append=input("Write text to insert:__")
		with file.open(mode="a", encoding="utf-8") as file_append:
			file.write(f"{usr_append}\n")


	finally:
        print("File appended.")
        
		end_choice=input("Append to another file? (Y/N)")
		case_ins=end_choice.lower().strip()
		if(end_choice!="y"):
			print("Closing program...")
			break
			
