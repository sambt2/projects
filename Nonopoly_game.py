
# This is a program to provide a text-based Nonopoly game, which is similar to monopoly but not quite the same. 
# It provides general functionality, but (a) the buying houses function is incomplete, (b) you can't trade properties with other players yet, and (c) there is no bankruptcy mechanism yet. 


# This section sets up the starting parameters.


import random

space = 0

money = 1500

player_name = ["nobody", "Alice", "Bob", "Charlie", "David", "Ellie", "Fred"]

player_money = [0, 1500, 1500, 1500, 1500, 1500, 1500]

player_type = ["Null", "Human", "Computer", "Computer", "Computer", "Computer", "Computer"]

player_position = [0, 0, 0, 0, 0, 0, 0, 0]

space_name = ["Go", "Old Kent Road", "Community Chest", "Whitechapel Road", "Income Tax", "Kings Cross Station", "The Angel Islington", "Chance", "Euston Road", "Pentonville Road", "Visiting Prison",
              "Pall Mall", "Electric Company", "Whitehall", "Northumberland Avenue", "Marylebone Station", "Bow Street", "Community Chest", "Marlborough Street", "Vine Street", "Free Parking", "The Strand", "Chance", "Fleet Street", "Trafalgar Sqaure", "Fenchurch St Station", "Leicester Square", "Coventry Street", "Water Works", "Piccadilly", "Go to Jail",
              "Regent Street", "Oxford Street", "Community Chest", "Bond Street", "Liverpool St Station", "Chance", "Park Lane", "Sales Tax", "Mayfair"]

#property_type follows a special code: 0 means it cannot be bought, 1 are utilities, 2 are stations, 3 are browns, 4 are light blues, 5 are pinks, etc.
property_type = [0, 3, 0, 3, 0, 2, 4, 0, 4, 4, 0, 5, 1, 5, 5, 2, 6, 0, 6, 6, 0, 7, 0, 7, 7, 2, 8, 8, 1, 8, 0, 9, 9, 0, 9, 2, 0, 10, 0, 10, 0]

property_price = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180, 0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0,
                   300, 300, 0, 320, 200, 0, 350, 0, 400]

# property_owner follows a specific code: -1 means the space cannot be bought, 0 means nobody owns it, a number means the player of that number owns it.  
property_owner = [-1, 0, -1, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0]

#test_property_owner = [-1, 1, -1, 1, -1, 0, 1, -1, 1, 1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0]

# property_owner = test_property_owner (these two lines are a testing mechanism for the buying houses code: currently commented out)

starting_roll = [0]

rent = [0] * 40
number_of_houses = [0] * 40

## RENT TABLE. [rent with no houses, 1 house, 2 houses, 3 houses, 4 houses, hotel, house cost]

rent[1] = [2, 10, 30, 90, 160, 250, 50]
rent[3] = [4, 20, 60, 180, 320, 450, 50]
rent[6] = [6, 30, 90, 270, 400, 550, 50]
rent[8] = [6, 30, 90, 270, 400, 550, 50]
rent[9] = [8, 40, 100, 300, 450, 600, 50]
rent[11] = [10, 50, 150, 450, 625, 750, 100]
rent[13] = [10, 50, 150, 450, 625, 750, 100]
rent[14] = [12, 60, 180, 500, 700, 900, 100]
rent[16] = [14, 70, 200, 550, 750, 950, 100]
rent[18] = [14, 70, 200, 550, 750, 950, 100]
rent[19] = [16, 80, 220, 600, 800, 1000, 100]
rent[21] = [18, 90, 250, 700, 875, 1050, 150]
rent[23] = [18, 90, 250, 700, 875, 1050, 150]
rent[24] = [20, 100, 300, 750, 925, 1100, 150]
rent[26] = [22, 110, 330, 800, 975, 1150, 150]
rent[28] = [22, 110, 330, 800, 975, 1150, 150]
rent[29] = [22, 120, 360, 850, 1025, 1200, 150]
rent[31] = [26, 130, 390, 900, 1100, 1275, 200]
rent[33] = [26, 130, 390, 900, 1100, 1275, 200]
rent[34] = [28, 150, 450, 1000, 1200, 1400, 200]
rent[37] = [35, 175, 500, 1100, 1300, 1500, 200]
rent[39] = [50, 200, 600, 1400, 1700, 2000, 200]

