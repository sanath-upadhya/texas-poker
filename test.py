import card
import utils as u
import table
import player


number_of_players = int(input("Enter the number of players: "))

table1 = table.Table() 

table1.assign_table_cards()

for i in range(0,number_of_players):
    player1 = player.Player()
    player1.join_table(table1)
    table1.add_player_to_table(player1)

u.assign_player_cards(table1)

u.print_cards_table(table1)

for player1 in table1.get_players():
    player1.get_highest_hand()


