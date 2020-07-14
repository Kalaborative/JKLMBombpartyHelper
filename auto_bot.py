AC='Closing program...'
AB='Shutting down browser...'
AA='green'
A9='Result: {}'
A8='A match could not be found!'
A7='.syllable'
A6='syllable'
A5='Waiting for syllable to be detected...'
A4='Error switching to a frame.'
A3='Frame available. Switching...'
A2='iframe'
A1='Game found! Locating frame...'
A0='game'
z='Locating game...'
y="To quit the program, type 'CTRL+C'."
x='Word list loaded.'
w='r'
v='> '
u=Exception
t=KeyboardInterrupt
s=open
r=input
j=len
i=range
Z=''
J=False
F=True
A=print
from time import sleep as H
from random import choice as G
from termcolor import colored as a
from colorama import init
from selenium import webdriver as k
from selenium.webdriver.chrome.options import Options as l
from selenium.common.exceptions import JavascriptException as b,ElementNotInteractableException as c
from selenium.webdriver.common.keys import Keys as d
from selenium.webdriver.support.ui import WebDriverWait as S
from selenium.webdriver.support import expected_conditions as T      
from selenium.webdriver.common.by import By
import pyperclip,json,sys
m='https://jklm.fun/'
U='abcdefghijlmnopqrstuv'
init(autoreset=F)
C=[]
for K in U:C.append(K)
A('Starting up browser...')
e=l()
e.add_argument('disable-infobars')
B=k.Chrome(options=e)
B.implicitly_wait(5)
n=[0.02,0.04,0.03]
o=[F,J]
def f(word):
        A=word;A=list(A);C=[]
        for E in i(10):C.append([G(U),d.BACKSPACE])
        F=G(o)
        if F:
                I=G([1,2,3])
                for E in i(I):A.insert(G(i(j(A))),G(C))
                A=[C for B in A for C in B]
        D=B.find_element_by_css_selector('.selfTurn input')
        for J in A:K=G(n);D.send_keys(J);H(K)
        H(0.2);D.send_keys(d.ENTER)
A('Navigating to the JKLM website...')
B.get(m)
g=J
while not g:A("Please choose your room! Hit enter when ready. Make sure you're in the game!");AD=r(v);g=F
A('Choose ENGLISH or FRENCH')
h=r(v)
if h.lower()=='english':
        with s('sowpods.txt',w)as W:
                L=W.read().splitlines();A(x);H(1);A(y);H(1);p=[];A(z)
                try:S(B,15).until(T.presence_of_element_located((By.CLASS_NAME,A0)));A(A1);M=B.find_elements_by_tag_name(A2);A(j(M));B.switch_to.default_content;A(A3);B.switch_to.frame(M[0])
                except:A(A4)
                A(A5);N=J
                while not N:S(B,10).until(T.visibility_of_element_located((By.CLASS_NAME,A6)));N=F
                while F:
                        try:
                                C=[];D=Z;V=Z
                                while F:
                                        I=[]
                                        if not C:
                                                for K in U:C.append(K)
                                        X=J
                                        while not X:
                                                q=B.find_element_by_css_selector('.selfTurn').get_attribute('hidden')
                                                if q!='true':X=F     
                                        D=B.find_element_by_css_selector(A7).text;D=D.lower();O=J
                                        for P in L:
                                                if D in P.lower():O=F;I.append(P)
                                        if not O:A(A8)
                                        else:
                                                Q=[A for A in I for B in C if B in A.lower()]
                                                if Q:E=G(Q)
                                                else:E=G(I)
                                                A(A9.format(a(E,AA)))
                                                if X:f(E)
                                                H(0.3);L.remove(E)   
                                                for R in E:
                                                        if R.lower()in C:C.remove(R.lower())
                                                V=D
                        except t:A(AB);B.quit();A(AC);sys.exit()     
                        except b:pass
                        except c:pass
                        except u as Y:A(Y)
elif h.lower()=='french':
        with s('touslesmots.txt',w)as W:
                L=W.read().splitlines();A(x);H(1);A(y);H(1);p=[];A(z)
                try:S(B,15).until(T.presence_of_element_located((By.CLASS_NAME,A0)));A(A1);M=B.find_elements_by_tag_name(A2);A(j(M));B.switch_to.default_content;A(A3);B.switch_to.frame(M[0])
                except:A(A4)
                A(A5);N=J
                while not N:S(B,10).until(T.visibility_of_element_located((By.CLASS_NAME,A6)));N=F
                while F:
                        try:
                                C=[];D=Z;V=Z
                                while F:
                                        I=[]
                                        if not C:
                                                for K in U:C.append(K)
                                        while V==D:D=B.find_element_by_css_selector(A7).text;D=D.lower()
                                        O=J
                                        for P in L:
                                                if D in P.lower():O=F;I.append(P)
                                        if not O:A(A8)
                                        else:
                                                Q=[A for A in I for B in C if B in A.lower()]
                                                if Q:E=G(Q)
                                                else:E=G(I)
                                                A(A9.format(a(E,AA)));f(E);H(0.3);L.remove(E)
                                                for R in E:
                                                        if R.lower()in C:C.remove(R.lower())
                                                V=D
                        except t:A(AB);B.quit();A(AC);sys.exit()     
                        except b:pass
                        except c:pass
                        except u as Y:A(Y)
else:A("Please type either 'english' or 'french'.")