# This parameter counts who has which sets. 0 means nobody owns that set. The sets correspond to the colours in the set_colour parameter immediately below.
set_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

set_colour = [0, 0, "BROWN", "BLUE", "PINK", "ORANGE", "RED", "YELLOW", "GREEN", "PURPLE"]

set_house_price = [0, 0, 50, 50, 100, 100, 150, 150, 200, 200]

house_counter = [0] * 40

for x in range(0,7):
    set_counter[x] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
## the sets are, in order, Utilities, Stations, Browns,  Blues, Pinks, Oranges, Reds, Yellows, Greens, Purples


#This section sets up the game: allows the user to specify the number of players, and their names. 

print ("Welcome to Sam's Nonopoly game!")


print()

human_players = input("How many human players are playing? (Max of 6 players total) :")

while human_players not in ['1', '2', '3', '4', '5', '6']:
    print ("That is not a valid response")
    human_players = input("Please enter an integer between 1 and 6:")

human_players = int(human_players)

for x in range (1, human_players+1):
    print ("Player number", x, ":")
    player_name[x] = str(input("What is your name? "))
    player_type[x] = "human"

computer_players = input("How many computer players are playing? Max of 6 players total :")
while computer_players not in ['0','1', '2', '3', '4', '5'] or int(computer_players) + human_players > 6:
    print ("That is not a valid reponse - consider if you've requested more than 6 players")
    computer_players = input("How many computer players are playing? Max of 6 players total :")

computer_players = int(computer_players)
number_of_players = human_players + computer_players

print ("")

for n in range (human_players+1, computer_players+2):
    print (player_name[n], "is a computer player.")


print ("")
print ("***************************")
print ("")
print ("Rolling to see who starts....")
print ("")

for n in range (1, number_of_players+1):
    a = random.randint (1,6)
    b = random.randint (1,6)
    starting_roll.append (a + b)
    print (player_name[n], " rolls ", starting_roll[n], "to start.")

n = starting_roll.index(max(starting_roll))
        
print(player_name[n], " has the highest roll and will start")
print ("")
print ("")
print ("Let the game begin!")
print ("")
print ("***************************")
print ("")


#These are the central instructions for how to administer turns. 

game_ended = False

while game_ended == False:
    print ("")

    if player_type[n] == "Computer":
        print ("It is", player_name[n], "'s turn.")
        print (player_name[n], "has £", player_money[n])
        a = random.randint (1,6)
        b = random.randint (1,6)
        roll = a + b
        player_position[n] = player_position[n] + roll
        if player_position[n] > 39:
            player_position[n] = player_position[n] - 40
            print (player_name[n], "passed Go and collects £200.")
            player_money[n] = player_money[n] + 200
        print (player_name[n], "rolled", roll, "and moves from", space_name[player_position[n] - roll], "to", space_name[player_position[n]], ".")

        if property_owner[player_position[n]] == -1:
            if player_position[n] == 4:
                player_money[n] -= 200
                print (player_name[n], "pays £200 income tax, and now has £", player_money[n])

            elif player_position[n] == 38:
                player_money[n] -= 100
                print (player_name[n], "pays £100 sales tax, and now has £", player_money[n])

            else:
                pass
        
        elif property_owner[player_position[n]] == 0:
            print (space_name[player_position[n]],"is owned by nobody and costs £", property_price[player_position[n]], ".")
            if player_money[n] > property_price[player_position[n]]:
                print (player_name[n], "buys", space_name[player_position[n]])
                player_money[n] = player_money[n] - property_price[player_position[n]]
                property_owner[player_position[n]] = n
                set_counter[n][property_type[player_position[n]]-1] += 1
                print (player_name[n], "now has £", player_money[n])
            else:
                print (player_name[n], "cannot afford to buy this.")

        elif property_owner[player_position[n]] == n:
            print (player_name[n], "already owns this.")
          
        elif property_owner[player_position[n]] > 0:
            print ("This property belongs to", player_name[property_owner[player_position[n]]])

                    ## instructions for computers paying rent on utilities
            if player_position[n] == 12 or player_position[n] == 28:
                if set_counter[property_owner[player_position[n]]][0] == 1:                            
                     current_rent = 4 * roll
                if set_counter[property_owner[player_position[n]]][0] == 2:
                    current_rent = 10 * roll
                                
            ####  instructions for computers paying rent on stations
            elif player_position[n] == 5 or player_position[n] == 15 or player_position[n] == 25 or player_position[n] == 35:
                if set_counter[property_owner[player_position[n]]][1] == 1:
                    current_rent = 25
                if set_counter[property_owner[player_position[n]]][1] == 2:
                    current_rent = 50
                if set_counter[property_owner[player_position[n]]][1] == 3:
                    current_rent = 100
                if set_counter[property_owner[player_position[n]]][1] == 4:
                    current_rent = 200

            ## instructions for computers paying rent on standard properties   
            else:
                current_rent = rent[player_position[n]][house_counter[player_position[n]]]
                          
            print (player_name[n], "must pay £", current_rent, "in rent.")
            player_money[n] = player_money[n] - current_rent
            player_money[property_owner[player_position[n]]] = player_money[property_owner[player_position[n]]] + current_rent
            print (player_name[n], "now has £", player_money[n], ",", player_name[property_owner[player_position[n]]], "now has £", player_money[property_owner[player_position[n]]], ".")

        print ("End of", player_name[n], "'s turn.")
        n = n + 1
        if n > number_of_players:
            n = n - number_of_players

