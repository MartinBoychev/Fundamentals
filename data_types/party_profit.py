# As a young adventurer, you travel with your group worldwide, seeking for gold and glory.
# But you need to split the profit among your companions.
# You will receive a group size. After that, you receive the days of the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion.
# But if you have a motivational party the same day, you spend additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
# but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
# You should calculate how many coins gets each companion at the end of the adventure.

group_size = int(input())
days = int(input())
coins = 50 - group_size * 2
final_coins = coins
people_left = group_size
count_days = 1

while count_days != days:
    count_days += 1
    if count_days % 15 == 0:
        people_left += 5
    if count_days % 10 == 0:
        people_left -= 2
    final_coins += 50 - 2 * people_left

    if count_days % 3 == 0:
        final_coins -= 3 * people_left
    if count_days % 5 == 0:
        final_coins += 20 * people_left
    if count_days % 15 == 0:
        final_coins -= 2 * people_left

coins_per_person = final_coins // people_left

print(f"{people_left} companions received {coins_per_person} coins each.")
