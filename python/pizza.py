print("Frist test program of python")
print("Pizza * 20")


import random
secret = random.randint(1,99)
guess = 0
tries = 0
print("AHOY")
print("six tries")
print(secret)
while guess != secret and tries < 6:
    #guess = int(input("what's your guess? "))
    """
    some comments
    """

    '''
    some other comments
    '''
    guess = input("what's your guess? ")
    print(guess)
    if guess < secret:
                  print(guess,"too small")
    elif guess > secret:
                  print("too big")

    tries = tries +1

if guess == secret:
    print("GOOD")
else:
    print("DONE")

                  
                  
