# Tony and Andi love playing in the snow and having snowball fights,
# but they always argue about who makes the best snowballs.
# They have decided to involve you in their fray by writing a program
# that calculates snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# ⦁	The weight of the snowball (integer).
# ⦁	The time needed for the snowball to get to its target (integer).
# ⦁	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.


num_snowballs = int(input())
snowball_weight_highest = 0
snowball_time_highest = 0
snowball_quality_highest = 0
best_value = 0

for _ in range(num_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_weight / snowball_time) ** snowball_quality

    if value > best_value:
        best_value = int(value)
        snowball_weight_highest = snowball_weight
        snowball_time_highest = snowball_time
        snowball_quality_highest = snowball_quality

print(f"{snowball_weight_highest} : {snowball_time_highest} = {best_value} ({snowball_quality_highest})")
