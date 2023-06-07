import card
import table as t
import utils

class Player:
    chips:int
    current_table: t.Table
    current_card1: card.Card
    current_card2: card.Card

    def __init__(self):
        self.chips = 10000
        self.current_table = None
        self.current_card1 = None
        self.current_card2 = None

    def bet(self, bet_chips):
        if (bet_chips > self.chips):
            print("Not enough chips")
        else:
            self.chips = self.chips - bet_chips

    def win(self, win_chips):
        self.chips = self.chips + win_chips

    def join_table(self, new_table):
        self.current_table = new_table

    def assign_cards(self):
        self.current_card1 = card.Card(self.current_table.get_current_cards())
        self.current_table.get_current_cards().append(self.current_card1)

        self.current_card2 = card.Card(self.current_table.get_current_cards())
        self.current_table.get_current_cards().append(self.current_card2)

    def get_current_cards(self):
        return self.current_card1, self.current_card2
    
    def get_highest_hand(self):
        all_cards = self.current_table.get_table_cards()
        all_cards.append(self.current_card1)
        all_cards.append(self.current_card2)

        all_cards.sort(key=lambda x:x.card_value, reverse=True)
        print("Player cards are")
        for card in all_cards:
            print(str(card.get_card_value()) + " "+ str(card.get_card_type()))

        if utils.check_straight_flush(all_cards):
            print("Player has straight flush")
        elif utils.check_four_of_a_kind(all_cards):
            print("Player has four of a kind")
        elif utils.check_full_house(all_cards):
            print("Player has a full house")
        elif utils.check_flush(all_cards):
            print("Player has flush")
        elif utils.check_straight(all_cards)[0]:
            print("Player has straight")
        elif utils.check_three_of_a_kind(all_cards)[0]:
            print("Player has three of a kind")
        elif utils.check_two_pairs(all_cards):
            print("Player has two pairs")
        elif utils.check_one_pair(all_cards)[0]:
            print("Player has one pair")
        else:
            print("Player has high card")



