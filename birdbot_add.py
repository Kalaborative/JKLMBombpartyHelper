from time import sleep
from colorama import init
from random import choice
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import JavascriptException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import json
import sys

web_link = "https://jklm.fun"
letterbank = "abcdefghijlklmnopqrstuvwxyz"

individual_letters = []

for l in letterbank:
    individual_letters.append(l)


init(autoreset=True)
dir_path = os.getcwd()
print("Starting up browser...")
chrome_options = Options()
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-error')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.add_argument(f'user-data-dir={dir_path}/jklm')
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(5)

print("Navigating to the BombParty website...")
browser.get(web_link)

print("Please choose your room! Hit enter when ready. Make sure you're in the game!")
ready = input("> ")

with open("sowpods.txt", "r") as wordlist:
    text = wordlist.read().splitlines()
    print("Word list loaded.")
    sleep(1)
    print("To quit the program, type 'CTRL+C'.")
    sleep(1)
    print("Waiting for game to start...")
    frame = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(frame)
    previous_word = ''
    while True:
        try:
            bot_word = browser.execute_script('return milestone.playerStatesByPeerId[0].word;')
            if bot_word != previous_word:
                if bot_word:
                    # print(bot_word)
                    previous_word = bot_word
                    # Track added and existing words
                    added_words = []
                    existing_input_words = []

                    # Check if the word is already in the list
                    if bot_word in text:
                        existing_input_words.append(bot_word)
                    else:
                        # Add the new word to the list
                        text.add(bot_word)
                        added_words.append(bot_word)

                    # Save the updated list back to the file
                    with open('sowpods.txt', "a") as file:
                        file.write(bot_word + "\n")

                    if added_words:
                        print("Word(s) added successfully:", ', '.join(added_words))
                    else:
                        print("No new words to add.")

                    if existing_input_words:
                        print("Word(s) already in the list:", ', '.join(existing_input_words))
        except Exception as e:
            pass
        
