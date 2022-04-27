#Basic colour combinations for design, arts, and crafts

color_list = {1: 'RED', 2: 'BLUE', 3: 'YELLOW'}
combo_type = {1: 'COMPLEMENTARY', 2: 'TRIADIC'}


#Pick a colour
print('List of Colours')
for key, value in color_list.items():
    print(key, ') ', value)
user_color = int(input('Select a color from the list above: '))

if(user_color == 1 or user_color == 2 or user_color == 3):
    #Pick a combination 
    print('\nList of combination types')
    for key, value in combo_type.items():
        print(key, ') ', value)
    user_combo = int(input('Select a combination from the list above: '))
    
    #catch errors
    if (0<user_combo<4 or 0<user_combo<3):
        print(f'\nYou have selected the color {color_list[user_color]} and the {combo_type[user_combo]} combination type.')
        
        print('Suggested Matching Colours: ')
        if ((user_color == 1) and (user_combo == 1)): #red color, complementary combo
            print('Green')

        elif ((user_color == 1) and (user_combo == 2)): #red color, triadic combo: 
            print('Yellow, Blue')

        elif ((user_color == 2) and (user_combo == 1)): #blue color, complementary combo
            print('Orange')
    
        elif ((user_color == 2) and (user_combo == 2)): #blue color, triadic combo
            print('Red, Yellow')
    
        elif ((user_color == 3) and (user_combo == 1)): #yellow color, complementary combo
            print('Purple')
    
        elif ((user_color == 3) and (user_combo == 2)): #yellow color, triadic combo
            print('Red, Blue')

        else: 
            print('The color / combination you selected does not exist. Please try again.')
        
    else: 
        print('Error: Please enter a valid combination selection.')
        print('Ensure your input is a number.')
else: 
    print('Error: Please enter a valid colour selection.')
    print('Ensure your input is a number.')
    
exit = input("\n\nPress any key to exit.")

#Source of colour wheel used for color combinations --> https://brightside.me/creativity-home/the-ultimate-color-combinations-cheat-sheet-92405/
