#import Player
#import Events

def main():

    locations = {"PA":"Drexel University, in Philadelphia, PA",
                 "CA":"University of California, Berkeley, in Berkeley, CA",
                 "TX":"Texas A&M at College Station, TX",
                 "WA":"University of Washington, in Seattle, WA",
                 "IL":"Northwestern University, in Evanston, IL",
                 "MA":"Harvard, in Cambridge, MA"}

    print("\n")
    print("You have received an email from esteemed Nobel Laureate in waiting, Bryan Scott! Let's see what he has to say...")
    print("\n")
    print("o---------------------------------------------o")
    print("| Dear ...                                    |")
    print("\n\n\n")
    name = input("What is your name? ")
    name = name.capitalize()
    print("\n")
    print("o---------------------------------------------o")
    print(f"| Dear {name},                                   |")
    print("| We are pleased to announce the next DSFP session   |")
    print("| will be held at ...                         |")
    print("\n\n\n")
    loc_key = ""
    while (loc_key not in locations.keys()):
        loc_key = (input(f"Where is the next session? {list(locations.keys())} "))
        loc_key = loc_key.upper()
    location = locations[loc_key.upper()]
    print("\n")
    print("o---------------------------------------------o")
    print(f"| Dear {name},                                   |")
    print("| We are pleased to announce the next DSFP session   |")
    print(f"| will be held at {location}.                    |")
    print("\n\n\n")
    start_loc = ""
    while ((start_loc != "domestic") and (start_loc != "international")):
        start_loc = input("Make sure you book your... [domestic/international] ")
        start_loc = start_loc.lower()
    print("\n")
    print("o---------------------------------------------o")
    print(f"| Dear {name},                                   |")
    print("| We are pleased to announce the next DSFP session  |")
    print(f"| will be held at {location}.                    |")
    print(f"| Make sure you book your {start_loc} travel quickly so you |")
    print("| get a big stonking per diem. We'll see you soon! |")
    print("|                                                      |")
    print("| Love you!                                            |")
    print("| Bryan <3                                           |")
    print("o---------------------------------------------o")
    print("\n\n\n")
    print(f"You're going to {location}! Yippee!!")



























if __name__ == "__main__":
    main()