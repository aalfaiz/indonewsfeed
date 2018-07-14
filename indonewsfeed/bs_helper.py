from bs4 import Comment

class HtmlCleaner:    
    def remove_comment(self, soup):
        for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
            comments.extract()

    def remove_element(self, soup, element):
        for comments in soup.findAll(element):
            comments.extract()
