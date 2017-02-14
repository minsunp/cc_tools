import sys

import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    #Loop through the json_data
    for item in json_data: #item: dictionary
        for key,value in item.items():

            if key == "platform":
                for k, v in value.items(): #value: dictionary
                    if k == "launch year":
                        launch_year = v
                    else: #k == "name"
                        name = v

            elif key == "title":
                title = value

            else: #key == "year"
                year = value

        #For loop for item dictionary ends: put in test_data classes
        # Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        game_platform = test_data.Platform(name, launch_year)
        game = test_data.Game(title, game_platform, year)

        #Add that Game object to the game_library
        game_library.add_game(game)

    #json_data for loop ends.
    #Return the completed game_library
    return game_library

# Handling command line arguments
#  Note: sys.argv is a list of strings that contains each command line argument
#        The first element in the list is always the name of the python file being run
# Command line format: <input json filename>

default_input_json_file = "data/test_data.json"

if len(sys.argv) == 2:
    input_json_file = sys.argv[1]
    print("Using command line args:", input_json_file)
else:
    print("Unknown command line options. Using default values:", default_input_json_file)
    input_json_file = default_input_json_file

#Load the json data from the input file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py

with open(input_json_file, 'r') as reader:
    json_data = json.load(reader)

game_library_data = make_game_library_from_json(json_data)
test_data.print_game_library(game_library_data)