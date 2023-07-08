name = input("enter a name: ")
family = input("enter a family: ")

score_1 = float(input("enter first score: "))
score_2 = float(input("enter first score: "))
score_3 = float(input("enter first score: "))

total = score_1 + score_2 + score_3
print(f"{name} {family}'s total score is:{total}")
print(f"{name} {family}'s average score is:{total/3}")