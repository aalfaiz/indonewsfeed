from bs4 import Comment

class HtmlCleaner:    
    def remove_comment(self, soup):
        for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
            comments.extract()

    def remove_element(self, soup, element):
        for comments in soup.findAll(element):
            comments.extract()

    def remove_tags_and_get_content(self, soup, invalid_tags):
        #invalid_tags = ['a', 'b', 'br', 'center', 'div', 'strong', 'ins']
        for tag in invalid_tags: 
            for match in soup.findAll(tag):
                match.unwrap()
