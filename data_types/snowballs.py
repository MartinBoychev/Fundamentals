num_snowballs = int(input())
snowball_weight_highest = 0
snowball_time_highest = 0
snowball_quality_highest = 0
value = 0
for _ in range(num_snowballs):
    snowball_weight = int(input())
    if snowball_weight > snowball_weight_highest:
        snowball_weight_highest = snowball_weight
    snowball_time = int(input())
    if snowball_time > snowball_time_highest:
        snowball_time_highest = snowball_time
    snowball_quality = int(input())
    if snowball_quality > snowball_quality_highest:
        snowball_quality_highest = snowball_quality

value = (snowball_weight_highest / snowball_time_highest) ** snowball_quality_highest
print(f"{snowball_weight_highest} : {snowball_time_highest} = {value} ({snowball_quality_highest})")


