# As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
# His equipment consists of a helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.
# Input / Constraints
# The input will consist of 5 lines:
# ⦁	On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# ⦁	On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# ⦁	On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# ⦁	On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# ⦁	On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].
# Output
# ⦁	As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmets = 0
swords = 0
shields = 0
armors = 0
repair_cost = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        helmets += 1
    if fight % 3 == 0:
        swords += 1
    if fight % 6 == 0:
        shields += 1
    if fight % 12 == 0:
        armors += 1

repair_cost = helmets * helmet_price + swords * sword_price + shields * shield_price + armor_price * armors

print(f"Gladiator expenses: {repair_cost:.2f} aureus")
