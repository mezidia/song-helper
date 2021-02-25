import pafy
import os


def audio_downloader(url): 
    type_of_audio_file = 1
    video = pafy.new(url)
    audiostreams = video.audiostreams
    print(audiostreams)
    audiostreams[type_of_audio_file].download(filepath = './bot/')
    return f'bot/{video.title}.{audiostreams[type_of_audio_file].extension}'

audio_downloader('https://www.youtube.com/watch?v=YAZGKbAp36E')