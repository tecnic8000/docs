import os

def create_folders(base_path, folder_structure):
    for folder in folder_structure:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")

# Define your folder structure
folder_structure = [
    "project",
    "project/assets",
    "project/assets/textures",
    "project/assets/models",
    "project/scripts",
    "project/configs"
]

# Set the base path
base_path = "C:/Users/YourUser/Desktop"  # Change this to your target directory

# Create folders
create_folders(base_path, folder_structure)