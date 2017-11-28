print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    if int(numCats) <= 0:
        print('No cats. How sad.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')
