import requests
import json

#url : https://suggest-bar.daum.net/suggest?mod=json&code=utf_in_out&enc=utf&id=language&cate=eng&q=s
class search:
    def __init__(self,q,lang="eng"):    #default -> kr - eng / eng - kr
        super().__init__()
        #eng-kr : eng
        #kr-eng : eng
        #eng-eng : ene
        #kr-kr : kor
        #jp : jpn
        #chn : chn
        #한자 : han
        api_server = "https://suggest-bar.daum.net/suggest?mod=json&code=utf_in_out&enc=utf&id=language&cate={lang}&q={q}" #lang = language / q = search query
        self.result = requests.get(api_server.format(q=q,lang=lang))
    
    def __str__(self):
        if self.result.status_code == 200:
            return json.loads(self.result.text)
        else:
            return "DaumDictSearch¥¥¥"
    
    #return type :  json text

    
        

"""
#------USAGE---------
a = search("Hello!")    #default : Eng
print(a)
"""
