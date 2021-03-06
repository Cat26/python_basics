#-*-coding:utf-8-*-
import random
import os
from draw import *
from turtle import Turtle, Screen
t1 = Turtle()
t1.showturtle()

WORDLIST_FILENAME = "words.txt"
WORDLIST_POLISH = "podpalaczka.txt"

def loadWords(c):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(c, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = "".join(set(secretWord))
    letters_guessed = (''.join(lettersGuessed))
    return len(secretWord) == len(letters_guessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i in lettersGuessed:
            print(i, end=' ')
# print in the same raw
        else:
            print('_', end=' ')
    return ''



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alfabet:
        if i not in lettersGuessed:
            print(i, end=' ')
    return ''

def getAvailablePolish(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alfabet = 'aąbcćdeęfghijklłmnoópqrsśtuvwxyzżź'
    for i in alfabet:
        if i not in lettersGuessed:
            print(i, end=' ')
    return ''

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print(" The secret Word contain {} letters/".format(len(secretWord)))
    lista = []
    l = []
    funkcje=[szu_1, szu_2, szu_3, head, body, right_arm, left_arm, left_leg, right_leg]
    i = 0
    while i < 9:
        if isWordGuessed(secretWord, lista) == False:
            letter = input("give a letter: ")
            if letter in secretWord:
                lista.append(letter)
            else:
                funkcje[i](t1)
                i = i + 1
            l.append(letter)
            print(getGuessedWord(secretWord, lista))
            print("letters available: ")
            print(getAvailableLetters(l))
            if i == 9:
                print("you are hang! Try again")
                print("secret word was: " + secretWord)
        else:
            print("You win!")
            break


def hangmanpol(secretWord):
    print("słowo posiada {} liter".format(len(secretWord)))
    lista = []
    l = []
    funkcje=[szu_1, szu_2, szu_3, head, body, right_arm, left_arm, left_leg, right_leg]
    i = 0
    while i < 9:
        if isWordGuessed(secretWord, lista) == False:
            letter = input("podaj literę: ")
            if letter in secretWord:
                lista.append(letter)
            else:
                funkcje[i](t1)
                i = i + 1
            l.append(letter)
            print(getGuessedWord(secretWord, lista))
            print("dostępne litery: ")
            print(getAvailablePolish(l))
            if i == 9:
                print("Zawisłeś! Spróbuj ponownie!")
                print("tajemniczym słowem było: " + secretWord)
        else:
            print("Brawo wygrałeś!")
            break


language = input("Wybierz język polski kliknij 'p'/Choose language english press 'e': ")
if language == 'e':
    wordlist = loadWords(WORDLIST_FILENAME)
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
elif language == 'p':
    wordlist = loadWords(WORDLIST_POLISH)
    secretWord = chooseWord(wordlist).lower()
    hangmanpol(secretWord)
else:
    print("nie wybrales języka spróbuj ponownie/ Choose language again")