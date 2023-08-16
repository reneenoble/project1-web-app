# create a function that capitalises names
def capitalise_name(name):
    return name.capitalize()

# Create a function that gives back a list of colours, based on a specified length passed in as an argument
def get_colours(length):
    colours = ["red", "green", "blue", "yellow", "black", "white", "purple", "orange"]
    return colours[:length]

# Create a function that takes in a list of names and returns a list of names that start with a specified letter
def get_names_starting_with(names, letter):
    return [name for name in names if name.startswith(letter)]