# Homework 8 Part 1 

# MongoDB Atlas Database Connection and Quote Search

This project demonstrates how to connect to a MongoDB Atlas database using the Mongoengine library in Python. It also includes a script for searching quotes.

## Prerequisites

1. Python 3.x
2. MongoDB database
3. Required Python packages:  `mongoengine`  (install using `pip install mongoengine`)

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.

## Loading Data into the Database

1. Create JSON files named `authors.json` and `quotes.json` with the data to be loaded into the database.

2. Run the `baseloader.py` script to load the data into the MongoDB Atlas database:

        `python baseloader.py`


## Searching for Quotes

1. Run the `searcher.py` script to search for quotes using different commands:


        `python searcher.py`


The script will prompt you to input commands in the format `command:value`. Available commands are:
- `name:value` - Search and display quotes by author's name.
- `tag:value` - Search and display quotes by a specific tag.
- `tags:value1,value2` - Search and display quotes by multiple tags (comma-separated).
- `exit` - Exit the script.

## License

This project is licensed under the MIT License.
