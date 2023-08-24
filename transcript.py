from youtube_transcript_api import YouTubeTranscriptApi

class Video:
    def __init__(self, link : str):
        self.link = link
        self.ID = link[link.index("=") + 1:]
    
    def getTranscriptText(self) -> str:
        transcript = YouTubeTranscriptApi.get_transcript(self.ID)
        transcriptText = ""
        for entry in transcript:
            transcriptText += " " + entry["text"]
        
        return transcript


if __name__ == "__main__":
    link = input("Link: ")
    vid = Video(link)
    print(vid.getTranscriptText())

