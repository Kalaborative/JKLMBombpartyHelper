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
letterbank = "abcdefghijlklmnopqrstuvwy"

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
chrome_options.add_argument(f'user-data-dir={dir_path}/jklm')
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(5)

sleepy_seconds = [0.02, 0.04, 0.03]
include_typos = [True, False]

# def sendWord(word):
#     # sleep(1)
#     word = list(word)
#     typos = []
#     for i in range(10):
#         typos.append([choice(letterbank), Keys.BACKSPACE])
#     decide_if_typo = choice(include_typos)
#     if decide_if_typo:
#         number_of_typos = choice([1, 2, 3])
#         for i in range(number_of_typos):
#             word.insert(choice(range(len(word))), choice(typos))
#         word = [item for sublist in word for item in sublist]
#     inputBox = browser.find_element(By.XPATH, "//div[@class='selfTurn']//input")
#     for w in word:
#         seconds = choice(sleepy_seconds)
#         inputBox.send_keys(w)
#         sleep(seconds) # recommend for 0.02 seconds
#         # print(seconds)
#     sleep(0.2) # leave a small window between suggestions
#     inputBox.send_keys(Keys.ENTER)

with open("sub1.txt", "r") as wordlist:
    sub1text = wordlist.read().splitlines()



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
    previous_syllable = ''
    while True:
        try:
            individual_letters = []
            while True:
                current_syllable = browser.find_element(By.CLASS_NAME, 'syllable').text
                if current_syllable == previous_syllable:
                    pass
                else:
                    # print("On player {}".format(current_player))
                    matching_words = []
                    if not individual_letters:
                        for l in letterbank:
                            individual_letters.append(l)
                    # print(individual_letters)
                    letters = current_syllable
                    letters = letters.lower()
                    found = False
                    for word in text:
                        if letters in word.lower():
                            found = True
                            matching_words.append(word)
                    
                    if not found:
                        print("A match could not be found!")
                    else:
                        preferred_words = [word for word in matching_words for i in individual_letters if i in word.lower()]
                        if preferred_words:
                            chosen_word = choice(preferred_words)
                        else:
                            chosen_word = choice(matching_words)

                        longs = [word for word in matching_words if len(word) >= 20]
                        minis = [word for word in matching_words if len(word) <= 6] 
                        subs = [word for word in matching_words if word in sub1text]
                        mc = [word for word in matching_words if '-' in word]
                        print()                  
                        print("Result: {}".format(colored(chosen_word, 'green')))
                        if longs:
                            print("Long: {}".format(colored(choice(longs), 'yellow')))
                        if minis:
                            print("Mini: {}".format(colored(choice(minis), 'cyan')))
                        if subs:
                            print("Sub: {}".format(colored(choice(subs), 'magenta')))
                        if mc:
                            print("MC: {}".format(colored(choice(mc), 'white')))
                        # sendWord(chosen_word)
                        # text.remove(chosen_word)
                        for c in chosen_word:
                            if c.lower() in individual_letters:
                                individual_letters.remove(c.lower())
                    previous_syllable = current_syllable
        except JavascriptException:
            pass
        except ElementNotInteractableException:
            pass