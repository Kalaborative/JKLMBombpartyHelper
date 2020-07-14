# A Simple Python Script for BombParty!

Hello! This is my scripts for BombParty, it is simple and easy to set up.


## Requirements

You need a browser and Python installed on your system.


## Installation

 1. Download or clone this repo. 
 2. Open a terminal and navigate to downloaded directory
 3. Run `pip install -r requirements.txt`
 4. Run either **auto_bot.py** or **auto_bot_nosend.py**. If it gives you an error about the wrong ChromeDriver version, please download the correct one [here](https://chromedriver.chromium.org/downloads)!

## Usage

Follow the prompts for English or French. You can type "stop" to stop the program or manually break by pressing Ctrl+C.

 - *auto_bot.py* - Main script. This will open a Chrome window. Enter a game and it will automatically play the game for you. Must supply the language first.
 - *auto_bot_nosend.py* - Same as auto_bot but will not automatically send results. randomly displays a word matching the prompt for you in real-time.
 - *manual_bot.py* - Use this one if you don't want to launch a new Chrome window, and offers more control with user input.
 - *new_word.py* - Adds a new word to the dictionaries if not already there
 - *search_fr.py* - Searches the French dictionary for a string of characters
 - *search_en.py* - Searches English dictionary for a string of characters
 - *sowpods.txt* - The user-supplied English dictionary
 - *touslesmots.txt* - The user-supplied French dictionary
 
## Offline Training

Run *train.py* to coach yourself to use specific words based on the prompts! You can type your prompt or let the program choose one for you.
The supplied ones are examples of words you can use to train with, but you can replace them with your own.
Remember if you want French instead, rename `sowpods.txt` to `touslesmots.txt`

## Customization

Edit **auto_bot.py** or **manual_bot.py** if you want to make your own changes.

> You can filter the words you get from the dictionary.  For example, to only get words longer than eight letters, set `text = [t for t in text if len(t) > 8]`This is already supplied in the code.

> You can also choose if you want a randomly chosen word or the longest word to be the result. Simply comment out one line and uncomment the other.

Edit **sowpods.txt** or **touslesmots.txt** to alter the dictionaries.

> You can use the Find/Replace tool to search for words and delete them.

## Contribution

Please feel free to contribute to the repo! Or if you would like to update the dictionairies, you may do that as well.

## Example use
[NEEDS UPDATE]
![Sample Image](https://puu.sh/FrVco.png)

