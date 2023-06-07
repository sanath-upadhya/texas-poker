import random

class Card:
    card_type: int
    card_value: int

    def __init__(self, present_cards):
        self.get_new_card_values()

        found_new_card = False

        while not found_new_card:
            card_already_present = False
            for card in present_cards:
                if self.card_type == card.get_card_type() and self.card_value == card.get_card_value():
                    self.get_new_card_values()
                    card_already_present = True
                    break
            
            if not card_already_present:
                found_new_card = True

    def get_new_card_values(self):
        self.card_type = random.randint(1,4)
        self.card_value = random.randint(1,13)
    
    def get_card_value(self):
        return self.card_value

    def get_card_type(self):
        return self.card_type