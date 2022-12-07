with open("input.txt", "r") as str_input:
    input = str_input.read()

totals = []
i = 0
top_3 = []
elves = [cal for cal in input.split("\n\n")]

for elf in elves:
    cal_list = [int(cal) for cal in elf.split("\n") if cal.isnumeric()]
    totals.append(sum(cal_list))

print(max(totals))

while i < 3:
    most = max(totals)
    top_3.append(most)
    totals.remove(most)
    i += 1

print(sum(top_3))