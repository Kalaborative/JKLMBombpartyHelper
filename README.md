# A Simple Python Script for BombParty!

Hello! This is my scripts for BombParty, it is simple and easy to set up.


## Requirements

You need a browser and Python installed on your system.


## Installation

 1. Download or clone this repo. 
 2. Open a terminal and navigate to downloaded directory
 3. Run `pip install -r requirements.txt`
 4. Run either **bot.py** or **minibot.py**. Minibot is condensed for
    better performance. If it gives you an error about the wrong ChromeDriver version, please download the correct one [here](https://chromedriver.chromium.org/downloads)!

## Usage

Follow the prompts for English or French. You can type "stop" to stop the program or manually break by pressing Ctrl+C.

 - *auto_bot.py* - Main script. This will open a Chrome window. Enter a game and it will automatically play the game for you. Must supply the language first.
 - *manual_bot.py* - Use this one if you don't want to launch a new Chrome window, and offers more control with user input.
 - *new_word_fr.py* - Adds a new word to the French dictionary if not already there
 - *search_fr.py* - Searches the French dictionary for a string of characters
 - *search_en.py* - Searches English dictionary for a string of characters
 - *sowpods.txt* - The user-supplied English dictionary
 - *touslesmots.txt* - The user-supplied French dictionary

## Customization

Edit **auto_bot.py** or **manual_bot.py** if you want to make your own changes.

> You can filter the words you get from the dictionary.  For example, to only get words longer than eight letters, set `text = [t for t in text if len(t) > 8]`This is already supplied in the code.

Edit **sowpods.txt** or **touslesmots.txt** to alter the dictionaries.

> You can use the Find/Replace tool to search for words and delete them.

## Contribution

Please feel free to contribute to the repo! Or if you would like to update the dictionairies, you may do that as well.

## Example use

![Sample Image](https://puu.sh/FrVco.png)

