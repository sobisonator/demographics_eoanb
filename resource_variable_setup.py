# This script creates variables out of all states' resources
# for first-time setup of EOANB
# This creates a load of state scopes with variable assignments which you can put into an event's effects
from glob import *
import re
import os
import shutil

states_path = "history/states/*.txt"

all_state_files = iglob(states_path)

resources_file = "resources_master.txt"

# Add the string _available before the substring  ' ='
# This turns 'r_wood =' into 'r_wood_available =' etc.
substrs = [" ","="]
inserttxt = "_available"

new_history_path = "./new_history"

states_path = "/history/states"

def lookat(file):
    open(file, "rt")

def add_values(state_id, resources):
    f = open(resources_file, "a+")
    print("Made variable declaration for " + state_id)
    f.write(
        "\n" +
        state_id + "= {"
        )
    for resource in resources:
        resource_str = resource
        # Add the string _available before the substring  ' ='
        # This turns 'r_wood =' into 'r_wood_available =' etc.
        # See above for the setting of variables used in this.
        for substr in substrs:
            try:
                if inserttxt not in resource_str:
                    idx = resource_str.index(substr)
                    resource_str = resource_str[:idx] + inserttxt + resource_str[idx:]
            except:
                pass
        f.write(
            "set_variable = { r_" + resource_str + " } \n"
        )
    f.write(
        "} \n"
        )
    f.close

def clear_resources(filename, resources):
    resources = ''.join(resources)
    with open(filename, encoding="utf8") as f:
        s = f.read()
        if resources not in s:
            return
        with open(filename, "w", encoding="utf8") as f:
            s = s.replace(resources, "")
            f.write(s)

# Create a path to store the new history files with 0 resources
if not os.path.exists(new_history_path + states_path):
    print("Made directory at " + new_history_path)
    os.makedirs(new_history_path + states_path)

for state_filepath in all_state_files:
    # Get only numbers from the filename, which should be the ID
    state_id_location = re.findall(r"\d+", state_filepath)
    state_id = state_id_location[0]
    state_info = open(state_filepath, encoding="utf8")
    state_resource_info = re.findall("resources = {(.*?)}", state_info.read(), re.S)
    # Create a variable declaration statement with the resource values from the original file
    for resources in state_resource_info:
        # Remove all comments
        resources = ''.join(resources.split("#")[0].split("\t"))
        # Make lists of the resources in states
        resources_list = resources.strip().splitlines()
    # Create a new state history file with 0 resources in it
    shutil.copy(state_filepath,new_history_path + states_path + "/")
    newfile = new_history_path + "/" + state_filepath
#    new_info = open(newfile, encoding = "utf8")
    clear_resources(newfile, state_resource_info)
    add_values(state_id, resources_list)
