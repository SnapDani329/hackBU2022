# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

alphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '/', '{', '}']

print('how long would you like your password to be?')
i=input()
i = int(i)
j=i

k=0
print('would you like to potentially include lowercase letters, Y/N?')
lowerCase=input().upper()
if lowerCase == 'Y':
    k=k+1

print('would you like to potentially include numbers, Y/N?')
numbersYN=input()
if numbersYN == 'Y':
    k=k+1

print('Would you like to potentially include Uppercase letters, Y/N?')
upperCase=input()
if upperCase == 'Y':
    k=k+1

print('Would you like to potentially include Symbols, Y/N?')
symbolsYN=input()
if symbolsYN == 'Y':
    k=k+1

if k == 0:
    print('Your password could not be created')

choicelist = []

if lowerCase == 'Y':
    while i > 0:
        choicelist.append(random.choice(alphaLower))
        i = i-1

i=j
if upperCase == 'Y':
    while i>0:
        choicelist.append(random.choice(alphaUpper))
        i=i-1

i=j
if numbersYN == 'Y':
    while i>0:
        choicelist.append(random.choice(numbers))
        i=i-1

i=j
if symbolsYN == 'Y':
    while i>0:
        choicelist.append(random.choice(symbols))
        i=i-1

random.shuffle(choicelist)
longPass= ''.join(choicelist)

if k == 1:
    print(longPass)

if k> 1:
    print(longPass[0:j])
    #print(longPass[len: finlen])





"""

if SymbolsYN:
    choiceList+= symbols
    
if Upper:
    choiceList += upper
    
for i in legnth:
    output += choiceList[random.randrange(0,len(choiceList))]

"""