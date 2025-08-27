# File Read & Write Challenge + Error Handling Lab

This program demonstrates how to:
- Read a file safely using exception handling
- Modify content (convert to uppercase)
- Write the result to a new file

## 🔧 Features
- ✅ User input for filename
- ✅ Handles missing files (`FileNotFoundError`)
- ✅ Handles permission issues (`PermissionError`)
- ✅ Graceful error messages
- ✅ Writes modified content to `modified_output.txt`

## 📝 Example Usage
1. Save a text file (e.g., `input.txt`) in the same folder.
2. Run the program.
3. Enter `input.txt` when prompted.
4. Output will be saved as `modified_output.txt`.

## 📂 Files
- `main.py` – The main program
- `README.md` – This file

## 🚀 How to Run
Make sure you have Python installed. Then run:
```bash
python main.py

🛠️ Sample Output
Enter the filename to read: input.txt
Successfully read 'input.txt'
Original content:
Hello World!

Modified content written to 'modified_output.txt'
Created by: Eden
Date: 2025
