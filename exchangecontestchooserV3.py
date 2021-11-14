import sys # Imports system module
import time # Imports time module
from art import * # Imports art module
import random # Imports 'random' module
from termcolor import colored, cprint

def artTime(a): #function that takes 1 parameter: the winning string: to convert to ASCII and delay the release of the next printed line.
    a = text2art(a, font='Raleway', chr_ignore=True) #converts the string to ASCII art
    for x in a: # Iterates over the ASCII (a) string
        print(colored(x,'red', 'on_grey', attrs=['bold','dark']), end='', flush = True) #prints the fomatted ASCII (a) string
        time.sleep(0.001) #delays by 1 thousandth of a second before printing the next line
    return a # returns the winner in ASCII in the specified release interval

def split(s): #function
    return [char for char in s] #splits the element in an expression

ranNumber = [] # creates empty list
ranNumber.extend(range(1,13)) # fills list with integers from 1 to 12
random.shuffle(ranNumber) # shuffles order of list

listI = [] #empty list
lines = ['Lukman Hakim', 'Captainfalconer', 'wmzy(Petr)', 'Terry', 'cryptofy', 'Er_Ick', 'INAM', 'cryptoMJ', 'cabbage', 'Paul', 'Nix', '//sdinelli'] # This is the contestant list

for i in range(0, len(lines)): # Loops over the contestant list's index (positional value) one iteration at a time
    if i == int(ranNumber[0]): # Conditional statement to compare equality between the current index position of the contestant list and index position 0 of the random number list
        listI.append(lines[i]) # adds the string with the winners name to the empty list1

x = split(listI) #Splits the characters of the list element 0 with the contest winner string across the list's index
stringX = ''.join(str(x) for e in x) #converts the x list into a string to be handled by the art function (artTime)

liChar = '\'_[_]' #string characters which are left over after the list to string conversion
for character in liChar: #iterates over the string lichar
    stringX = stringX.replace(character, '') #searches over the stringx string to remove the lichar characters

artTime(stringX) #passes stringX to the artTime function

