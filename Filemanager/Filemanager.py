import os
import shutil

def create_file(file_name, folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as file:
            file.write("")  # Create an empty file
        return f"File '{file_name}' created successfully in '{folder_path}'."
    except Exception as e:
        return f"Error creating file: {e}"

def delete_file(file_name, folder_path):
    try:
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"File '{file_name}' deleted successfully from '{folder_path}'."
        else:
            return f"File '{file_name}' does not exist in '{folder_path}'."
    except Exception as e:
        return f"Error deleting file: {e}"

def rename_file_or_folder(old_name, new_name, folder_path):
    try:
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            return f"'{old_name}' renamed to '{new_name}' in '{folder_path}'."
        else:
            return f"'{old_name}' does not exist in '{folder_path}'."
    except Exception as e:
        return f"Error renaming: {e}"

def create_folder(folder_name, parent_path):
    try:
        folder_path = os.path.join(parent_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder '{folder_name}' created successfully in '{parent_path}'."
    except Exception as e:
        return f"Error creating folder: {e}"

def delete_folder(folder_name, parent_path):
    try:
        folder_path = os.path.join(parent_path, folder_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            return f"Folder '{folder_name}' deleted successfully from '{parent_path}'."
        else:
            return f"Folder '{folder_name}' does not exist in '{parent_path}'."
    except Exception as e:
        return f"Error deleting folder: {e}"

def search_files_and_folders(keyword, search_path):
    try:
        results = []
        for root, dirs, files in os.walk(search_path):
            for name in files + dirs:
                if keyword.lower() in name.lower():
                    results.append(os.path.join(root, name))
        return results if results else f"No files or folders found with keyword '{keyword}' in '{search_path}'."
    except Exception as e:
        return f"Error searching: {e}"

def list_files_and_folders(folder_path):
    try:
        if os.path.exists(folder_path):
            return os.listdir(folder_path)
        else:
            return f"Folder '{folder_path}' does not exist."
    except Exception as e:
        return f"Error listing contents: {e}"

# Sample Command-Line Interface
def main():
    while True:
        print("\nFile Management System")
        print("1. Create File")
        print("2. Delete File")
        print("3. Rename File/Folder")
        print("4. Create Folder")
        print("5. Delete Folder")
        print("6. Search")
        print("7. List Files and Folders")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            file_name = input("Enter file name: ")
            folder_path = input("Enter folder path: ")
            print(create_file(file_name, folder_path))

        elif choice == '2':
            file_name = input("Enter file name: ")
            folder_path = input("Enter folder path: ")
            print(delete_file(file_name, folder_path))

        elif choice == '3':
            old_name = input("Enter current name of file/folder: ")
            new_name = input("Enter new name: ")
            folder_path = input("Enter folder path: ")
            print(rename_file_or_folder(old_name, new_name, folder_path))

        elif choice == '4':
            folder_name = input("Enter folder name: ")
            parent_path = input("Enter parent folder path: ")
            print(create_folder(folder_name, parent_path))

        elif choice == '5':
            folder_name = input("Enter folder name: ")
            parent_path = input("Enter parent folder path: ")
            print(delete_folder(folder_name, parent_path))

        elif choice == '6':
            keyword = input("Enter keyword to search: ")
            search_path = input("Enter path to search in: ")
            results = search_files_and_folders(keyword, search_path)
            if isinstance(results, list):
                print("Search Results:")
                for result in results:
                    print(result)
            else:
                print(results)

        elif choice == '7':
            folder_path = input("Enter folder path: ")
            contents = list_files_and_folders(folder_path)
            if isinstance(contents, list):
                print("Contents:")
                for item in contents:
                    print(item)
            else:
                print(contents)

        elif choice == '8':
            print("Exiting File Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
