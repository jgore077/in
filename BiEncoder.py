from sentence_transformers import SentenceTransformer
import numpy as np
import tqdm
import json
import re

 
def remove_html_tags(text): 
    clean = re.compile('<.*?>') 
    return re.sub(clean, '', text) 
 
 
class BiEncoder():
    def __init__(self,answers_file,model_name="all-MiniLM-L6-v2",embeddings_file="embeddings.np") -> None:
        self.model_name=model_name
        self.embeddings_file=embeddings_file
        self.answers_file=answers_file
        self.model=SentenceTransformer(model_name)
        with open(self.answers_file,'r',encoding='utf-8') as answersfile:
            self.answers=json.loads(answersfile.read())
        try:
            with open(self.embeddings_file,'r',encoding='utf-8') as embeddingsfile:
                pass
        except:
            self._create_embeddings()
            
    def _create_embeddings(self):
        embeddings=[]
        # Iterate over answers and encode the text without no html
        for answer in tqdm.tqdm(self.answers):
            embeddings.append(self.model.encode(remove_html_tags(answer["Text"])))
            
        # Write embeddings back out to file
        np.save(self.embeddings_file,embeddings)
            
    def search(self,query):
        pass
    
    
if __name__=="__main__":
    encoder=BiEncoder("./Answers.json")