# =====================================================================
#   Noughts and Crosses
#   In Python, by Sheraz, 11-12 Dec 2024, update March 2025
# =====================================================================

# =====================================================================
#   Show results, used for spacing
# =====================================================================
def show_results (Display_Value): 
    space = """

    ------------------------------------------------------------------------

    """
    display_result = space + Display_Value
    return display_result
   
# =====================================================================
#   Ask the user for the slot
#   Convert from visual slot location to array position
# ===================================================================== 
def ask_for_slot(data_grid):
    
    player_slot = input("Select slot ")

    player_slot = player_slot.capitalize()
    player_slot_grid = int()
    
    #convert slot to grid placement
    if player_slot == "A1":
        player_slot_grid = 0
    elif player_slot == "B1":
        player_slot_grid = 1
    elif player_slot == "C1":
        player_slot_grid = 2
    elif player_slot == "A2":
        player_slot_grid = 3    
    elif player_slot == "B2":
        player_slot_grid = 4  
    elif player_slot == "C2":
        player_slot_grid = 5  
    elif player_slot == "A3":
        player_slot_grid = 6  
    elif player_slot == "B3":
        player_slot_grid = 7  
    elif player_slot == "C3":
        player_slot_grid = 8
        
        

        
        
        
    return player_slot_grid


# =====================================================================
#   Ask user for the value
# =====================================================================
def ask_for_value():
    player_value = input(" X ---- O ")
    #check value choosen being X or O
    return player_value.upper()

# =====================================================================
#   update the grid with the input value
# =====================================================================
def update_grid(data_grid, player_slot, player_value):
    
    #add checks for the submitted values
    #print (data_grid)
    #print (player_slot)
    #print (player_value)
    
    new_player_slot = int(player_slot)    
    data_grid[new_player_slot] = player_value
    #print (data_grid[new_player_slot], " - UPDATED ")
    #print (data_grid)
    return data_grid
    
# =====================================================================
#   Show the grid on display
# =====================================================================
def show_grid(data_grid):
    
    #print ("SENT FOR PREVIEW BOX")
    #print(data_grid)
    #for x in data_grid:
        #print(x)    
    #print ("-------------------")  

    row = 0
    col = 0
    i = 0
    print("    A   B   C")
    print("") 
    
    while i < len(data_grid) :
        while row <= 2 :
            if i < 7 :
                print(row+1 , " ", data_grid[i], " ", data_grid[i+1], " ", data_grid[i+2])
                i = i +3
                row +=1
    return

# =====================================================================
#  check if slot already used
#  havent coded yet
# =====================================================================
def check_slot_usage():
    
    return

# =====================================================================
#  Check if user has won
# =====================================================================
def check_if_won():
    
    game_status = 0
    #print(data_grid)
    
    if data_grid[0] == data_grid[1] == data_grid[2] != "-":
        # top row
        print("Winner " + data_grid[1] + " has won.")
    elif data_grid[3] == data_grid[4] == data_grid[5] != "-":
        # 2ABC
        print("Winner " + data_grid[4] + " has won.. 2ABC")
    elif data_grid[6] == data_grid[7] == data_grid[8] != "-":
        # low row
        print("Winner " + data_grid[7] + " has won...")
    elif data_grid[0] == data_grid[3] == data_grid[6] != "-":
        # A1, A2, A3
        print("Winner " + data_grid[3] + " has won.... A123")
    elif data_grid[1] == data_grid[4] == data_grid[7] != "-":
        # low row
        print("Winner " + data_grid[4] + " has won.....")
    elif data_grid[2] == data_grid[5] == data_grid[8] != "-":
        # mid row
        print("Winner " + data_grid[5] + " has won......")
    elif data_grid[0] == data_grid[4] == data_grid[8] != "-":
        # A1, B2, C3
        print("Winner " + data_grid[4] + " has won....... A1, B2, C3")
    elif data_grid[2] == data_grid[4] == data_grid[6] != "-":
        # mid row
        print("Winner " + data_grid[4] + " has won........")
    #else :
        #print("No Winner Check")
    
    return game_status



# =====================================================================
#   Core data fields
# =====================================================================

#check if slot is correct
check_slot_options = ["a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"]
introduction = "Noughts and Crosses"
data_grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player1 = "Superman"
player2 = "Batman"
game_loop = 0
print(show_results(""))
show_grid(data_grid)
print(show_results(""))

def check_slot_if_free(data_grid, the_slot):
    
    if data_grid[the_slot] == "-":
        #print("FREE")
        free = True
    elif data_grid[the_slot] != "-":
        #print("NOT FREE")
        free = False
    return free

def check_if_value_correct(the_value):
    
    if the_value == "X" :
        #print("X Found")
        value_okay = True
    elif the_value == "O" :
        #print("O Found")
        value_okay = True
    else :
        #print(the_value + " Found")
        value_okay = False
    return value_okay

if game_loop >=5:
        check_if_won()
        
while game_loop <=8 :
    #print(game_loop)
    
    if game_loop >=5:
        check_if_won()
  
    the_slot = ask_for_slot(data_grid)
    
    if check_slot_if_free(data_grid, the_slot) == True :
        
        the_value = ask_for_value()
        if check_if_value_correct(the_value) == True :
            print(show_results(""))
            update_grid(data_grid, the_slot, the_value)
            show_grid(data_grid)
            print(show_results(""))
            game_loop = game_loop + 1
        else :
            print(show_results(""))
            show_grid(data_grid)
            print(show_results(""))
            print("The Value entered was incorrect, only X and O are allowed")
            game_loop = game_loop
            
    else :
        print(show_results(""))
        show_grid(data_grid)
        print(show_results(""))
        print("The slot select was not free, please select another")
        game_loop = game_loop
