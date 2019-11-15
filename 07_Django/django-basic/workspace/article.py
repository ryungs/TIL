class Model:
    def __init__():
        # Init 
    def save(self):
        # CREATE RECORD IN DB
    def get(self):
        # READ RECORD FROM DB
    
class Article:
    title =''
    content = ''
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    
a = Article('오늘 메뉴 뭐임?', '제발 맛있는거ㅜㅜ')


class Comment:
    article_id = None
    content = ''
    def __init__(self, article_id, content):
        self.article_id = article_id    
        self.content = content