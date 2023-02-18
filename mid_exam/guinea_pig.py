# Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and
# buys him everything he needs – food, hay, and cover. On the first three lines, you will receive the quantity of
# food, hay, and cover, which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's
# weight. Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain
# amount of hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of
# 1/3 of its weight. Calculate whether the quantity of food, hay, and cover, will be enough for a month. If Merry
# runs out of food, hay, or cover, stop the program! Input On the first line – quantity food in kilograms - a
# floating-point number in the range [0.0 – 10000.0] On the second line – quantity hay in kilograms - a
# floating-point number in the range [0.0 – 10000.0] On the third line – quantity cover in kilograms - a
# floating-point number in the range [0.0 – 10000.0] On the fourth line – guinea's weight in kilograms - a
# floating-point number in the range [0.0 – 10000.0] Output If the food, the hay, and the cover are enough,
# print: "Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}." If one of
# the things is not enough, print: "Merry must go to the pet store!" The output values must be formatted to the
# second decimal place!


food_in_kilograms = float(input())
hay_in_kilograms = float(input())
cover_in_kilograms = float(input())
weight_in_kilograms = float(input())

food_in_grams = food_in_kilograms * 1000
hay_in_grams = hay_in_kilograms * 1000
cover_in_grams = cover_in_kilograms * 1000
weight_in_grams = weight_in_kilograms * 1000
is_food_not_left = False
month_days = 30

for day in range(1, month_days + 1):
    food_in_grams -= 300
    if food_in_grams <= 0:
        is_food_not_left = True

    if day % 2 == 0:
        hay_in_grams -= food_in_grams * (5 / 100)
        if hay_in_grams <= 0:
            is_food_not_left = True

    if day % 3 == 0:
        cover_in_grams -= weight_in_grams * 1 / 3
        if cover_in_grams <= 0:
            is_food_not_left = True

    if is_food_not_left:
        print('Merry must go to the pet store!')
        break

if not is_food_not_left:
    print('Everything is fine! Puppy is happy! 'f'Food: {food_in_grams / 1000:.2f}, ' 
          f'Hay: {hay_in_grams / 1000:.2f}, ' f'Cover: {cover_in_grams / 1000:.2f}.')
