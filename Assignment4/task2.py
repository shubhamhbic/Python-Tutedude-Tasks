file = open("file.txt", "w")
writing = file.write(input("Enter text to write to file: "))
if writing>0:
    print("Data successfully written to output.txt.\n")
else:
    print("Something went wrong.")
file.close()

file = open("file.txt", "a")
file.write("\n")
appending = file.write(input("Enter additional text to append: "))
if appending>0:
    print("Data successfully appended.")
else:
    print("Something went wrong.")
file.close()

file = open("file.txt", "r")
print("\nFinal contents of output.txt:")
print(file.read())
file.close()
