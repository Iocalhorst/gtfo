import myclasses
import requests
import sys
import os

#java serialized object notation
import json
text="bla"
text2='bla'

class Karteikarte():
	def __init__(self,data,debug):
		self.data=data
		self.debug=debug
		if self.debug==True:
			print("initmethode aufgerufen")

url=""
port=""

def main():
#	myinterface=Consoleninterface()

	data1={"2q4w35sefukzt":"foo","backpage":"bar","uid":"abc"}
	print("data1 :",data1)
	data2={"frontpage":"123","backpage":"456","uid":"xyz"}
	print("data2 :",data2)
	karteikarten=[]
	print("karteikarten :",karteikarten)
	karteikarte1=Karteikarte(data1,True)
	karteikarte2=Karteikarte(data2,False)
	karteikarten.append(data1)
	karteikarten.append(data2)


	#var1={"a","b",42,23}
	#print(var1)
	
	tup=tuple(karteikarten)

	print("nochmal das deck :",tup)

	json_string=json.dumps(tup)

	print(json_string)
	

main()
