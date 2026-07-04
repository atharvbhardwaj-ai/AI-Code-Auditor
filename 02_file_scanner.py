# Defining the target file path
target_file = "C:/Users/Atharv/Documents/Codes/Summer_Assignment_25112CN382/Week-4/Day-28/Q110_bank_account.cpp"

# Using 'with' handles opening and automatic closing cleanly
with open(target_file, "r") as file:
    line_num = 1
    
    # Python lets you loop directly over the file object line by line!
    for line in file:
        # end="" prevents double spacing because raw lines already contain '\n'
        print(f"{line_num}: {line}", end="")
        line_num += 1