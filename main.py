import requests 
import bs4 
text= input("What Should i seach Boss")
url = 'https://google.com/search?q=' + text  
request_result=requests.get( url )  
soup = bs4.BeautifulSoup(request_result.text, "html.parser") 
heading_object=soup.find_all( 'h3' ) 
for info in heading_object: 
  print(info.getText()) 

heading_object=soup.find_all('a' ,href=True) 
for info in heading_object: 
    fullstring = info['href']
    substring = "/url"

    if fullstring.find(substring) != -1:
      links = info['href'].replace("/url?q=",'').split("&sa")
      print(links[0])
