# This script generates wealth in provinces
# for first-time setup of EOANB
# It must be run AFTER resource_variable_setup
from glob import *
import re
import os
import shutil

states_path = "history/states/*.txt"

all_state_files = iglob(states_path)

new_history_path = "./new_history"

states_path = "/history/states"

# NOTE: The value of resources is tied to currencies, not raw wealth

def get_resource_wealth(state):
    # Get the number of resources available in a state
