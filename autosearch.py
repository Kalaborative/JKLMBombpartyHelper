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

def make_syllable():
    syll_1 = choice(letterbank)
    syll_2 = choice(letterbank)
    return syll_1 + syll_2

print("Please choose your room! Hit enter when ready. Make sure you're in the game!")
ready = input("> ")

with open("sowpods.txt", "r") as wordlist:
    text = wordlist.read().splitlines()
    print("Word list loaded.")
    sleep(1)
    print("To quit the program, type 'CTRL+C'.")
    sleep(1)
    while True:
        prompt = make_syllable()
        browser.find_element(By.TAG_NAME, 'textarea').send_keys('/c {}'.format(prompt) + Keys.ENTER)
        sleep(1)
        texts = browser.find_elements(By.CLASS_NAME, 'text')
        recent = texts.pop()
        msg = recent.text
        # "0 result(s):  (0 hidden)"
        # "2 result(s): TEQBALL, TEQBALLS (0 hidden)"
        if 'result(s)' in msg:
            result = msg.split(": ")[1].split(" (")[0]
            if result:
                input_words = [word.strip().lower() for word in result.split(",")]
                added_words = []
                existing_input_words = []
                with open('sowpods.txt', "r") as file:
                    existing_words = {word.strip() for word in file.readlines()}
                for new_word in input_words:
                    # Check if the word is already in the list
                    if new_word in existing_words:
                        existing_input_words.append(new_word)
                    else:
                        # Add the new word to the list
                        existing_words.add(new_word)
                        added_words.append(new_word)

                # Save the updated list back to the file
                with open('sowpods.txt', "w") as file:
                    for word in existing_words:
                        file.write(word + "\n")

                if added_words:
                    added_words = [colored(a, 'green') for a  in added_words]
                    print("Word(s) added successfully:", ', '.join(added_words))
                else:
                    print("No new words to add.")

                if existing_input_words:
                    print("Word(s) already in the list:", ', '.join(existing_input_words))
                
        sleep(2)



