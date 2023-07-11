from youtube_transcript_api import YouTubeTranscriptApi

class Video:
    def __init__(self, link):
        self.link = link
        self.ID = link[link.index("=") + 1:]
    
    def getTranscriptText(self):
        transcript = YouTubeTranscriptApi.get_transcript(self.ID)
        transcriptText = ""
        for entry in transcript:
            transcriptText += " " + entry["text"]
        
        return transcript

link = input("Link: ")
vid = Video(link)
print(vid.getTranscriptText())
# aw

"""

url = "https://gpt-summarization.p.rapidapi.com/summarize"

info = {"text" : transcriptText, "num_sentences" : 20}

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "707002898dmshcc9f17c8e05c13dp1c3471jsn4a5c26b80ae6",
	"X-RapidAPI-Host": "gpt-summarization.p.rapidapi.com"
}

response = requests.post(url, json=info, headers=headers)

print(response.json())"""