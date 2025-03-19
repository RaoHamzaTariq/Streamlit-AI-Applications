def mad_libs():

    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (present tense): ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter a plural noun: ")
    verb2 = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    adjective3 = input("Enter a third adjective: ")
    noun3 = input("Enter another noun: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    food = input("Enter a food: ")

    story = f"""
    The {adjective1} {noun1} decided to {verb1} to the store. It was a very {adjective2} day, and many {noun2} were out and about.
    Suddenly, the {noun1} {verb2} into a {place}. It was a very {adjective3} place filled with {noun3}.
    The {noun1} started {verb_ing} and then decided to eat some {food}.
    It was a very strange day.
    """

    print("\nHere's your Mad Libs story:\n")
    print(story)

mad_libs()