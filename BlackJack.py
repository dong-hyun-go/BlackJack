from random import randint

class deck(object):
	deck={"A":4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, "J":4, "Q":4, "K":4}
	cardsDict={1:"A", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K" }

	def __init__(self):
		print ("Deck was shuffled!")

	def getCard(self):
		global deck
		global cardsDict
		i=randint(1,13)
		if self.deck[self.cardsDict[i]] !=0:
			self.deck[self.cardsDict[i]]-=1
			return self.cardsDict[i]
		else:
			return self.getCard()

	


newDeck=deck()
print("Player gets following cards")
playerTotal=0
# card=newDeck.getCard()
# print ("First card: "+ str(card))
# playerTotal=playerTotal+card
# card=newDeck.getCard()
# print ("Second Card: "+ str(card))
for i in range(1, 53):
	card=newDeck.getCard()
	print (str(i)+" "+str(card))
#playerTotal=playerTotal+card
computerTotal=0

def cardValue(card):
	global playerTotal
	cardsDict={"A":1 , 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10 }
	if card=="A":
		if playerTotal<=10:
			return 11
	else:
		return cardsDict[card]
