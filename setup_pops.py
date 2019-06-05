# This script creates POPs for all states
# for first-time setup of EOANB
# It must be run AFTER resource_varialbe_setup and wealth_setup scripts
import re
from math import *
from glob import *

# Identify the config file which contains constants
pops_config_path = "pops_config.txt"

# Define the constants
import sys
import configparser

config = configparser.ConfigParser()
config.read(pops_config_path)

MAX_POP_SIZE = float(config.get("values","MAX_POP_SIZE"))
MIN_POPS_PER_STATE = float(config.get("values","MIN_POPS_PER_STATE"))
SETUP_POPS_PER_PERSON = float(config.get("values","SETUP_POPS_PER_PERSON"))
MIN_POP_SPAWN_SIZE = float(config.get("values","MIN_POP_SPAWN_SIZE"))

def get_num_from_regex(input_string):
    input_string = input_string[0]
    input_string = input_string.replace(" ","")
    input_string = input_string.replace("=","")
    input_string = ''.join(input_string.split("#")[0].split("\t"))
    return input_string
    

def count_population(state_info):
    try:
        state_population_count = re.findall("manpower[ =](.*?)\n", state_info.read(), re.S)
        state_population_count = get_num_from_regex(state_population_count)
        print("Population here: " + str(state_population_count))
        return int(state_population_count)
    except Exception as ex:
        print("Could not find population value for state")

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def local_max_pop_size(state):
    state_max_pop_size = count_population(state)/10
    return state_max_pop_size

def get_max_pop_size(state):
    capped_max_pop_size = clamp(max_pop_calc(state),1,100000)
    return capped_max_pop_size

def create_pops(p):
    try:
        max_pop_size_here = p / MIN_POPS_PER_STATE
        max_pop_size_here = ceil(clamp(max_pop_size_here, 1, MAX_POP_SIZE))
        print("Max pop size here: " + str(max_pop_size_here))
        num_pops = p / max_pop_size_here
        # Add 1 to the number of starting pops, so they start under maximum size
        num_pops = ceil(clamp(num_pops, MIN_POPS_PER_STATE, 999)) + 1
        print("Number of pops in state: " + str(num_pops))
        pops_list = [pop_dictionary] * num_pops
        fill_pops(pops_list, p)
    except Exception as ex:
        print(ex)
        print("Did not create pops for state")

def determine_career():
    # Determine the career for a pop
    # Options are: service, labour, trades, intellectual
    pass

def determine_habitat():
    # Determine the habitat for a pop
    # Options are: rural, urban
    pass

def determine_culture():
    # Determine the culture for a pop
    pass

def determine_religion():
    # Determine the religion for a pop
    pass

def get_wealth_weight():
    # Get the weight for the share of wealth to be given to this pop
    pass

def determine_wealth():
    # Determine how much wealth a pop owns
    pass

def get_size_weight():
    # Get the weight for the share of population to be put in this pop
    pass

def default_pop_size(p):
    # Default size is equal to all other pops
    pop_size = ceil(p / len(pops_list))
    # Each pop needs a weighting to determine the percentage of population
    return pop_size

def determine_size(p):
    # Based on the number of jobs for this pop type available
    actual_pop_size = default_pop_size(p) * pop_percentage

pop_dictionary = {
    "habitat": determine_habitat(),
    "culture": determine_culture(),
    "religion": determine_religion(),
    "career": determine_career(),
    "wealth_weight": get_wealth_weight(),
    "wealth": determine_wealth(),
    "size": get_size_weight(),
    "consumer_goods_needs": determine_cg_needs(),
    # Consumer goods output of a pop is determined by other in-game factors
    "consumer_goods_output": determine_cg_output(),
    # Growth weight is set in-game
    # as a factor of immigration push/pull & policies
    "growth_weight": 0,
    # Militancy is a factor set in-game
    # as a factor of wealth per capita, policies, liberty and freedom
    "militancy": 0
    }

def fill_pops(pops_list, p):
    if pops_list != None:
        pops_done = 0
        for pop in pops_list:
            print(pop)
    

# Directories and files which the script needs to access
states_path = "history/states/*.txt"
all_state_files = iglob(states_path)
# new_history_path is used to write the new files
# This means old files are not overwritten
new_history_path = "./new_history"

for state in all_state_files:
    # Get only numbers from the filename, which should then give the state's ID
    state_id_location = re.findall(r"\d+", state)
    state_id = state_id_location[0]
    print("Reading state " + state_id)
    state_info = open(state, encoding="utf8")
    p = count_population(state_info)
    create_pops(p)
