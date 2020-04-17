import random

def card_dealer():

 card_value =["1","2","3","4","5","6","7","8","9","10","King","Queen","Jack","Ace"]
 card_suit =["♡", "♧", "♤","♢"]

 value_rand =random.randrange(len(card_value))   
 suite_rand =random.randrange(len(card_suit))  
 
 hit = (card_value[value_rand]+card_suit[suite_rand])

 print(hit)

card_dealer()

# other versions

#import random

#card_value =["1","2","3","4","5","6","7","8","9","10","King","Queen","Jack","Ace"]
#card_suit =["♡", "♧", "♤","♢"]

#value_rand =random.randrange(len(card_value))   
#suite_rand =random.randrange(len(card_suit))  

#def card_dealer():
 
 #hit = (card_value[value_rand]+card_suit[suite_rand])

 #print(hit)

#card_dealer()


#---------------------------------------------

#import random

#card_value =["1","2","3","4","5","6","7","8","9","10","King","Queen","Jack","Ace"]
#card_suit =["Hearts", "Spades", "Clubs","Diamons"]

#def card_dealer():

 #value_rand =random.randrange(len(card_value))   
 #suite_rand =random.randrange(len(card_suit))  
 

 #hit = (card_value[value_rand]+" of "+card_suit[suite_rand])

 #print(hit)

#card_dealer()