## These are the instructions for human players
    else:
        print ("****************")
        print ("")
        print ("It is your turn,", player_name[n], ".")
        print ("")
        print ("You have £", player_money[n], "and you are currently on", space_name[player_position[n]],".")
        print ("")
        choice = input("What are your instructions? (r = roll)(d = display properties)(b = buy houses and hotels)(q = quit)")
        print ("")
        while choice not in ['r', 'd', 'b', 'q']:
            print ("That is not a valid choice.")
            choice = input("What are your instructions? (r = roll)(d = display properties)(b = buy houses and hotels)")
        if choice == 'q':
            game_ended = True

        if choice == "d":
            print (player_name[n],", you have the following properties:")
            for x in range (0, 40):
                if property_owner[x] == n:
                    if property_type [x] == 1 or property_type [x] == 2:
                        print (space_name[x])
                    else:
                        print (space_name[x], "with", house_counter[x], "houses.")

        #This section deals with humans buying houses
        if choice == "b":
            sets_possible = False
            if n == property_owner[1] == property_owner[3]:
                set_counter [2] = n
                sets_possible = True
            if n == property_owner[6] == property_owner[8] == property_owner[9]:
                set_counter [3] = n
                sets_possible = True
            if n == property_owner[11] == property_owner[13] == property_owner[14]:
                set_counter [4] = n
                sets_possible = True
            if n == property_owner[16] == property_owner[18] == property_owner[19]:
                set_counter [5] = n
                sets_possible = True
            if n == property_owner[21] == property_owner[23] == property_owner[24]:
                set_counter [6] = n
                sets_possible = True
            if n == property_owner[26] == property_owner[28] == property_owner[29]:
                set_counter [7] = n
                sets_possible = True
            if n == property_owner[31] == property_owner[33] == property_owner[34]:
                set_counter [8] = n
                sets_possible = True
            if n == property_owner[37] == property_owner[39]:
                set_counter [9] = n
                sets_possible = True

            
            if sets_possible == True:
                sets_yes = True
                for a in range (2, 9):
                    if set_counter[a] == n:
                        print ("You can build houses on", set_colour[a])
                        print("Houses on", set_colour[a], "cost £", set_house_price[a], "each.")
                        print ("")
                set_choice = int(input("Which set would you like to buy on? 1 = Browns, 2 = Blues, 3 = Pinks, 4 = Oranges, 5 = Reds, 6 = Yellows, 7 = Greens, 8 = Purples, 9 = None:" ))
                if set_choice == 9:
                    sets_yes = False
                while set_choice not in [1,2,3,4,5,6,7,8,9]:
                    print ("That is not a valid choice")
                    set_choice = int(input("Which set would you like to buy on? "))
                if set_choice in [1,2,3,4,5,6,7,8]:
                    while set_counter[set_choice + 1] is not n and set_choice is not 9:
                        print ("You don't own that set.")
                        set_choice = int(input("Which set would you like to buy on? "))
                        if set_choice == 9:
                            sets_yes = False
                if sets_yes == True:
                    print("Houses on ", set_colour[set_choice + 1], "cost £", set_house_price[set_choice + 1], "each. How many would you like to buy?")
                    house_request = input()
                    while house_request not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
                        print ("That is not a valid number.")
                        print("Houses on ", set_colour[set_choice + 1], "cost £", set_house_price[set_choice + 1], "each. How many would you like to buy?")    
                        house_request = input()
                    print ("This costs £", house_request * set_house_price[set_choice + 1])


            if sets_possible == False:
                print ("You don't have any full sets yet.")
                pass
                
            
        if choice == "r":
            a = random.randint (1,6)
            b = random.randint (1,6)
            roll = a + b
            player_position[n] = player_position[n] + roll
            if player_position[n] > 39:
                player_position[n] = player_position[n] - 40
                print ("You passed Go and collect £200.")
                player_money[n] = player_money[n] + 200
            print ("You rolled", roll, "and move from", space_name[player_position[n] - roll], " to ", space_name[player_position[n]], ".")

            if property_owner[player_position[n]] == -1:
                if player_position[n] == 4:
                    player_money[n] -= 200
                    print ("You pay £200 income tax. You now have", player_money[n])

                elif player_position[n] == 38:
                    player_money[n] -= 100
                    print ("You pay £100 sales tax. You now have", player_money[n])
                else:
                    pass
            elif property_owner[player_position[n]] == 0:
                print (space_name[player_position[n]],"is owned by nobody and costs £", property_price[player_position[n]], ".")
                if player_money[n] < property_price[player_position[n]]:
                    print ("You cannot afford this.")
                else:
                    choice = input("Would you like to buy this property? (y/n)")    
                    while choice not in ['y', 'n']:
                        print ("That is not a valid response.")
                        choice = input("Would you like to buy this property? (y/n)") 

                    if choice == "y":
                        print (player_name[n], "buys", space_name[player_position[n]])
                        player_money[n] = player_money[n] - property_price[player_position[n]]
                        property_owner[player_position[n]] = n
                        set_counter[n][property_type[player_position[n]]-1] += 1
                        print (player_name[n], "now has £", player_money[n])
                    else:
                        pass

            elif property_owner[player_position[n]] == n:
                print ("You already own this.")
                
            elif property_owner[player_position[n]] > 0:
                print ("This property belongs to", player_name[property_owner[player_position[n]]])
                
                    ## instructions for humans to pay rent on utilities
                if player_position[n] == 12 or player_position[n] == 28:
                    if set_counter[property_owner[player_position[n]]][0] == 1:                            
                         current_rent = 4 * roll
                    if set_counter[property_owner[player_position[n]]][0] == 2:
                        current_rent = 10 * roll
                                
            ####  instructions for humans to pay rent on stations
                elif player_position[n] == 5 or player_position[n] == 15 or player_position[n] == 25 or player_position[n] == 35:
                    if set_counter[property_owner[player_position[n]]][1] == 1:
                        current_rent = 25
                    if set_counter[property_owner[player_position[n]]][1] == 2:
                       current_rent = 50
                    if set_counter[property_owner[player_position[n]]][1] == 3:
                        current_rent = 100
                    if set_counter[property_owner[player_position[n]]][1] == 4:
                        current_rent = 200

            ## instructions for humans to pay rent on properties     
                else:
                    current_rent = rent[player_position[n]][house_counter[player_position[n]]]
                
                print (player_name[n], "must pay £", current_rent)
                player_money[n] -= current_rent
                player_money[property_owner[player_position[n]]] += current_rent
                print (player_name[n], "now has £", player_money[n], ",", player_name[property_owner[player_position[n]]], "now has £", player_money[property_owner[player_position[n]]], ".")

            print ("End of", player_name[n], "'s turn.")
            n = n + 1
            if n > number_of_players:
               n = n - number_of_players           
        else:
            pass
                       

    
