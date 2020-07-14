_R='Closing program...'
_Q='Shutting down browser...'
_P='green'
_O='Result: {}'
_N='A match could not be found!'
_M='.syllable'
_L='syllable'
_K='Waiting for syllable to be detected...'
_J='Error switching to a frame.'
_I='Frame available. Switching...'
_H='iframe'
_G='Game found! Locating frame...'
_F='game'
_E='Locating game...'
_D="To quit the program, type 'CTRL+C'."
_C='Word list loaded.'
_B=False
_A=True
from time import sleep
from random import choice
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import JavascriptException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC     
from selenium.webdriver.common.by import By
import pyperclip,json,sys
web_link='https://jklm.fun/'
letterbank='abcdefghijlmnopqrstuv'
individual_letters=[]
for l in letterbank:individual_letters.append(l)
print('Starting up browser...')
chrome_options=Options()
chrome_options.add_argument('disable-infobars')
browser=webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(5)
sleepy_seconds=[0.02,0.04,0.03]
include_typos=[_A,_B]
def sendWord(word):
        A=word;A=list(A);B=[]
        for D in range(10):B.append([choice(letterbank),Keys.BACKSPACE])
        E=choice(include_typos)
        if E:
                F=choice([1,2,3])
                for D in range(F):A.insert(choice(range(len(A))),choice(B))
                A=[C for B in A for C in B]
        C=browser.find_element_by_css_selector('.selfTurn input')    
        for G in A:H=choice(sleepy_seconds);C.send_keys(G);sleep(H)  
        sleep(0.2);C.send_keys(Keys.ENTER)
print('Navigating to the JKLM website...')
browser.get(web_link)
correct_setup=_B
while not correct_setup:print("Please choose your room! Hit enter when ready. Make sure you're in the game!");ready=input('> ');correct_setup=_A
print('Choose ENGLISH or FRENCH')
language=input('> ')
if language.lower()=='english':
        with open('sowpods.txt','r')as wordlist:
                text=wordlist.read().splitlines();print(_C);sleep(1);print(_D);sleep(1);reported_words=[];print(_E)
                try:WebDriverWait(browser,15).until(EC.presence_of_element_located((By.CLASS_NAME,_F)));print(_G);num_frames=browser.find_elements_by_tag_name(_H);print(len(num_frames));browser.switch_to.default_content;print(_I);browser.switch_to.frame(num_frames[0])        
                except:print(_J)
                print(_K);syllablesFound=_B
                while not syllablesFound:WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CLASS_NAME,_L)));syllablesFound=_A
                while _A:
                        try:
                                individual_letters=[]
                                while _A:
                                        matching_words=[]
                                        if not individual_letters:   
                                                for l in letterbank:individual_letters.append(l)
                                        letters=browser.find_element_by_css_selector(_M).text;letters=letters.lower();found=_B
                                        for word in text:
                                                if letters in word.lower():found=_A;matching_words.append(word)
                                        if not found:print(_N)       
                                        else:
                                                preferred_words=[A for A in matching_words for B in individual_letters if B in A.lower()] 
                                                if preferred_words:chosen_word=choice(preferred_words)
                                                else:chosen_word=choice(matching_words)
                                                print(_O.format(colored(chosen_word,_P)));sendWord(chosen_word);sleep(0.3);text.remove(chosen_word)
                                                for c in chosen_word:
                                                        if c.lower()in individual_letters:individual_letters.remove(c.lower())
                        except KeyboardInterrupt:print(_Q);browser.quit();print(_R);sys.exit()
                        except JavascriptException:pass
                        except ElementNotInteractableException:pass  
                        except Exception as e:print(e)
elif language.lower()=='french':
        with open('touslesmots.txt','r')as wordlist:
                text=wordlist.read().splitlines();print(_C);sleep(1);print(_D);sleep(1);reported_words=[];print(_E)
                try:WebDriverWait(browser,15).until(EC.presence_of_element_located((By.CLASS_NAME,_F)));print(_G);num_frames=browser.find_elements_by_tag_name(_H);print(len(num_frames));browser.switch_to.default_content;print(_I);browser.switch_to.frame(num_frames[0])        
                except:print(_J)
                print(_K);syllablesFound=_B
                while not syllablesFound:WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CLASS_NAME,_L)));syllablesFound=_A
                while _A:
                        try:
                                individual_letters=[]
                                while _A:
                                        matching_words=[]
                                        if not individual_letters:   
                                                for l in letterbank:individual_letters.append(l)
                                        letters=browser.find_element_by_css_selector(_M).text;letters=letters.lower();found=_B
                                        for word in text:
                                                if letters in word.lower():found=_A;matching_words.append(word)
                                        if not found:print(_N)       
                                        else:
                                                preferred_words=[A for A in matching_words for B in individual_letters if B in A.lower()] 
                                                if preferred_words:chosen_word=choice(preferred_words)
                                                else:chosen_word=choice(matching_words)
                                                print(_O.format(colored(chosen_word,_P)));sendWord(chosen_word);sleep(0.3);text.remove(chosen_word)
                                                for c in chosen_word:
                                                        if c.lower()in individual_letters:individual_letters.remove(c.lower())
                        except KeyboardInterrupt:print(_Q);browser.quit();print(_R);sys.exit()
                        except JavascriptException:pass
                        except ElementNotInteractableException:pass  
                        except Exception as e:print(e)
else:print("Please type either 'english' or 'french'.")