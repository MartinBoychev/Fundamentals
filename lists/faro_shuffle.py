# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the
# cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and
# the original top card is still on top. For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five',
# 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six'] Write a program that receives a single string (
# cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the
# state of the deck after the shuffle. Note: The length of the deck of cards will always be an even number.

cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    final_cards = []
    middle_of_cards = len(cards) // 2
    first_part_cards = cards[0:middle_of_cards]
    sec_part_cards = cards[middle_of_cards::]
    for index_card in range(len(first_part_cards)):
        final_cards.append(first_part_cards[index_card])
        final_cards.append(sec_part_cards[index_card])
        cards = final_cards

print(cards)
