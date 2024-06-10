from player import Player
import time
from events import RandomEvent
import numpy.random as rng
import numpy as np


def dotmove(n):
    dot = "."*n
    loading = (f"{dot}")
    print(loading + "   ", end='\r')
    time.sleep(0.3)


locations =    {"PA": "Drexel University, in Philadelphia, PA",
                "CA": "University of California, Berkeley, in Berkeley, CA",
                "TX": "Texas A&M, in College Station, TX",
                "WA": "University of Washington, in Seattle, WA",
                "IL": "Northwestern University, in Evanston, IL",
                "MA": "Harvard, in Cambridge, MA"}



def main():

    print("\n")
    print("You have received an email from esteemed Nobel Laureate in waiting, Bryan Scott! Let's see what he has to say...")

    print(f'''

                    .----.
        .---------. | == |
        |.-"""""-.| |----|
        ||       || | == |
        ||       || |----|
        |'-.....-'| |::::|
        `"")---(""` |___.|
        /:::::::::::\" _  "
        /:::=======:::\`\`\ 
        `"""""""""""""`  '-'
            
            ''')

    print("\n")
    print("o--------------------------------------------------------------------------------o")
    print("{:.80s} {}".format("| Dear..."+" "*120,"|"))
    print("\n\n\n")
    name = input("What is your name? ")
    name = name.capitalize()
    print("\n")
    print("o--------------------------------------------------------------------------------o")
    print("{:.80s} {}".format(f"| Dear {name},"+" "*120,"|"))
    print("{:.80s} {}".format(f"|           "+" "*150,"|"))
    print("{:.80s} {}".format(f"| We are pleased to announce the next DSFP session..."+" "*120,"|"))
    print("{:.80s} {}".format(f"| will be held at ..."+" "*120,"|"))
    print("\n\n\n")
    loc_key = ""
    while (loc_key not in locations.keys()):
        loc_key = (input(f"Where is the next session? {list(locations.keys())} "))
        loc_key = loc_key.upper()
    location = locations[loc_key.upper()]
    print("\n")
    print("o--------------------------------------------------------------------------------o")
    print("{:.80s} {}".format(f"| Dear {name},"+" "*120,"|"))
    print("{:.80s} {}".format(f"|           "+" "*150,"|"))
    print("{:.80s} {}".format(f"| We are pleased to announce the next DSFP session"+" "*120,"|"))
    print("{:.80s} {}".format(f"| will be held at {location}."+" "*120,"|"))
    print("\n\n\n")
    start_loc = ""
    while ((start_loc != "domestic") and (start_loc != "international")):
        start_loc = input("Make sure you book your... [domestic/international] ")
        start_loc = start_loc.lower()
    print("\n")
    print("o--------------------------------------------------------------------------------o")
    print("{:.80s} {}".format(f"| Dear {name},"+" "*120,"|"))
    print("{:.80s} {}".format(f"|           "+" "*150,"|"))
    print("{:.80s} {}".format(f"| We are pleased to announce the next DSFP session"+" "*120,"|"))
    print("{:.80s} {}".format(f"| will be held at {location}."+" "*120,"|"))
    print("{:.80s} {}".format(f"| Make sure you book your {start_loc} travel quickly so you"+" "*120,"|"))
    print("{:.80s} {}".format(f"| get a big stonking per diem. We'll see you soon!"+" "*120,"|"))
    print("{:.80s} {}".format(f"|           "+" "*150,"|"))
    print("{:.80s} {}".format(f"| Love you! "+" "*150,"|"))
    print("{:.80s} {}".format(f"| Bryan <3 "+" "*150,"|"))
    print("o--------------------------------------------------------------------------------o")
    print("\n\n\n")
    print(f"You're going to {location}! Yippee!!")

    if(start_loc == 'domestic'):
        travel_status = 1.0
        flight_time = 4
    else:
        travel_status = 1.10
        flight_time = 8
    
    you = Player(name=name, travel_status=travel_status)

    print("\n\n\n")

    print("%-------------------------")
    print("TRAVEL DAY")
    for x in range(10):
        dotmove(x)    

    print("\n\n")

    print("""
                    ____
               .---[[__]]----.
              ;-------------.|       ____
              |             ||   .--[[__]]---.
              |             ||  ;-----------.|
              |             ||  |           ||
              |_____________|/  |           ||
                                |___________|/

          """)

    print("You've arrived at your local airport and get to security.")
    for x in range(10):
        dotmove(x)    
    print()
    num = rng.uniform()
    if(you.travel_status * num <= 0.8):
        print("You sped through security no problem!")
    else:
        print("You must have been packing drugs! You've been stopped for a random check.")
        you.mod_focus(5)

    print("\n")
    time.sleep(2)
    print("Phew, through security. Time to check how your flight is doing...")

    num = rng.uniform()
    print()
    if(num <= 0.9):
        print("Everything's on time! Let's head to the lounge to relax...")
    else:
        print("Oh no! There's a delay! Time to talk to the gate agent...")
        you.mod_focus(5)

    for x in range(5):
        dotmove(x)    
    
    print("\n")
    print(f"Finally! It's time to fly. Sit back and relax, it's a {flight_time} hour flight.")

    print("""   
                    __  _
                    \ `/ |
                    \__`!
                    / ,' `-.__________________
                    '-'\_____                LI`-.
                    <____()-=O=O=O=O=O=[]====--)
                        `.___ ,-----,_______...-'
                            /    .'
                            /   .'
                            /  .'         
                            `-'""")

    for x in range(10):
        dotmove(x)


    print('\n\n')

    print("You've landed and made it to the hotel. Probably a good idea to get checked in and head to bed --the session starts at 9am!")

    print("""
          
              .
               ('
               '|
              |'
            [::]
            [::]   _......_
            [::].-'      _.-`.
            [:.'    .-. '-._.-`.
            [/ /\   |  \        `-..
            / / |   `-.'      .-.   `-.
            /  `-'            (   `.    `.
            |           /\      `-._/      \\
            '    .'\   /  `.           _.-'|
            /    /  /   \_.-'        _.':;:/
        .'     \_/             _.-':;_.-'
        /   .-.             _.-' \;.-'
        /   (   \       _..-'     |
        \    `._/  _..-'    .--.  |
        `-.....-'/  _ _  .'    '.|
                | |_|_| |      | \  (o)
            (o)  | |_|_| |      | | (\'/)
            (\'/)/  ''''' |     o|  \;:;
            :;  |        |      |  |/)
             ;: `-.._    /__..--'\.' ;:
                :;  `--' :;   :;

          """)

    choice = 0
    print()
    while ((choice != 1) and (choice != 2)):
        choice = int(input("CHOICE [1,2]: 1. Nah, let's stay up and explore the city! (- Focus, + Fun)\n              2. I can feel my eyes closing already... (+ Focus)\n"))
    if (choice == 1):
        you.mod_focus(-3)
        you.mod_fun(3)
        print()
        print("This place is so cool! Wow, is it midnight already?")
    else:
        you.mod_focus(3)
        print()
        print("It's been a long day. This bed looks super comfy!")

    print('''
          
             .::""-,                      .::""-.
            /::     \                    /::     \\
            |::     |   _..--""""--.._   |::     |
            '\:.__ /  .'              '.  \:.__ /
            ||____|.'                  '.||____|
            ||:.  |                       |:.  |
            ||:.  |                       |:.  |
            ||:.  |                       |:.  |
            ||:.  |  _..---"````````'---. |:.  |
            ||:.  | `                     \:.  |
            ||:.  |: :                .--._.-""-;
            ||:.  |: : _.---``````---/    '.   _.`.
            ||:.  | .-'  _,'```'-...'   _ .-'.'    '-.
            ||:. .-'   .'        '. . '      '.      `'.
            ||: ;.' .`'        _. '`'-.         '.   . ''-._
            ||:. :   '.     .'          '.  . ' ' '.`       '._
            ||:. :    '. .'     .::""-: .''.        ' .   . ' ' :::""-.
            ||:. '     ..' .    /::     \    '.        . '.    /::     \\
            ||:  :  . .'      '.|::     |    _.:---""---.._'   |::     |
            ||.  ;  .:          '\:.__ /   .'              '.   \:.__ /
            ||:  ;  : '.       . ||____|_.'                  '._||____|
            ||:  ;__:   '.   .'  ||:.  |                        ||:.  |
            ||:___| \     '. :   ||:.  |                        ||:.  |
            [[____]  '.     '.-._||:.  |                        ||:.  |
                       '.    :   ||:.  |                        ||:.  |
                         '.  :   ||:.  |                        ||:.  |
                           '-:   ||:.  |                        ||:.  |
                              '._||:.  |________________________||:.  |
                                 ||:___|'-.-'-.-'-.-'-.-'-.-'-.-||:___|
                                 [[____]                        [[____]

          ''')
    
    print("\n\n")

    print("END OF TRAVEL DAY")
    print()
    you.check_status()

    print("\n\n\n")

    # initialize dsfp day tracker
    counter = 1

    for x in range(10):
        dotmove(x)

    ###################################
    # typical day structure
    # Morn -> lunch -> afternoon
    # -> dinner -> end of day updates
    # To do: Better day progression, 
    # add special events like Wednesday Break
    # and the group dinner.
    ###################################
    print(f'Welcome to Day {counter}!!')
    print()
    print("Bryan: 'Now that we've finished our dicussion about the Code of Conduct,")
    for x in range(10):
        dotmove(x)
    print("        let's get into today's session. Pull the GitHub...'")
    for x in range(3):
        dotmove(x)

    for x in range(15):
        dotmove(x)
    print("\n\n")
    print("Bryan: 'Let's start our first break, be back in 30 minutes!")

    for x in range(10):
        dotmove(x)

    print()
    RandomEvent(you)
    print("\n\n")
    for x in range(10):
        dotmove(x)
    print(f"END OF DAY {counter}")
    print()
    you.check_status()
    counter += 1
    you.mod_knowledge(5)





























if __name__ == "__main__":
    main()
