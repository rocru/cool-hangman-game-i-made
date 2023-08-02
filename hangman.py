yyimport random
words = ('ant').split()
tries = 6
wordchoice = random.choice(words)
Lcount = len(wordchoice)
Ucount = ("_ "* Lcount)
wordGuess = Ucount.split()


def checker():
    if answer in wordchoice:
        wordPos = wordchoice.find(answer)
        wordGuess[wordPos] = answer
        print(wordGuess)
        wordCheck = ''.join(wordGuess)
        if wordCheck == wordchoice:
            print(wordCheck)
            print('You won. ')
        return


def prompt2():
    tries = 6
    tries -= 1
    answer = input(f'Your answer was wrong/invalid. You have {tries} tries left. ')
    print(wordGuess)
    return 
start = input('Welcome to hangman. Would you like to proceed? [Y/N] ')
if start == ('Y') or ('y'):
    answer = input(f'You have {tries} tries left. Please submit your guess. ')
    if answer in wordchoice:
        checker()
    if answer not in wordchoice:
        prompt2()
    
    answer = input(f'You have {tries} tries left. Please submit your guess. ')
    if answer in wordchoice:    
        checker()
    if answer not in wordchoice:
        prompt2()
    
    answer = input(f'You have {tries} tries left. Please submit your guess. ')
    if answer in wordchoice:    
        checker()
    if answer not in wordchoice:
        prompt2()

  