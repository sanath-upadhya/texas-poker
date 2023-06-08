
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
            second_high_card_value = -1
            if i == 0:
                second_high_card_value = all_cards[4].get_card_value()
            else:
                second_high_card_value = all_cards[i-1].get_card_value()
            return True,all_cards[i].get_card_calue(),second_high_card_value
    return False,-1,-1

def get_high_hands(all_cards, card_type):
    high_hand_value = -1
    second_high_hand_value = -1
    remaining_hands_value = []
    for card in all_cards:
        if card.get_card_type() == card_type and high_hand_value == -1:
            high_hand_value = card.get_card_value()
        elif card.get_card_type() == card_type and second_high_hand_value == -1:
            second_high_hand_value = card.get_card_value()
        elif card.get_card_type() == card_type and len(remaining_hands_value) < 3:
            remaining_hands_value.append(card.get_card_value())
        else:
            pass
    
    return high_hand_value, second_high_hand_value, remaining_hands_value

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
    high_card_value = -1
    second_high_card_value = -1
    remaining_card_value = []
    if diamond_count >= 5:
        high_card_value,second_high_card_value,remaining_card_value = get_high_hands(all_cards, 1)
    elif heart_count >= 5:
        high_card_value,second_high_card_value,remaining_card_value = get_high_hands(all_cards, 2)
    elif spade_count >= 5:
        high_card_value,second_high_card_value,remaining_card_value = get_high_hands(all_cards, 3)
    elif club_count >= 5:
        high_card_value,second_high_card_value,remaining_card_value = get_high_hands(all_cards, 4) 

    if spade_count>=5 or club_count >=5 or heart_count >= 5 or diamond_count >= 5:
        return True, high_card_value, second_high_card_value, remaining_card_value
    else:
        return False, high_card_value, second_high_card_value, remaining_card_value

def check_straight(all_cards):
    for i in range(0, len(all_cards) - 4):
        if (all_cards[i].get_card_value() == all_cards[i+1].get_card_value() + 1) and (all_cards[i+1].get_card_value() == all_cards[i+2].get_card_value() + 1) and (all_cards[i+2].get_card_value() == all_cards[i+3].get_card_value() + 1) and (all_cards[i+3].get_card_value() == all_cards[i+4].get_card_value() + 1):
            return True,i
    return False,-1

def check_straight_flush(all_cards):
    is_straight,i=check_straight(all_cards)
    if is_straight:
        if (all_cards[i].get_card_type() == all_cards[i+1].get_card_type()) and (all_cards[i+1].get_card_type() == all_cards[i+2].get_card_type()) and (all_cards[i+2].get_card_type() == all_cards[i+3].get_card_type()) and (all_cards[i+3].get_card_type() == all_cards[i+4].get_card_type()):
            return True,i
        else:
            return False,-1
    else:
        return False,-1
    
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
        high_card_value = all_cards[i].get_card_value()
        new_cards = []
        for j in range(0,len(all_cards)):
            if j == i or j == i+1 or j == i+2:
                continue
            else:
                new_cards.append(all_cards[j])

        one_pair,k = check_one_pair(new_cards)
        if one_pair:
            second_high_card_value = new_cards[k].get_card_value()
            remaining_cards = []
            return True,high_card_value,second_high_card_value,remaining_cards
        else:
            return False,-1,-1,remaining_cards
        
    else:
        return False,-1,-1,[]
    
def check_two_pairs(all_cards):
    one_pair,i=check_one_pair(all_cards)
    if one_pair:
        high_card_value = all_cards[i].get_card_value()
        new_cards = []
        for j in range(0,len(all_cards)):
            if j == i or j == i+1:
                continue
            else:
                new_cards.append(all_cards[j])

        second_pair,k = check_one_pair(new_cards)
        if second_pair:
            second_high_card_value = new_cards[k].get_card_value()
            remaining_cards = []
            if k == 0:
                remaining_cards.append(new_cards[2].get_card_value())
            else:
                remaining_cards.append(new_cards[0].get_card_value())
            return True,high_card_value,second_high_card_value,remaining_cards
        else:
            return False,-1,-1,[]

    else:
        return False,-1,-1,[]
    
def get_high_cards(all_cards):
    high_card_value = -1
    second_high_card_value = -1
    remaining_cards = []

    for card in all_cards:
        if high_card_value == -1:
            high_card_value = card.get_card_value()
        elif second_high_card_value == -1:
            second_high_card_value = card.get_card_value()
        elif len(remaining_cards) < 3:
            remaining_cards.append(card.get_card_value())
        else:
            pass
    
    return high_card_value, second_high_card_value, remaining_cards




        


