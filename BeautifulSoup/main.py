from bs4 import BeautifulSoup
import requests


url = "https://eng.auburn.edu/csse/academics/online/online-undergraduate-program.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.find_all("tbody"))
#print(doc.prettify())

test = doc.find_all("li")
#print(test)



