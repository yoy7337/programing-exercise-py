## path and file basic

from pathlib import Path

print ("==\n")

## path1
file_path = Path.home() / "my_folder" / "my_file.txt"
print(file_path)

print(file_path.exists())

print(file_path.name)

print(file_path.parent.name)

print ("==\n")

## path2
script_path = Path(__file__).resolve()

print(script_path)

print(script_path.exists())

print(script_path.name)

print(script_path.parent.name)
print ("==\n")

## path3
csv_path = script_path.parent / "csv_data" / "1.csv"

print(csv_path)

print(csv_path.exists())

print(csv_path.name)

print(csv_path.parent.name)
print ("==\n")