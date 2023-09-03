def blackjack(cards):
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    total = 0
    aces = 0

    for card in cards:
        total += values[card]
        if card == 'A':
            aces += 1

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    if total > 21:
        return 'Bust'
    else:
        return total


# Приклад використання
player_cards = ['A', 'Q', '5']
dealer_cards = ['K', '6']

player_score = blackjack(player_cards)
dealer_score = blackjack(dealer_cards)

print("Гравець:", player_cards, "Очки:", player_score)
print("Дилер:", dealer_cards, "Очки:", dealer_score)
