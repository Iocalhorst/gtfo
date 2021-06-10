import requests
import re

url="http://www.volkerito.de/"

def parse(text_to_search):
    matches = re.findall(r'href=[\'"]?([^\' >]+)', text_to_search)
    return matches

def main():
    response=requests.get(url)
    print(" Status Code : ", response.status_code,'\n')
    print("header : ", response.headers,'\n')
    #print("Content as UTF-8  :","/n", response.text)

    links=parse(response.text)
    for link in links :
        print(link)

main()