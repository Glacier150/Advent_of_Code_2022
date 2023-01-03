with open("input-1.txt", "r") as str_input: # Check that you are in the proper working directory, "day_1", so that the relative path to "input_1.txt" works as intended.
    input = str_input.read()

totals = []
top_3 = []
elves = [cal for cal in input.split("\n\n")]

# Part 1

for elf in elves:
    cal_list = [int(cal) for cal in elf.split("\n") if cal.isnumeric()]
    totals.append(sum(cal_list))

print(max(totals))

# Part 2

for i in range(3):
    most = max(totals)
    top_3.append(most)
    totals.remove(most)

print(sum(top_3))