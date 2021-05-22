import requests
import json

def main():
	r=requests.get("http://127.0.0.1:9001/dummy")

	questionaire=json.loads(r.text)

	#print(questionaire)
	
	print(questionaire["type"])
	print(questionaire["instruction"])
	print(questionaire["optionset"])
	

main()
