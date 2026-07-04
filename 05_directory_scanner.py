import os

# Target directory containing your recent day-to-day assignments
target_folder = "C:/Users/Atharv/Documents/Codes/Summer_Assignment_25112CN382/Week-4/Day-28"

# os.listdir() returns a Python list containing the names of all files inside that folder
all_files = os.listdir(target_folder)

print("--- Files Found in Directory ---")
for file_name in all_files:
    if (file_name.endswith(".cpp")):
        print(f"Discovered: {file_name}")