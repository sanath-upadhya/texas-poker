import card
import table as t
import utils
import highhand

class Player:
    chips:int
    current_table: t.Table
    current_card1: card.Card
    current_card2: card.Card
    current_highhand: highhand.HighHand

    def __init__(self):
        self.chips = 10000
        self.current_table = None
        self.current_card1 = None
        self.current_card2 = None
        self.current_highhand = None

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
        # print("Player cards are")
        # for card in all_cards:
        #     print(str(card.get_card_value()) + " "+ str(card.get_card_type()))

        self.current_highhand = highhand.HighHand()
        is_straight_flush,card_num = utils.check_straight_flush(all_cards)
        if is_straight_flush:
            high_card_value = all_cards[card_num].get_card_value()
            self.current_highhand.set_high_hand(10,high_card_value,-1,[])
        else:
            #Check for four of a kind
            is_four_of_a_kind,high_card_value,second_card_value = utils.check_four_of_a_kind(all_cards)
            if is_four_of_a_kind:
                self.current_highhand.set_high_hand(9,high_card_value,second_card_value,[])
            else:
                #Check for full house
                is_full_house,high_card_value,second_card_value,remaining_card_values = utils.check_full_house(all_cards)
                if is_full_house:
                    self.current_highhand.set_high_hand(8,high_card_value,second_card_value,remaining_card_values)
                else:
                    #Check for flush
                    is_flush, high_card_value, second_card_value, remaining_card_values = utils.check_flush(all_cards)
                    if is_flush:
                        self.current_highhand.set_high_hand(7,high_card_value,second_card_value,remaining_card_values)
                    else:
                        #check for straight
                        is_straight,card_num = utils.check_straight(all_cards)
                        if is_straight:
                            high_card_value = all_cards[card_num].get_card_value()
                            self.current_highhand.set_high_hand(6,high_card_value,-1,[])
                        else:
                            #Check for three of a kind
                            is_three_of_a_kind,card_num = utils.check_three_of_a_kind(all_cards)
                            if is_three_of_a_kind:
                                high_card_value = all_cards[card_num].get_card_value()
                                second_card_value = -1
                                remaining_card_values = []
                                if card_num > 1:
                                    second_card_value = all_cards[0].get_card_value()
                                    remaining_card_values.append(all_cards[1].get_card_value())
                                elif card_num == 1:
                                    second_card_value = all_cards[0].get_card_value()
                                    remaining_card_values.append(all_cards[4].get_card_value())
                                elif card_num == 0:
                                    second_card_value = all_cards[3].get_card_value()
                                    remaining_card_values.append(all_cards[4].get_card_value())
                                self.current_highhand.set_high_hand(5,high_card_value,second_card_value,remaining_card_values)
                            else:
                                #Check for two pairs
                                is_two_pairs, high_card_value, second_card_value, remaining_card_values = utils.check_two_pairs(all_cards)
                                if is_two_pairs:
                                    self.current_highhand.set_high_hand(4,high_card_value,second_card_value,remaining_card_values)
                                else:
                                    #Check for one pair
                                    is_one_pair,card_num = utils.check_one_pair(all_cards)
                                    if is_one_pair:
                                        high_card_value = all_cards[card_num].get_card_value()
                                        second_card_value = -1
                                        remaining_card_values = []
                                        if card_num > 2:
                                            second_card_value = all_cards[0].get_card_value()
                                            remaining_card_values.append(all_cards[1].get_card_value())
                                            remaining_card_values.append(all_cards[2].get_card_value())
                                        elif card_num == 2:
                                            second_card_value = all_cards[0].get_card_value()
                                            remaining_card_values.append(all_cards[1].get_card_value())
                                            remaining_card_values.append(all_cards[4].get_card_value())                                            
                                        elif card_num == 1:
                                            second_card_value = all_cards[0].get_card_value()
                                            remaining_card_values.append(all_cards[3].get_card_value())
                                            remaining_card_values.append(all_cards[4].get_card_value())
                                        elif card_num == 0:
                                            second_card_value = all_cards[2].get_card_value()
                                            remaining_card_values.append(all_cards[3].get_card_value())
                                            remaining_card_values.append(all_cards[4].get_card_value())
                                        else:
                                            pass
                                        self.current_highhand.set_high_hand(3,high_card_value,second_card_value,remaining_card_values)
                                    else:
                                        #Check for high card
                                        high_card_value, second_card_value, remaining_card_values = utils.get_high_cards(all_cards)
                                        self.current_highhand.set_high_hand(2,high_card_value,second_card_value,remaining_card_values)

        #self.current_highhand.get_high_hand()

    def get_high_hand_object(self):
        return self.current_highhand



