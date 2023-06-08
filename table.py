import card
import utils

class Table:
    value_of_current_pot: int
    present_cards: list
    present_players: list
    card1: card.Card
    card2: card.Card
    card3: card.Card
    card4: card.Card
    card5: card.Card
    current_round:int
    current_big_blind_player = None
    current_small_blind_player = None
    number_of_players: int

    def __init__(self):
        self.value_of_current_pot = 0
        self.present_cards = []
        self.present_players = []
        self.current_round = 0
        self.number_of_players = 0

    def assign_table_cards(self):
        self.card1 = card.Card(self.present_cards)
        self.present_cards.append(self.card1)
        self.card2 = card.Card(self.present_cards)
        self.present_cards.append(self.card2)
        self.card3 = card.Card(self.present_cards)
        self.present_cards.append(self.card3)
        self.card4 = card.Card(self.present_cards)
        self.present_cards.append(self.card4)
        self.card5 = card.Card(self.present_cards)
        self.present_cards.append(self.card5)

    def get_current_cards(self):
        return self.present_cards
    
    def add_player_to_table(self, player):
        self.present_players.append(player)

    def get_players(self):
        return self.present_players
    
    def start_round(self):
        self.current_round += 1
        self.value_of_current_pot = 0
        self.current_big_blind_player = self.present_players[(self.current_round-1)%self.number_of_players]
        self.current_small_blind_player = self.present_players[(self.current_round)%self.number_of_players]
        self.card1 = None
        self.card2 = None
        self.card3 = None
        self.card4 = None
        self.card5 = None

    def get_table_cards(self):
        table_cards = []
        table_cards.append(self.card1)
        table_cards.append(self.card2)
        table_cards.append(self.card3)
        table_cards.append(self.card4)
        table_cards.append(self.card5)
        return table_cards
    
    def get_player_winning(self):
        self.present_players.sort(key=lambda x:(x.current_highhand.hand_type*225 + x.current_highhand.high_hand_value*15 + x.current_highhand.second_high_hand_value), reverse=True)

        print("Order of the players card is ")

        for i in range(0,len(self.present_players)-1):
            ith_high_hand = self.present_players[i].get_high_hand_object()
            i_plus_one_high_hand = self.present_players[i+1].get_high_hand_object()
            ith_hand_weighted_value = ith_high_hand.get_hand_type()*225 + ith_high_hand.get_high_hand_value()*15 + ith_high_hand.get_second_high_hand_value()
            i_plus_one_hand_weighted_value = i_plus_one_high_hand.get_hand_type()*225 + i_plus_one_high_hand.get_high_hand_value()*15 + i_plus_one_high_hand.get_second_high_hand_value()
            #Check if both are the same
            if ith_hand_weighted_value == i_plus_one_hand_weighted_value and ith_high_hand.get_remaining_cards() == i_plus_one_high_hand.get_remaining_cards():
                continue
            else:
                break

        #See if the only one player in table has won the round
        if i == 0:
            print("Winner is the player with the following cards:")
            utils.print_card_player(self.present_players[0])

        else:
            #Need to separate out the players based on remaining cards
            pass

        for player in self.present_players:
            current_card1,current_card2 = player.get_current_cards()
            print("Card 1 is "+str(current_card1.get_card_value()) + " "+str(current_card1.get_card_type()))
            print("Card 2 is "+str(current_card2.get_card_value()) + " "+str(current_card2.get_card_type()))
            player.get_high_hand_object().get_high_hand()

