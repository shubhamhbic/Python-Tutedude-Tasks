try:
    file = open("sample.txt", "r")
    print("Reading file content:")
    print(file.read())

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
