A9='Closing program...'
A8='Shutting down browser...'
A7='green'
A6='Result: {}'
A5='A match could not be found!'
A4='.syllable'
A3='letters'
A2='syllable'
A1='Waiting for syllable to be detected...'
A0='Error switching to a frame.'
z='Frame available. Switching...'
y='iframe'
x='Game found! Locating frame...'
w='game'
v='Locating game...'
u="To quit the program, type 'CTRL+C'."
t='Word list loaded.'
s='r'
r='> '
q=Exception
p=KeyboardInterrupt
o=open
n=input
h=len
g=range
S=False
G=True
A=print
from time import sleep as I
from random import choice as F
from termcolor import colored as Z
from selenium import webdriver as i
from selenium.webdriver.chrome.options import Options as j
from selenium.common.exceptions import JavascriptException as a,ElementNotInteractableException as b
from selenium.webdriver.common.keys import Keys as c
from selenium.webdriver.support.ui import WebDriverWait as T
from selenium.webdriver.support import expected_conditions as U      
from selenium.webdriver.common.by import By
import pyperclip as d,json,sys
k='https://jklm.fun/'
V='abcdefghijlmnopqrstuv'
C=[]
for J in V:C.append(J)
A('Starting up browser...')
W=j()
W.add_argument('disable-infobars')
B=i.Chrome(options=W)
B.implicitly_wait(5)
AA=[0.02,0.04,0.03]
l=[G,S]
def AB(word):
        A=word;A=list(A);C=[]
        for E in g(10):C.append([F(V),c.BACKSPACE])
        G=F(l)
        if G:
                H=F([1,2,3])
                for E in g(H):A.insert(F(g(h(A))),F(C))
                A=[C for B in A for C in B]
        D=B.find_element_by_css_selector('.selfTurn input')
        for J in A:D.send_keys(J)
        I(0.2);D.send_keys(c.ENTER)
A('Navigating to the JKLM website...')
B.get(k)
e=S
while not e:A("Please choose your room! Hit enter when ready. Make sure you're in the game!");AC=n(r);e=G
A('Choose ENGLISH or FRENCH')
f=n(r)
if f.lower()=='english':
        with o('sowpods.txt',s)as X:
                K=X.read().splitlines();A(t);I(1);A(u);I(1);m=[];A(v)
                try:T(B,15).until(U.presence_of_element_located((By.CLASS_NAME,w)));A(x);L=B.find_elements_by_tag_name(y);A(h(L));B.switch_to.default_content;A(z);B.switch_to.frame(L[0])
                except:A(A0)
                A(A1);M=S
                while not M:T(B,10).until(U.visibility_of_element_located((By.CLASS_NAME,A2)));M=G
                while G:
                        try:
                                C=[];D=A3;N=''
                                while G:
                                        H=[]
                                        if not C:
                                                for J in V:C.append(J)
                                        while N==D:D=B.find_element_by_css_selector(A4).text;D=D.lower()
                                        O=S
                                        for P in K:
                                                if D in P.lower():O=G;H.append(P)
                                        if not O:A(A5)
                                        else:
                                                Q=[A for A in H for B in C if B in A.lower()]
                                                if Q:E=F(Q)
                                                else:E=F(H)
                                                A(A6.format(Z(E,A7)));d.copy(E);K.remove(E)
                                                for R in E:
                                                        if R.lower()in C:C.remove(R.lower())
                                                N=D
                        except p:A(A8);B.quit();A(A9);sys.exit()     
                        except a:pass
                        except b:pass
                        except q as Y:A(Y)
elif f.lower()=='french':
        with o('touslesmots.txt',s)as X:
                K=X.read().splitlines();A(t);I(1);A(u);I(1);m=[];A(v)
                try:T(B,15).until(U.presence_of_element_located((By.CLASS_NAME,w)));A(x);L=B.find_elements_by_tag_name(y);A(h(L));B.switch_to.default_content;A(z);B.switch_to.frame(L[0])
                except:A(A0)
                A(A1);M=S
                while not M:T(B,10).until(U.visibility_of_element_located((By.CLASS_NAME,A2)));M=G
                while G:
                        try:
                                C=[];D=A3;N=''
                                while G:
                                        H=[]
                                        if not C:
                                                for J in V:C.append(J)
                                        while N==D:D=B.find_element_by_css_selector(A4).text;D=D.lower()
                                        O=S
                                        for P in K:
                                                if D in P.lower():O=G;H.append(P)
                                        if not O:A(A5)
                                        else:
                                                Q=[A for A in H for B in C if B in A.lower()]
                                                if Q:E=F(Q)
                                                else:E=F(H)
                                                A(A6.format(Z(E,A7)));d.copy(E);K.remove(E)
                                                for R in E:
                                                        if R.lower()in C:C.remove(R.lower())
                                                N=D
                        except p:A(A8);B.quit();A(A9);sys.exit()     
                        except a:pass
                        except b:pass
                        except q as Y:A(Y)
else:A("Please type either 'english' or 'french'.")