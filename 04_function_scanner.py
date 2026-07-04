file_path = "C:/Users/Atharv/Documents/Codes/Summer_Assignment_25112CN382/Week-4/Day-28/Q110_bank_account.cpp"
line_count = 1

with open(file_path, "r") as file:
    for line in file:
        if ((("int" in line) or ("void" in line)) and "(" in line):
            if ";" not in line and "<" not in line and ">" not in line:
                print(f"{line_count}- Function Found!:\n{line}")
        line_count += 1