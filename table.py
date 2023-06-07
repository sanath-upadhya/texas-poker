import card

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
