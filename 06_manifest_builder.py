import os

# 1. Setup paths (Using your Day-28 folder as our testbed)
target_folder = "C:/Users/Atharv/Documents/Codes/Summer_Assignment_25112CN382/Week-5/Day-30"
all_files = os.listdir(target_folder)

# 2. This master dictionary will hold our final audited payload
project_manifest = {}

print("--- Initializing Code Extraction Pipeline ---")

for file_name in all_files:
    if file_name.endswith(".cpp"):
        # We need the full absolute path to open the file correctly
        full_path = os.path.join(target_folder, file_name)
        
        # Open the file and extract its content
        with open(full_path, "r") as f:
            raw_code = f.read()  # .read() grabs the entire file content as one big string!
            
        # Store it in our dictionary: { "FileName.cpp": "raw code string here" }
        project_manifest[file_name] = raw_code
        print(f"Successfully loaded: {file_name} into memory.")

print("\n--- Pipeline Extraction Complete ---")

count = 0
for file in all_files:
    if (file.endswith(".cpp")):
        count += 1

print(f"There are {count} files stored in the target folder\n")

print(project_manifest["Q120_Mini_Project.cpp"])