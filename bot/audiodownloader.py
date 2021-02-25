import pafy
import os


def audio_downloader(url): 
    type_of_audio_file = 3
    video = pafy.new(url)
    audiostreams = video.audiostreams
    audiostreams[type_of_audio_file].download(filepath = './bot/')
    return f'bot/{video.title}.{audiostreams[type_of_audio_file].extension}'
