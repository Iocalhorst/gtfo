import random

colors = ["diamonds","clubs","spades","hearts"]
symbols = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
value=[1,2,3,4,5,6,7,8,9,10,11,12,13]

class Card():
	def __init__(self,symbol,color,value):
		self.symbol=symbol
		self.color=color
		self.__name__=self.symbol+" of "+self.color
	
	def __repr__(self):
		print(self.__name__)

class Deck():
	#self stellt den bezug zur instanz her
	#print("moin")

	def __init__(self):
		self.cards=[]
		for color in colors:
			for i in range(13):
				symbol=symbols[i]
				newcard=Card(symbol,color,i)
				self.cards.append(newcard)
		
	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self):
		card=self.cards.pop()
		return card

	def foo():
		print("tach")


def main():
	mydeck=Deck()
	mydeck.shuffle()
	holding=[]

	liste=[]
	for i in range(5):
		card=mydeck.deal()
		holding.append(card)
		holding[i].__repr__()
		liste.append(holding[i].value)

	liste.sort()
	print(liste)
	#karte1=mydeck.deal()
	#karte1.__repr__()

main()
