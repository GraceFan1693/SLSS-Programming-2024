# Chatbot
# Author: Grace
# 11-03-2024

import random
#Demonstracte soe parts of the random module

def coin_flip():
    #return either head tail , or other?
    #Head -- (0, 0.5]
    #Tail -- (0.5, 0.999999]
    #others -- the rest
    result = random.random()
    if result < 0.5:
        return "heads"
    elif result < 0.999999:
        return "tails"
    else:
        return "others"
    
def main():
    head = 0
    tail = 0
    others = 0
    print(coin_flip)