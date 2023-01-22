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
