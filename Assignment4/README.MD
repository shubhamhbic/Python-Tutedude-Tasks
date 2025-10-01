# Task 1 ---- Read a File and Handle Errors 

This program demonstrates how to safely read a file in Python using **exception handling**.  
It tries to open and read `sample.txt`, and if the file is not found, it handles the error gracefully.

---

## 📋 How It Works
1. The program attempts to:
   - Open `sample.txt` in **read mode (`"r"`)**.
   - Print the contents of the file.

2. If the file is missing:
   - A `FileNotFoundError` is raised.
   - The program catches the error and displays a friendly error message instead of crashing.

---

## ▶️ Example Run

### Case 1: File exists
Reading file content:
Line1: This is sample text file.
Line2: It contains multiple lines.


### Case 2: File does not exist
Error: The file 'sample.txt' was not found.



=============================================================================================================================


# Task 2 -----File Handling: Write and Append (Python)

This program demonstrates how to **write, append, and read data from a file** using Python’s built-in file handling methods.

---

## 📋 How It Works
1. **Write Mode (`"w"`)**  
   - Opens `file.txt` (creates it if not present).
   - Writes user input to the file.
   - Overwrites existing content if the file already exists.

2. **Append Mode (`"a"`)**  
   - Reopens `file.txt`.
   - Appends additional user input to the end of the file.

3. **Read Mode (`"r"`)**  
   - Reads and prints the final contents of `file.txt`.

---

## ▶️ Example Run
Enter text to write to file: Hello World
Data successfully written to output.txt.

Enter additional text to append: This is Python file handling!
Data successfully appended.

Final contents of output.txt:
Hello World
This is Python file handling!
