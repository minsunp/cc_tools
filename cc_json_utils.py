import sys
import cc_data
import cc_dat_utils
import json

# Handling command line arguments
if len(sys.argv) == 2:
    input_json_filename = sys.argv[0]
    output_dat_filename = sys.argv[1]
    print("Using command line args:", input_json_filename, output_dat_filename)
else:
    print("Unknown command line options.")

# Get json input file and store info in dat output file.
def jsonToDat(inputfile, outputfile):

    # Load the json data from the input file
    with open(inputfile, 'r') as reader:
        json_data = json.load(reader)

    # Create new CCDataFile object
    cc_dat = cc_data.CCDataFile()

    for level in json_data: # level = dictionary

        # Create new CCLevel object, set variables
        cc_level = cc_data.CCLevel()

        cc_level.level_number = level["level_number"]
        cc_level.time = level["time"]
        cc_level.num_chips = level["num_chips"]
        cc_level.upper_layer = level["upper_layer"]
        cc_level.lower_layer = level["lower_layer"]

        # Iterate through all fields, add all fields to allFields list
        fields = level["optional_fields"] # fields = array

        for field in fields: # field = dictionary
            if (field["type"] == 3):
                cc_level.add_field(cc_data.CCMapTitleField(field["title"]))
            elif (field["type"] == 6):
                cc_level.add_field(cc_data.CCEncodedPasswordField(field["password"]))
            elif (field["type"] == 7):
                cc_level.add_field(cc_data.CCMapHintField(field["hint"]))
            else: # field["type"] == 10
                monsterPositions = field["monster_position"] # monsterPositions = array
                monsters = []
                for pos in monsterPositions: # pos = dictionary each corresponding to position
                    monsters.append(cc_data.CCCoordinate(pos["x"], pos["y"]))
                # All monster position elements added.
                cc_level.add_field(cc_data.CCMonsterMovementField(monsters))

        # Add levels to allLevels array
        cc_dat.add_level(cc_level)

    # Completed filling in cc_dat, output to dat file
    cc_dat_utils.write_cc_data_to_dat(cc_dat, outputfile)


#Use jsonToDat function to generate a dat file.
jsonToDat("minsunp_cc1.json", "minsunp_cc1.dat")