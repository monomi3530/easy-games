import random

# игровая логика

class machanics():

    field = []
    # игра 

    def __init__(self):
        self.player = []
        self.dealer = []
        self.player_cards = []
        self.dealer_cards = ['        ┌─────────┐\n        │ ??      │\n        │         │\n        │    ?    │\n        │         │\n        │      ?? │\n        └─────────┘\n        ']
        self.deck = self.new_deck()



    # колода 
    def new_deck(self):
        suits = ["♠", "♥", "♦", "♣"]
        values = {"A" : 11, "К" : 10, "Q" : 10, "J" : 10, "10": 10, "9" : 9,"8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}
        new_deck = [(rank, suit, values[rank]) for rank in values for suit in suits]
        return new_deck
    # игровое поле
    def game_card(self, rank, suit):

        card_template =  f"""
        ┌─────────┐
        │ {rank:<2}      │
        │         │
        │    {suit}    │
        │         │
        │      {rank:>2} │
        └─────────┘
        """
        return card_template.strip("\n")

    # ход игрока
    def mov(self):
        num = random.choice(self.deck)
        self.deck.remove(num)
        self.player.append(num)
        card_visual = self.game_card(num[0], num[1])
        self.player_cards.append(card_visual)
        self.show_field()
        print(f"player: {num}")
        return num

    def show_field(self):
        # выводим карты игрока в одну строку
        print("Player's Cards:")
        split_cards = [card.split("\n") for card in self.player_cards]
        for line in zip(*split_cards):
            print(" ".join(line))

        print("\n")

    def dealer_mov(self):
        num = random.choice(self.deck)
        self.deck.remove(num)
        self.dealer.append(num)
        self.show_fields()

    def dealer_game(self):
        numb = random.choice(self.deck)
        self.deck.remove(numb)
        self.dealer.append(numb)
        card_visual = self.game_card(numb[0], numb[1])
        self.dealer_cards.append(card_visual)
        self.show_fields()
        return numb


    
    def show_fields(self):
        # выводим карты игрока в одну строку
        print("Dealer`s Cards:")
        split_cards = [card.split("\n") for card in self.dealer_cards]
        for line in zip(*split_cards):
            print(" ".join(line))

        print("\n")

    def clear_list(self):
        self.player = []
        self.dealer = []
        self.player_cards = []
        self.dealer_cards = ['        ┌─────────┐\n        │ ??      │\n        │         │\n        │    ?    │\n        │         │\n        │      ?? │\n        └─────────┘\n        ']
        self.deck = self.new_deck()










def ace(total_pl, total_dl, player_cards, dealer_cards):
    # Берем карты игрока
    if total_pl > 21:  # Проверяем, если сумма больше 21
        for i in range(len(player_cards)):
            if player_cards[i][0] == "A" and player_cards[i][2] == 11:
                # Заменяем 11 на 1
                player_cards[i] = ("A", player_cards[i][1], 1)
        total_pl = sum(card[2] for card in player_cards)  # Пересчитываем сумму для игрока
    
    # Берем карты дилера
    if total_dl > 21:  # Проверяем, если сумма больше 21
        for i in range(len(dealer_cards)):
            if dealer_cards[i][0] == "A" and dealer_cards[i][2] == 11:
                # Заменяем 11 на 1
                dealer_cards[i] = ("A", dealer_cards[i][1], 1)
        total_dl = sum(card[2] for card in dealer_cards)  # Пересчитываем сумму для дилера

    return total_pl, total_dl, player_cards, dealer_cards
# план проекта 
"""
- пробная версия игры готова 

"""

print()
print("WELCOME TO BLACKJACK")

def update_victory_counter():
    return f"""
███████████████████████████████████████████████████████████████
█                       ІГРОК:  █ ████████████████████████  {player_wins} █
█                       ДИЛЕР:  █ ████████████████████████  {dealer_wins} █
███████████████████████████████████████████████████████████████
"""

start_game = """
*********************************
*   ███████  █████  ██████      *
*   ██      ██   ██ ██   ██     *
*   █████   ███████ ██████      *
*   ██      ██   ██ ██   ██     *
*   ██      ██   ██ ██   ██     *
*      S T A R T   G A M E      *
*********************************
"""

player_wins = 0
dealer_wins = 0

blackjack = machanics()
start = False

print(update_victory_counter())
while True:

    starting = input("Do you want to start the game? (y/n): ").lower()
    if starting == "y":
        start = True
    elif starting == "n":
        start = False
        print("это на минуточку вторая игра которую я написал")
        startings = input("Вы уверены что не хотите играть в blackjack (y/n): ")
        if startings == "y":
            print("спасибо за игру! пока")
            break
        else:
            continue

    while start:

        print(start_game)

        starts = input("Вы готовы начать игру? (y/n): ")
        if starts  == "y":
            pass
        elif starts  == "n":
            break

        print()
        print("Диллер начинает рассдачу карт на стол")
        print()

        blackjack.dealer_mov()
        blackjack.mov()

        print()
        print("Диллер раздает вторую игровую карту")
        print()

        blackjack.mov()
        blackjack.dealer_game()

        while True:

            player_win = blackjack.player
            dealer_win = blackjack.dealer

            total = sum(card[2] for card in player_win)
            totals = sum(cars[2] for cars in dealer_win)

            if total == 21 and totals != 21 or totals > 21:
                player_wins += 1
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("You win")
                start = False
                print(update_victory_counter())
                blackjack.clear_list()
                break
            elif totals == 21 and total != 21 or total > 21:
                dealer_wins += 1
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("dealer win!")
                start = False
                print(update_victory_counter())
                blackjack.clear_list()
                break
            elif total == 21 and  totals == 21:
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("draw")
                start = False
                print(update_victory_counter())
                blackjack.clear_list()
                break

            ace(total, totals, blackjack.player, blackjack.dealer)
            total = sum(card[2] for card in player_win)
            totals = sum(cars[2] for cars in dealer_win)

            # цыкл хотите взять ещё карту 
            while True:
                print(f"Общая ваша сумма очков {total}")
                take = input("Хотите взять еще карту? (y/n): ").lower()
                if take == "y":
                    print("Игрок берёт карту")
                    blackjack.mov()
                    total = sum(card[2] for card in player_win)
                    ace(total, totals, blackjack.player, blackjack.dealer)
                elif take == "n":
                    print("Ход дилера")
                    break

            ace(total, totals, blackjack.player, blackjack.dealer)
            total = sum(card[2] for card in player_win)

            if total > 21: 
                dealer_wins += 1
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("dealer win!")
                start = False
                blackjack.clear_list()
                print(update_victory_counter())
                break

            if totals <= 16:
                blackjack.dealer_game()
                print()
                print("диллер берет карту ")
                print()
                
            
            ace(total, totals, blackjack.player, blackjack.dealer)
            totals = sum(cars[2] for cars in dealer_win)

            if totals > 21:
                player_wins += 1
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("You win")
                start = False
                blackjack.clear_list()
                print(update_victory_counter())
                break

            if total > totals:
                player_wins += 1
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("You win")
                start = False
                blackjack.clear_list()
                print(update_victory_counter())
                break
            elif totals > total:
                dealer_wins += 1
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("dealer win!")
                start = False
                blackjack.clear_list()
                print(update_victory_counter())
                break
            elif total == totals:
                print(f"Общая ваша сумма очков {total}")
                print(f"Общая сумма очков дилера {totals}")
                print()
                print("draw")
                start = False
                blackjack.clear_list()
                print(update_victory_counter())
                break



            








        


