from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

class qnaModel():
    @staticmethod
    def unpack(transcript):
        """Unpacks the transcript into a string"""
        transcript_string = ''
        for item in transcript:
            transcript_string += item + ' '
        return transcript_string
    
    @staticmethod
    def trainer(transcript, question):
        model_name = 'deepset/roberta-large-squad2'

        #get predictions
        nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
        QA_input = {
            'question': f'{question}',
            'context': f'{transcript}'
        }

        res = nlp(QA_input)

        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        if res['score'] < 0.45:
            return 'Sorry, I do not know the answer to that question.'
        else:
            return res['answer'], res['score']
    
    @staticmethod
    def qna(transcript, question):
        transcript_filtered = qnaModel.unpack(transcript)
        return qnaModel.trainer(transcript_filtered, question)
        
            
       
                
    
