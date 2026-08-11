# Desc
# Opens a file, reads its byte value and converts it to hex

from pathlib import Path


while True:

	usr_inp=input("Enter file name:		")

	try:

		# searches current dir

		file=Path(usr_inp)

	except FileNotFoundError as e:
		print(e)

	except ValueError as e:
		print(e)

	else:

		# executes calculation if no error conditions are met

		stats=file.stat()
		print(f"Size: {stats.st_size} bytes.")

		byte_count=stats.st_size
		hex_val=hex(byte_count)
		print(f"Hex value is {hex_val}.")

	finally:

		# always executes, signals program ends

		print("Closing program...Done.")
		break
