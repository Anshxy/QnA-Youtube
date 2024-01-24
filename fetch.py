from youtube_transcript_api import YouTubeTranscriptApi
import re

class youtube_transcript:

    @staticmethod
    def fetchTranscript(url):
        """Fetches the transcript of a video given its url"""
        
        reg = re.findall(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url) # Filter for the video id using regex
        if reg:
            id = reg[0]
        else:
            raise ValueError("Invalid YouTube URL")
        
        return YouTubeTranscriptApi.get_transcript(id)

    @staticmethod
    def filter(data):
        """Filters the transcript data to only include the text"""""
        text_list = []
        for item in data:
            text_list.append(item['text'])
        return text_list

    @staticmethod
    def transcript(id):
        """Returns the transcript of a video given its id"""
        transcript_data = youtube_transcript.fetchTranscript(id)
        return youtube_transcript.filter(transcript_data)
    

youtube_transcript.fetchTranscript('https://www.youtube.com/watch?v=lhI6UpXMm6M')