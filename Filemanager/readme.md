# File Management System

## Description
This Python-based File Management System allows users to perform various file and folder operations, including creating, deleting, renaming, searching, and listing files and folders. The system is designed for simplicity and uses the command-line interface (CLI) to interact with the user.

## Features
1. **File Management**
   - Create new files in specified directories.
   - Delete existing files.
   - Rename files.

2. **Folder Management**
   - Create new folders.
   - Delete existing folders.
   - Rename folders.

3. **Search Functionality**
   - Search for files and folders by keyword.

4. **List Files and Folders**
   - Display all files and folders in a specified directory.

5. **Error Handling**
   - Provides meaningful error messages for invalid operations or paths.

## How to Use
1. Clone the repository or download the script.
2. Run the script using Python:
   ```bash
   python file_management_system.py
   ```
3. Follow the on-screen prompts to choose an operation:
   - Create File
   - Delete File
   - Rename File/Folder
   - Create Folder
   - Delete Folder
   - Search
   - List Files and Folders
   - Exit

## Example Input/Output
### Input
```plaintext
Enter your choice (1-8): 1
Enter file name: example.txt
Enter folder path: /documents
```
### Output
```plaintext
File 'example.txt' created successfully in '/documents'.
```

## Requirements
- Python 3.x

## Modules Used
- `os`: For file and folder operations.
- `shutil`: For folder deletion.

## Future Enhancements
- Add a graphical user interface (GUI).
- Implement advanced search filters (e.g., by file type, size, date).
- Add file editing capabilities.

## License
This project is licensed under the MIT License.
