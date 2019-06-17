# This script locates the files required and puts them into lists
# So we can iterate through them and read their contents
import regex
from glob import *
import os
import sys
import configparser
import __main__ as main

# BASIC PDOX SCRIPT AND HISTORY FILE READING FUNCTIONS

# Remove comments from a pdox file
def rm_comments(source_text):
    source_text = ''.join(source_text.split("#")[0].split("\t"))
    return source_text

# Make a list of values on different lines in a given piece of text
def make_list(source_text):
    new_list = source_text.strip().splitlines()
    return new_list

# Find values within a segment of a file inside curly brackets
def get_data_for(key_string, file):
    file = open(file, encoding="utf8")
    retrieved_data = re.findall(key_string + " = {(.*?)}", file.read(), re.S)
    rm_comments(retrieved_data)
    make_list(retrieved_data)
    return retrieved_data

# Get the config file for the file calling this script
# It must be called SCRIPTNAME_config.txt
config_path = main.__file__.split(".py")[0] + "_config.txt"

config = configparser.ConfigParser(allow_no_value = True)
config.read(config_path)

config_data = config._sections

def get_value(section, var, default):
    try:
        if config.get(section, var) != False:
            value = config.get(section,var)
    except:
        print("Invalid configuration '" + var + "'; set as default value: " + default)
        value = default
    print(var + " : " + value)
    return value

def list_options(section):
    try:
        options = config.options(section)
        if len(options) == 0:
            print("No folders specified")
        else:
            print(section + ": " + str(options))
    except:
        print("No "+section+" section in config")
        options = None
    return options

# A config file should have the following sections:

# [in_folders]
# Folders to be accessed and read from
# Each folder can have specific conditions to search for in its value
# If left blank, it will be left to a glob of the whole folder.
in_folders = list_options("in_folders")

# [out_folders]
# Folders into which new files are written
out_folders = list_options("out_folders")

# [important_files]
# Contains a list of important files stored in ./

important_files = list_options("important_files")

# [settings]
# Includes the following settings:

# id_from_filename_only (default = True)
# This gets only the state ID from the filename of states
get_value("settings","id_from_filename_only", "True")

# filetype (default = ".txt")
# Determines the filetypes to be searched
get_value("settings","filetype", ".txt")


