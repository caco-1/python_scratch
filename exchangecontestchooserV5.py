import sys # Imports system module.
import time # Imports time module.
from art import * # Imports ASCII art module.
import random # Imports 'random' module.
from termcolor import colored, cprint # Imports coloured 'text' module.


def artTime(a): # Function that takes 1 parameter: the winning string: to convert to ASCII and delay the release of the next printed line.
    print('And the winner is...'\n\n)
    a = text2art(a, font='4x4_offr', chr_ignore=True) # Converts the string to ASCII art.
    for x in a: # Iterates over the ASCII (a) string.
        print(colored(x,'red', 'on_grey', attrs=['bold','dark']), end='', flush = True) # Prints the fomatted ASCII (a) string with colours and attributes.
        time.sleep(0.001) # Delays by 1 thousandth of a second before printing the next line.
    print(stringX)
    return a # Returns the output of the above.

def split(s): # Function.
    return [char for char in s] # Splits the element in an expression.

ranNumber = [] # Creates empty list.
ranNumber.extend(range(1,13)) # Fills list with integers from 1 to 12.
random.shuffle(ranNumber) # Shuffles order of list.

listI = [] # Empty list.
lines = ['Lukman Hakim', 'Captainfalconer', 'wmzy(Petr)', 'Terry', 'cryptofy', 'Er_Ick', 'INAM', 'cryptoMJ', 'cabbage', 'Paul', 'Nix', '//sdinelli'] # This is the contestant list.
random.shuffle(lines) # Randomises the positions of the contestants in the lines list.


for i in range(1, len(lines[-1])): # Loops over the contestant list's index (positional value) one iteration at a time
    if len(listI) == 1: # Checks if listI has an element
        break # If listI has an elment then the loop exits and we move onto the artTime function.
    for y in ranNumber: # Iterates over the random numbers in the ranNumber list.
        if y == i: # Conditional statement to compare equality between the iteration of the Random number list and then i iteration above.
            listI.append(lines[i])  # Adds the string with the winners name to the empty list1.


x = split(listI) # Splits the characters of the list element 0 with the contest winner string across the list's index.
stringX = ''.join(str(x) for e in x) # Converts the x list into a string to be handled by the art function (artTime).

liChar = '\'[]' # String characters which are left over after the list to string conversion.
for character in liChar: # Iterates over the string lichar.
    stringX = stringX.replace(character, '') # Searches over the stringx string to remove the lichar characters.


artTime(stringX) # Passes stringX to the artTime function.
