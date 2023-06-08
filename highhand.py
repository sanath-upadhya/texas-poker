class HighHand:
    hand_type: int
    high_hand_value: int
    second_high_hand_value: int
    remaining_cards: list

    def __init__(self):
        self.high_hand_value = -1
        self.hand_type = -1
        self.second_high_hand_value = -1
        self.remaining_cards = []

    def get_hand_type(self):
        return self.hand_type
    
    def get_high_hand_value(self):
        return self.high_hand_value
    
    def get_second_high_hand_value(self):
        return self.second_high_hand_value
    
    def get_remaining_cards(self):
        return self.remaining_cards

    def set_high_hand(self,hand_type,high_hand_value,second_high_hand_value,remaining_cards):
        self.hand_type = hand_type
        self.high_hand_value = high_hand_value
        self.second_high_hand_value = second_high_hand_value
        self.remaining_cards = remaining_cards
        remaining_card_last_index = len(remaining_cards) - 1
        #Padding for remaining card
        for i in range(0,3):
            if i > remaining_card_last_index:
                self.remaining_cards.append(0)
            else:
                self.remaining_cards.append(remaining_cards[i])

    def get_high_hand(self):
        print("Player has")
        if (self.hand_type == 10):
            print("Straight flush")
        elif (self.hand_type == 9):
            print("Four of a kind")
        elif (self.hand_type == 8):
            print("Full house")
        elif (self.hand_type == 7):
            print("Flush")
        elif (self.hand_type == 6):
            print("Straight")
        elif (self.hand_type == 5):
            print("Three of a kind")
        elif (self.hand_type == 4):
            print("Two pairs")
        elif (self.hand_type == 3):
            print("One pair")
        elif (self.hand_type == 2):
            print("High Card")
        else:
            print("Somethings wrong!!")

        print("High card is " + str(self.high_hand_value))
        print("Second high card is " + str(self.second_high_hand_value))
        print("Remaining card is ")
        print(self.remaining_cards)