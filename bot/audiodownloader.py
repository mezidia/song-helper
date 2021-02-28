import pafy
import os


def audio_downloader(url): 
    video = pafy.new(url)
    audiostreams = video.audiostreams
    for i in range(len(audiostreams)):
        if 'm4a' in str(audiostreams[i]):
            audiostreams[i].download(filepath = './bot/')
            return f'bot/{video.title}.{audiostreams[i].extension}'
