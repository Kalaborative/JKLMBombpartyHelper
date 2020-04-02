_P='Reported this word.'
_O='report'
_N='Press enter to accept otherwise enter any text if failed.'      
_M='green'
_L='Result: {}'
_K='A match could not be found!'
_J=False
_I='red'
_H='Reported words this game:'
_G='stop'
_F='Send a combination of letters: '
_E="Type 'report' to report a word for not valid."
_D="To quit the program, type 'stop'."
_C='Word list loaded.'
_B='> '
_A=True
from time import sleep
from random import choice
from termcolor import colored
import pyperclip,json
letterbank='abcdefghijlmnopqrstuv'
individual_letters=[]
for l in letterbank:individual_letters.append(l)
print('Choose ENGLISH or FRENCH')
language=input(_B)
if language.lower()=='english':
        with open('sowpods.txt','r')as wordlist:
                text=wordlist.read().splitlines();print(_C);sleep(1);print(_D);sleep(1);print(_E);reported_words=[]
                while _A:
                        matching_words=[]
                        if not individual_letters:
                                for l in letterbank:individual_letters.append(l)
                        letters=input(_F)
                        if letters.lower()==_G:
                                if reported_words:
                                        print(_H)
                                        for bad_word in reported_words:print(colored(bad_word,_I))
                                break
                        found=_J
                        for word in text:
                                if letters in word.lower():found=_A;matching_words.append(word)
                        if not found:print(_K)
                        else:
                                preferred_words=[A for A in matching_words for B in individual_letters if B in A.lower()]
                                if preferred_words:chosen_word=choice(preferred_words)
                                else:chosen_word=choice(matching_words)
                                print(_L.format(colored(chosen_word,_M)));pyperclip.copy(chosen_word);print(_N);unacceptable=input(_B)  
                                if _O in unacceptable:print(_P);reported_words.append(chosen_word)
                                if not unacceptable:
                                        for c in chosen_word:       
                                                if c.lower()in individual_letters:individual_letters.remove(c.lower())
elif language.lower()=='french':
        with open('touslesmots.txt','r')as wordlist:
                text=wordlist.read().splitlines();print(_C);sleep(1);print(_D);sleep(1);print(_E);reported_words=[]
                while _A:
                        matching_words=[]
                        if not individual_letters:
                                for l in letterbank:individual_letters.append(l)
                        letters=input(_F)
                        if letters.lower()==_G:
                                if reported_words:
                                        print(_H)
                                        for bad_word in reported_words:print(colored(bad_word,_I))
                                break
                        found=_J
                        for word in text:
                                if letters in word.lower():found=_A;matching_words.append(word)
                        if not found:print(_K)
                        else:
                                preferred_words=[A for A in matching_words for B in individual_letters if B in A]
                                if preferred_words:chosen_word=choice(preferred_words)
                                else:chosen_word=choice(matching_words)
                                print(_L.format(colored(chosen_word,_M)));pyperclip.copy(chosen_word);print(_N);unacceptable=input(_B)  
                                if _O in unacceptable:reported_words.append(chosen_word);print(_P)
                                text.remove(chosen_word)
                                if not unacceptable:
                                        for c in chosen_word:       
                                                if c.lower()in individual_letters:individual_letters.remove(c.lower())
else:print("Please type either 'english' or 'french'.")