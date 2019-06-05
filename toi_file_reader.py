# This script locates the files required and puts them into lists
# So we can iterate through them and read their contents
import regex
from glob import *
import os
import sys
import configparser
import __main__ as main

# Get the config file for the file calling this script
# It must be called SCRIPTNAME_config.txt
config_path = main.__file__.split(".py")[0] + "_config.txt"

config = configparser.ConfigParser(allow_no_value = True)
config.read(config_path)

config_data = config._sections

# A config file should have the following sections:

# [folders]
# Folders to be accessed
# Each folder can have specific conditions to search for in its value
# If left blank, it will be left to a glob of the whole folder.

# [settings]
# Includes the following settings:
# id_from_filename_only (default = True)
# This gets only the state ID from the filename of states
id_from_filename_only = config.get("settings","id_from_filename_only")
