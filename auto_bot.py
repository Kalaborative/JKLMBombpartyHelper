AA='Closing program...'
A9='Shutting down browser...'
A8='green'
A7='Result: {}'
A6='A match could not be found!'
A5='.syllable'
A4='syllable'
A3='Waiting for syllable to be detected...'
A2='Error switching to a frame.'
A1='Frame available. Switching...'
A0='iframe'
z='Game found! Locating frame...'
y='game'
x='Locating game...'
w="To quit the program, type 'CTRL+C'."
v='Word list loaded.'
u='r'
t='> '
s=Exception
r=KeyboardInterrupt
q=open
p=input
i=len
h=range
Y=''
S=False
G=True
A=print
from time import sleep as H
from random import choice as F
from termcolor import colored as Z
from selenium import webdriver as j
from selenium.webdriver.chrome.options import Options as k
from selenium.common.exceptions import JavascriptException as a,ElementNotInteractableException as b
from selenium.webdriver.common.keys import Keys as c
from selenium.webdriver.support.ui import WebDriverWait as T
from selenium.webdriver.support import expected_conditions as U      
from selenium.webdriver.common.by import By
import pyperclip,json,sys
l='https://jklm.fun/'
V='abcdefghijlmnopqrstuv'
C=[]
for J in V:C.append(J)
A('Starting up browser...')
d=k()
d.add_argument('disable-infobars')
B=j.Chrome(options=d)
B.implicitly_wait(5)
m=[0.02,0.04,0.03]
n=[G,S]
def e(word):
        A=word;A=list(A);C=[]
        for E in h(10):C.append([F(V),c.BACKSPACE])
        G=F(n)
        if G:
                I=F([1,2,3])
                for E in h(I):A.insert(F(h(i(A))),F(C))
                A=[C for B in A for C in B]
        D=B.find_element_by_css_selector('.selfTurn input')
        for J in A:K=F(m);D.send_keys(J);H(K)
        H(0.2);D.send_keys(c.ENTER)
A('Navigating to the JKLM website...')
B.get(l)
f=S
while not f:A("Please choose your room! Hit enter when ready. Make sure you're in the game!");AB=p(t);f=G
A('Choose ENGLISH or FRENCH')
g=p(t)
if g.lower()=='english':
        with q('sowpods.txt',u)as W:
                K=W.read().splitlines();A(v);H(1);A(w);H(1);o=[];A(x)
                try:T(B,15).until(U.presence_of_element_located((By.CLASS_NAME,y)));A(z);L=B.find_elements_by_tag_name(A0);A(i(L));B.switch_to.default_content;A(A1);B.switch_to.frame(L[0])
                except:A(A2)
                A(A3);M=S
                while not M:T(B,10).until(U.visibility_of_element_located((By.CLASS_NAME,A4)));M=G
                while G:
                        try:
                                C=[];D=Y;N=Y
                                while G:
                                        I=[]
                                        if not C:
                                                for J in V:C.append(J)
                                        while N==D:D=B.find_element_by_css_selector(A5).text;D=D.lower()
                                        O=S
                                        for P in K:
                                                if D in P.lower():O=G;I.append(P)
                                        if not O:A(A6)
                                        else:
                                                Q=[A for A in I for B in C if B in A.lower()]
                                                if Q:E=F(Q)
                                                else:E=F(I)
                                                A(A7.format(Z(E,A8)));e(E);H(0.3);K.remove(E)
                                                for R in E:
                                                        if R.lower()in C:C.remove(R.lower())
                                                N=D
                        except r:A(A9);B.quit();A(AA);sys.exit()     
                        except a:pass
                        except b:pass
                        except s as X:A(X)
elif g.lower()=='french':
        with q('touslesmots.txt',u)as W:
                K=W.read().splitlines();A(v);H(1);A(w);H(1);o=[];A(x)
                try:T(B,15).until(U.presence_of_element_located((By.CLASS_NAME,y)));A(z);L=B.find_elements_by_tag_name(A0);A(i(L));B.switch_to.default_content;A(A1);B.switch_to.frame(L[0])
                except:A(A2)
                A(A3);M=S
                while not M:T(B,10).until(U.visibility_of_element_located((By.CLASS_NAME,A4)));M=G
                while G:
                        try:
                                C=[];D=Y;N=Y
                                while G:
                                        I=[]
                                        if not C:
                                                for J in V:C.append(J)
                                        while N==D:D=B.find_element_by_css_selector(A5).text;D=D.lower()
                                        O=S
                                        for P in K:
                                                if D in P.lower():O=G;I.append(P)
                                        if not O:A(A6)
                                        else:
                                                Q=[A for A in I for B in C if B in A.lower()]
                                                if Q:E=F(Q)
                                                else:E=F(I)
                                                A(A7.format(Z(E,A8)));e(E);H(0.3);K.remove(E)
                                                for R in E:
                                                        if R.lower()in C:C.remove(R.lower())
                                                N=D
                        except r:A(A9);B.quit();A(AA);sys.exit()     
                        except a:pass
                        except b:pass
                        except s as X:A(X)
else:A("Please type either 'english' or 'french'.")