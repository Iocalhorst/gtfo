import json

class Db():
	def __init__(self,name):
		self.name=name
		self.data={}

	def __query__(self):
		pass


class Entry():
	def __init__(self,uid,description,data,meta):
		self.uid=uid
		self.data=data
		self.meta=meta
		self.description=description


def main():
	




	s1="Im tiefen dichten Fichtendickicht dichten Dicke nüchten tüchtig."
	s2="Wer andern eine Bratwurst brät der hat ein Bratwurstbratgerät"
	s3="Informatik ist toll. Nur das mit den Computern nervt."
	s4="Wer niemals Keks im Bette aß weiss nicht wie Krümel pieken"
	s5="In der Ruhe liegt die Kraft. Und in der Truhe liegt der Schnaps"

	statement={1:s1,2:s2,3:s3,4:s4,5:s5}


	meta={"name":"dummy"}
	description={"text":"statement to validate"}
	data={"text":s1,"tags":{"text":"testtag"}}
	newid={"uid":1}

	
#	s1=Entry(newid,description,data,meta)

#	data={"text":s2,"tags":{"text":"testtag2"}}
#	newid={"uid":"2"}

#	s2=Entry(newid,description,data,meta)

#	data={"text":s3,"tags":{"text":"testtag3"}}
#	s3=Entry({"uid":"3"},description,data,meta)
#
#	data={"text":s4,"tags":{"text":"testtag4"}}
#	s4=Entry({"uid":"4"},description,data,meta)

#	data={"text":s5,"tags":{"text":"testtag5"}}
#	s5=Entry({"uid":"5"},description,data,meta)

	


	lässt sich die stelle der leitungsunterbrechung mittels traceroute ermitteln?
	

	instruction="Waehlen sie die zutreffende Aussage aus."
	optionset={1:s1,2:s2,3:s3,4:s4,5:s5}


	#s_list=[s1,s2,s3,s4,s5]
	#optionset={}
	#for i in range(len(s_list)):
	#	options={"id":i,"text":s_list[i].data["text"]}
	
	
		

	#optionset=tuple(optionset)

	testfrage={"type":"mc5","instruction":instruction,"optionset":optionset}


	j=json.dumps(testfrage)

	file=open("dummy.json","w")
	file.write(j)
	file.close() 

		
	#print(statement.json)


main()




