p='Reported this word.'
o='report'
n='Press enter to accept otherwise enter any text if failed.'        
m='green'
l='Result: {}'
k='A match could not be found!'
j=False
i='red'
h='Reported words this game:'
g='stop'
f='Send a combination of letters: '
e="Type 'report' to report a word for not valid."
d="To quit the program, type 'stop'."
c='Word list loaded.'
b='r'
a=len
Z=max
Y=open
X='> '
T=True
P=input
A=print
from time import sleep as N
from random import choice as U
from termcolor import colored as O
import pyperclip as V,json
Q='abcdefghijlmnopqrstuv'
C=[]
for F in Q:C.append(F)
A('Choose ENGLISH or FRENCH')
W=P(X)
if W.lower()=='english':
        with Y('sowpods.txt',b)as R:
                G=R.read().splitlines();A(c);N(1);A(d);N(1);A(e);D=[]
                while T:
                        E=[]
                        if not C:
                                for F in Q:C.append(F)
                        H=P(f)
                        if H.lower()==g:
                                if D:
                                        A(h)
                                        for S in D:A(O(S,i))
                                break
                        I=j
                        for J in G:
                                if H in J.lower():I=T;E.append(J)    
                        if not I:A(k)
                        else:
                                K=[A for A in E for B in C if B in A.lower()]
                                if K:B=U(K)
                                else:B=U(E)
                                A(l.format(O(B,m)));V.copy(B);A(n);L=P(X)
                                if o in L:A(p);D.append(B)
                                G.remove(B)
                                if not L:
                                        for M in B:
                                                if M.lower()in C:C.remove(M.lower())
elif W.lower()=='french':
        with Y('touslesmots.txt',b)as R:
                G=R.read().splitlines();A(c);N(1);A(d);N(1);A(e);D=[]
                while T:
                        E=[]
                        if not C:
                                for F in Q:C.append(F)
                        H=P(f)
                        if H.lower()==g:
                                if D:
                                        A(h)
                                        for S in D:A(O(S,i))
                                break
                        I=j
                        for J in G:
                                if H in J.lower():I=T;E.append(J)    
                        if not I:A(k)
                        else:
                                K=[A for A in E for B in C if B in A]
                                if K:B=Z(K,key=a)
                                else:B=Z(E,key=a)
                                A(l.format(O(B,m)));V.copy(B);A(n);L=P(X)
                                if o in L:D.append(B);A(p)
                                G.remove(B)
                                if not L:
                                        for M in B:
                                                if M.lower()in C:C.remove(M.lower())
else:A("Please type either 'english' or 'french'.")