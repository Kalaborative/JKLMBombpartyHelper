from time import sleep
from random import choice
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import JavascriptException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
import pyperclip
import json
import sys

web_link = "http://bombparty.sparklinlabs.com/"
letterbank = "abcdefghijlmnopqrstuv"

individual_letters = []

for l in letterbank:
    individual_letters.append(l)

print("Starting up browser...")
chrome_options = Options()
chrome_options.add_argument('disable-infobars')
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(5)

sleepy_seconds = [0.02, 0.04, 0.03]
include_typos = [True, False]

def sendWord(word):
    # sleep(1)
    word = list(word)
    typos = []
    for i in range(10):
        typos.append([choice(letterbank), Keys.BACKSPACE])
    decide_if_typo = choice(include_typos)
    if decide_if_typo:
        number_of_typos = choice([1, 2, 3])
        for i in range(number_of_typos):
            word.insert(choice(range(len(word))), choice(typos))
        word = [item for sublist in word for item in sublist]
    inputBox = browser.find_element_by_id("WordInputBox")
    for w in word:
        seconds = choice(sleepy_seconds)
        inputBox.send_keys(w)
        sleep(seconds) # recommend for 0.02 seconds
        # print(seconds)
    sleep(0.2) # leave a small window between suggestions
    inputBox.send_keys(Keys.ENTER)


print("Navigating to the BombParty website...")
browser.get(web_link)

correct_setup = False
while not correct_setup:
    print("Please choose your room! Hit enter when ready. Make sure you're in the game!")

    ready = input("> ")

    current_user_id = browser.execute_script("return app.user.authId")
    # print(current_user_id)

    print("Getting your activePlayerIndex...")
    try:
        activePlayerIndex = browser.execute_script("return channel.data.actors.findIndex(a => a.authId === app.user.authId)")
        if activePlayerIndex == -1:
            print("You aren't currently in a game. Please click join game.")
        else:
            correct_setup = True
    except:
        print("You aren't currently in a game. Please click join game.")
print("Choose ENGLISH or FRENCH")
language = input("> ")
if language.lower() == "english":
    with open("sowpods.txt", "r") as wordlist:
        text = wordlist.read().splitlines()
        print("Word list loaded.")
        sleep(1)
        print("To quit the program, type 'CTRL+C'.")
        sleep(1)
        reported_words = []
        print("Waiting for game to start...")
        while True:
            try:
                individual_letters = []
                game_in_progress = browser.execute_script("return channel.data.state")
                activePlayerIndex = browser.execute_script("return channel.data.actors.findIndex(a => a.authId === app.user.authId)")
                if game_in_progress == "playing" and activePlayerIndex != -1:
                    while True:
                        game_in_progress = browser.execute_script("return channel.data.state")
                        if game_in_progress != "playing":
                            break
                        current_player = browser.execute_script("return channel.data.activePlayerIndex")
                        # print("On player {}".format(current_player))
                        if current_player == activePlayerIndex:
                            matching_words = []
                            if not individual_letters:
                                for l in letterbank:
                                    individual_letters.append(l)
                            # print(individual_letters)
                            letters = browser.execute_script("return channel.data.wordRoot")
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
                                print("Result: {}".format(colored(chosen_word, 'green')))
                                # pyperclip.copy(chosen_word)
                                sendWord(chosen_word)
                                text.remove(chosen_word)
                                for c in chosen_word:
                                    if c.lower() in individual_letters:
                                        individual_letters.remove(c.lower())
                                # print("Press enter to accept otherwise enter any text if failed.")
                                # unacceptable = input("> ")
                                # if "report" in unacceptable:
                                #     reported_words.append(chosen_word)
                                #     print("Reported this word.")
                                #     chosen_word = choice(matching_words)
                                #     sendWord(chosen_word)
                                # elif unacceptable:
                                #     chosen_word = choice(matching_words)
                                #     sendWord(chosen_word)
                                # if not unacceptable:                  
            except KeyboardInterrupt:
                print("Shutting down browser...")
                browser.quit()
                print("Closing program...")
                sys.exit() 
            except JavascriptException:
                pass
            except ElementNotInteractableException:
                pass
elif language.lower() == "french":
    with open("touslesmots.txt", "r") as wordlist:
        text = wordlist.read().splitlines()

        # Longer words only! 
        # text = [t for t in text if len(t) < 8]

        print("Word list loaded.")
        sleep(1)
        print("To quit the program, type 'CTRL+C'.")
        sleep(1)
        reported_words = []
        print("Waiting for game to start...")
        while True:
            try:
                individual_letters = []
                game_in_progress = browser.execute_script("return channel.data.state")
                activePlayerIndex = browser.execute_script("return channel.data.actors.findIndex(a => a.authId === app.user.authId)")
                if game_in_progress == "playing" and activePlayerIndex != -1:                
                    while True:
                        game_in_progress = browser.execute_script("return channel.data.state")
                        if game_in_progress != "playing":
                            break
                        current_player = browser.execute_script("return channel.data.activePlayerIndex")
                        # print("On player {}".format(current_player))
                        if current_player == activePlayerIndex:
                            matching_words = []
                            if not individual_letters:
                                for l in letterbank:
                                    individual_letters.append(l)
                            # print(individual_letters)
                            letters = browser.execute_script("return channel.data.wordRoot")
                            letters = letters.lower()
                            found = False
                            for word in text:
                                if letters in word.lower():
                                    found = True
                                    matching_words.append(word)
                            
                            if not found:
                                print("A match could not be found!")
                            else:
                                preferred_words = [word for word in matching_words for i in individual_letters if i in word]

                                # Prefer words that are adjectives!
                                # preferred_words_adj = [p for p in preferred_words if p[-4:] == "ment"]
                                # if preferred_words_adj:
                                #     chosen_word = choice(preferred_words_adj)
                                if preferred_words:
                                    chosen_word = choice(preferred_words)
                                    # chosen_word = max(preferred_words, key=len)
                                else:
                                    chosen_word = choice(matching_words)
                                    # chosen_word = max(matching_words, key=len)                    
                                print("Result: {}".format(colored(chosen_word, 'green')))
                                # pyperclip.copy(chosen_word)
                                sendWord(chosen_word)
                                sleep(0.2)
                                text.remove(chosen_word)
                                for c in chosen_word:
                                    if c.lower() in individual_letters:
                                        individual_letters.remove(c.lower())
                                # print("Press enter to accept otherwise enter any text if failed.")
                                # unacceptable = input("> ")
                                # if "report" in unacceptable:
                                #     reported_words.append(chosen_word)
                                #     print("Reported this word.")
                                #     chosen_word = choice(matching_words)
                                #     sendWord(chosen_word)
                                # elif unacceptable:
                                #     chosen_word = choice(matching_words)
                                #     sendWord(chosen_word)
                                # if not unacceptable:                  
                                #     for c in chosen_word:
                                #         if c.lower() in individual_letters:
                                #             individual_letters.remove(c.lower())
            except KeyboardInterrupt:
                print("Shutting down browser...")
                browser.quit()
                print("Closing program...")
                sys.exit()
            
            except JavascriptException:
                pass
            except ElementNotInteractableException:
                pass
            
else:
    print("Please type either 'english' or 'french'.")