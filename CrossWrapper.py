from sentence_transformers import CrossEncoder
import json

class CrossEncoderWrapper():
    def __init__(self,answers_path="./Answers.json",model_name="cross-encoder/nli-deberta-v3-base") -> None:
        self.model_name=model_name
        self.answers_path=answers_path
        self.model=CrossEncoder(model_name)
        with open(answers_path,'r',encoding='utf-8') as answersfile:
            self.answers=json.loads(answersfile.read())
    
    
    def rerank(self,results:dict[str,float],query:str):
        
        for result in results:
            print(self.answers[result])
            
            

    