file = "C:/Users/Atharv/Documents/Codes/Summer_Assignment_25112CN382/Week-4/Day-28/Q110_bank_account.cpp"
comment_count = 0

with open(file, "r") as file:
    for line in file:
        if ("//" in line):
            comment_count += 1

print(f"The total number of comments in the given file is {comment_count}") 