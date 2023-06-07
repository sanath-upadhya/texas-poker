
def assign_player_cards(table1):
    for player in table1.get_players():
        player.assign_cards()

def print_cards_table(table1):
    print("Cards used are:")
    for card in table1.get_current_cards():
        print_cards(card)

def print_card_player(player1):
    card1,card2 = player1.get_current_cards()
    print_cards(card1)
    print_cards(card2)

def print_cards(card):
    print("Value is " + str(card.get_card_value()) + " of " + get_type(card.get_card_type()))

def get_type(int_type):
    if int_type == 1:
        return "diamond"
    elif int_type == 2:
        return "heart"
    elif int_type == 3:
        return "spade"
    elif int_type == 4:
        return "club"
    

def check_four_of_a_kind(all_cards):
    if len(all_cards) < 4:
        return False
    for i in range(0, len(all_cards) - 3):
        if (all_cards[i].get_card_value() == all_cards[i+1].get_card_value()) and (all_cards[i+1].get_card_value() == all_cards[i+2].get_card_value()) and (all_cards[i+2].get_card_value() == all_cards[i+3].get_card_value()):
            return True
    return False

def check_flush(all_cards):
    spade_count = 0
    diamond_count = 0
    heart_count = 0
    club_count = 0
    for card in all_cards:
        if card.get_card_type() == 1:
            diamond_count += 1
        elif card.get_card_type() == 2:
            heart_count += 1
        elif card.get_card_type() == 3:
            spade_count += 1
        elif card.get_card_type() == 4:
            club_count += 1
    
    if spade_count>=5 or club_count >=5 or heart_count >= 5 or diamond_count >= 5:
        return True
    else:
        return False

def check_straight(all_cards):
    for i in range(0, len(all_cards) - 4):
        if (all_cards[i].get_card_value() == all_cards[i+1].get_card_value() + 1) and (all_cards[i+1].get_card_value() == all_cards[i+2].get_card_value() + 1) and (all_cards[i+2].get_card_value() == all_cards[i+3].get_card_value() + 1) and (all_cards[i+3].get_card_value() == all_cards[i+4].get_card_value() + 1):
            return True,i
    return False,-1

def check_straight_flush(all_cards):
    is_straight,i=check_straight(all_cards)
    if is_straight:
        if (all_cards[i].get_card_type() == all_cards[i+1].get_card_type()) and (all_cards[i+1].get_card_type() == all_cards[i+2].get_card_type()) and (all_cards[i+2].get_card_type() == all_cards[i+3].get_card_type()) and (all_cards[i+3].get_card_type() == all_cards[i+4].get_card_type()):
            return True
        else:
            return False
    else:
        return False
    
def check_three_of_a_kind(all_cards):
    for i in range(0, len(all_cards) - 2):
        if (all_cards[i].get_card_value() == all_cards[i+1].get_card_value()) and (all_cards[i+1].get_card_value() == all_cards[i+2].get_card_value()):
            return True,i
        
    return False,-1

def check_one_pair(all_cards):
    for i in range(0, len(all_cards) - 1):
        if (all_cards[i].get_card_value() == all_cards[i+1].get_card_value()):
            return True,i
    
    return False,-1

def check_full_house(all_cards):
    three_of_kind,i = check_three_of_a_kind(all_cards)

    if three_of_kind:
        new_cards = []
        for j in range(0,len(all_cards)):
            if j == i or j == i+1 or j == i+2:
                continue
            else:
                new_cards.append(all_cards[j])

        one_pair,k = check_one_pair(new_cards)
        if one_pair:
            return True
        else:
            return False
        
    else:
        return False
    
def check_two_pairs(all_cards):
    one_pair,i=check_one_pair(all_cards)
    if one_pair:
        new_cards = []
        for j in range(0,len(all_cards)):
            if j == i or j == i+1:
                continue
            else:
                new_cards.append(all_cards[j])

        second_pair,k = check_one_pair(new_cards)
        if second_pair:
            return True
        else:
            return False

    else:
        return False




        


