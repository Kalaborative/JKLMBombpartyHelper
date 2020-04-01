_M='report'
_L='Press enter to accept otherwise enter any text if failed.'
_K='Result: {}'
_J='A match could not be found!'
_I=False
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
                        print(individual_letters);letters=input(_F)    
                        if letters.lower()==_G:
                                if reported_words:
                                        print(_H)
                                        for bad_word in reported_words:print(bad_word)
                                break
                        found=_I
                        for word in text:
                                if letters in word.lower():found=_A;matching_words.append(word)
                        if not found:print(_J)
                        else:
                                preferred_words=[A for A in matching_words for B in individual_letters if B in A.lower()]
                                if preferred_words:chosen_word=choice(preferred_words)
                                else:chosen_word=choice(matching_words)
                                print(_K.format(chosen_word));pyperclip.copy(chosen_word);print(_L);unacceptable=input(_B)
                                if _M in unacceptable:reported_words.append(chosen_word)
                                if not unacceptable:
                                        for c in chosen_word:
                                                if c.lower()in individual_letters:individual_letters.remove(c.lower())
elif language.lower()=='french':
        with open('touslesmots.txt','r')as wordlist:
                text=wordlist.read().splitlines();text=[A for A in text if len(A)>8];print(_C);sleep(1);print(_D);sleep(1);print(_E);reported_words=[]
                while _A:
                        matching_words=[]
                        if not individual_letters:
                                for l in letterbank:individual_letters.append(l)
                        print(individual_letters);letters=input(_F)    
                        if letters.lower()==_G:
                                if reported_words:
                                        print(_H)
                                        for bad_word in reported_words:print(bad_word)
                                break
                        found=_I
                        for word in text:
                                if letters in word.lower():found=_A;matching_words.append(word)
                        if not found:print(_J)
                        else:
                                preferred_words=[A for A in matching_words for B in individual_letters if B in A]
                                if preferred_words:chosen_word=choice(preferred_words)
                                else:chosen_word=choice(matching_words)
                                print(_K.format(chosen_word));pyperclip.copy(chosen_word);print(_L);unacceptable=input(_B)
                                if _M in unacceptable:reported_words.append(chosen_word)
                                text.remove(chosen_word)
                                if not unacceptable:
                                        for c in chosen_word:
                                                if c.lower()in individual_letters:individual_letters.remove(c.lower())
else:print("Please type either 'english' or 'french'.")