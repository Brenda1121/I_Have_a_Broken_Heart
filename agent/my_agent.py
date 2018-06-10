# -*- coding: utf-8 -*-
from agent import Agent
from card import ALL_CARDS


class MyAgent(Agent):
    '''
    You have to decide which card to play in this round.
    cards_you_have: list of cards in your hand
    cards_played: cards that has been played this round
    heart_broken: heart is broken or not
    info: score information and cards played in previous rounds
    '''
    def play(self, cards_you_have, cards_played, heart_broken, info):
        return ...

    '''
    decide cards you want to pass to the player next to you
    0->1, 1->2, 2->3, 3->0

    cards: list of cards in your hand
    '''
    def pass_cards(self, cards):
        q = cards_you_have.count('♥')
        if card.suit == '♠' and card.number == 12 in cards_you_have:
            cards_you_have.pop(Card('♠',12))
            if card.suit == '♠' and card.number == 13 in cards_you_have:
                cards_you_have.pop(Card('♠',13))    
            if card.suit == '♠' and card.number == 1 in cards_you_have:
                cards_you_have.pop(Card('♠',1)) 
            k = len(cards_you_have)
            for i in range (k-10):
                if 
        else:
            if q > 4:
                for i in range(3):
                    cards_you_have.pop(Card('♥',max(num))
            else:
                for i in range(3):
                    j = cards_you_have.count('♥')
                    if j > 0:
                        cards_you_have.pop(Card('♥',max(num))                                      
                    else :
                        cards_you_have.pop(Card(random(suit),max(num) for suit, num in product(_suit, _number)) 
                                       cards_you_have.pop(Card('♥',max(num))
                    j = cards_you_have.count('♥')
                    if j>0:
                        continue
                    if 
                       
                
            
            
                    
                cards_you_have.pop(
        if card.suit == '♥':
            return 1
        elif card.suit == '♠' and card.number == 12:
            return 13
        else:
            return 0
        return 
