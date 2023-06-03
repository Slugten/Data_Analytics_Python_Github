# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
first_scorer = 'Ruud Gullit'            #Name of player that scored the first goal
second_scorer = 'Marco van Basten'      #Name of player that scored the second goal

goal_0 = 32     #Time played on first goal
goal_1 = 54     #Time played on second goal

scorers = first_scorer +' ' + str(goal_0) + ',' + ' ' + second_scorer + ' ' + str(goal_1)
report = f'{first_scorer} scored in the {goal_0}nd minute\n{second_scorer} scored in the {goal_1}th minute'

player = 'Ronald Koeman'                            #Name of chosen player
name_1 = 'Ronald'                                   #First name we want to find and store later on
name_2 = 'Koeman'                                   #Last name we want to find and store later on

start_index_first_name = player.find(name_1)        #Find the start index of players name
first_name = player[:6]                             #Slice to get the first name of player

start_index_last_name = player.find(name_2)             #Start index of last name
total_length_name = len(player)                         #Total length of name
last_name_len = player[7:len(name_2)]

name_split = player.split()                         #Splits player in to two, on the space
first_initial = name_split[0][0] + "."
last_name = " ".join(name_split[1])             
name_short = f"{first_initial} + {last_name}"       #Joins first initial "R" with last name "Koeman"

X = len(first_name)

chant = (first_name+'!') * X                        #6x Ronald!
last_character_chant = chant[-1]                    #defines the last character of chant

good_chant = last_character_chant != " "            #Compare last character of chant with space

print(scorers)
print(report)
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
