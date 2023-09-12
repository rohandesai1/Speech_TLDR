import os, openai
from pathlib import Path
from dotenv import load_dotenv
from transcript import Video



class Summary:
    def __init__(self, transcript):
        path = Path(".env")
        load_dotenv(dotenv_path = path)
        openai.api_key = os.environ["openai_key"]
        self.full_transcript = transcript
        self.text_transcript = " ".join([val["text"] for val in self.full_transcript])
        
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
            def split(parts):
                try:
                    
                    texts = []
                    
                    for i,part in enumerate(parts):
                        print(f"part {i+1}")
                        if len(parts) == 1:
                            message=[{"role": "user", "content": f"marked by three dashes, there will be a transcript from a youtube video. your job is to provide a 150 word summary of the video. ---{part}---"}]
                        elif i > 0 and i < len(parts) - 1:
                            past_summary = " ".join([summ for summ in texts])
                            message=[{"role": "user", "content": f"marked by three dashes, there will be an excerpt of a transcript from a youtube video. marked with three backslashes there will be the summary so far. please continue the summary of this video based on the summary so far and the transcript. ---{part}--- |||{past_summary}|||"}]
                        elif i == 0:
                            message=[{"role": "user", "content": f"marked by three dashes, there will be an excerpt of a transcript from a youtube video. this excerpt is the start of the video. please start the summary of this youtube video based on the transcript. ---{part}---"}]
                        else:
                            past_summary = " ".join([summ for summ in texts])
                            message=[{"role": "user", "content": f"marked by three dashes, there will be an excerpt of a transcript from a youtube video. marked with three backslashes there will be the summary so far. this transcript is the final part of the youtube video, please finish the summary. ---{part}--- |||{past_summary}|||"}]

                            
                        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k-0613", messages = message, temperature = 0.0)
                        texts.append(completion.choices[0].message.content)

                    self.final = texts
                    return
                except openai.error.InvalidRequestError:
                    print("split")
                    new_parts = []
                    for part in parts:
                        new_parts.append(part[0:int(len(part)/2)])    
                        new_parts.append(part[int(len(part)/2):len(part) - 1])
                    split(new_parts)

            split([self.text_transcript])

            return " ".join(self.final)


def main():
    vid = Video(input("Enter youtube video link: "))
    transcript = vid.getTranscriptText()
    summary = Summary(transcript)
    print(summary.getSummary())
    
if __name__ == "__main__":
    main()
    
