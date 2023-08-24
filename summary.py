import os, openai
from pathlib import Path
from dotenv import load_dotenv
from transcript import Video



class Summary:
    def __init__(self, transcript):
        path = Path(".env")
        load_dotenv(dotenv_path = path)
        openai.api_key = os.environ["openai_key"]
        self.transcript = transcript
    def tokenCount(self,text):
        print(0.3679 * len(text))
        words = text
        wordLengths = []
        for word in words:
            wordLengths.append(len(word))
        avgWordLength = sum(wordLengths)/len(wordLengths)
        tokenLength = 3
        tokensPerWord = avgWordLength/tokenLength
        return tokensPerWord * len(words)
    
    def getSummary(self):
        text = f"marked by three dashes, there will be a transcript from a youtube video. your job is to provide a 150 word summary of the video. ---{self.transcript}---"
        print(self.tokenCount(text))
        message=[{"role": "user", "content": text}]
        try:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k-0613", messages = message, temperature = 0.0)
            print(completion.choices[0].message.content)
        except openai.error.InvalidRequestError:
            print("SORRY VIDEO TOO LONG. ADDING SUMMARY OF LONG-VIDEOS SOON. ")
        

def main():
    vid = Video(input("Enter youtube video link: "))
    transcript = vid.getTranscriptText()
    summary = Summary(transcript)
    summary.getSummary()
    
if __name__ == "__main__":
    main()
    
