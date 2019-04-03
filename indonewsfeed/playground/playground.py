from bs4 import BeautifulSoup



with open('sample.html') as file:  
    html_doc = file.read()

soup = BeautifulSoup(html_doc,'html.parser')

invalid_tags = ['a', 'b', 'br', 'center', 'div', 'strong', 'ins']
for tag in invalid_tags: 
    for match in soup.findAll(tag):
        match.unwrap()


print(soup.prettify())