with open("input-2.txt", "r") as str_input:
    input = str_input.read()

# Part 1

score = 0
opp_strat = ["A", "B", "C", "A"]
your_strat = ["X", "Y", "Z", "X"]
games = [game for game in input.split("\n")]

for game in games:
    score += game.count("X")
    score += game.count("Y") * 2
    score += game.count("Z") * 3
    for i in range (3):
        if opp_strat[i] in game and your_strat[i] in game:
            score += 3
        elif opp_strat[i] in game and your_strat[i+1] in game:
            score += 6

print(score)

# Part 2

new_score = 0
opp_strat_2 = ["A", "B", "C"]
shape_points = [1, 2, 3]

for game in games:
    new_score += game.count("Y") * 3
    new_score += game.count("Z") * 6

#for i in range(3):
#    for game in games:
#        if "X" in game:
#            new_score += shape_points[i-1]
#        elif "Y" in game:
#            new_score += shape_points[i]
#        elif "Z" in game:
#            if i < 2:
#                new_score += shape_points[i]
#            elif i == 2:
#               new_score += shape_points[0]

#print(new_score)

# I don't know why the above commented out code doesn't work right, I think it has something to do with the loops or the lists I use, but I don't know.