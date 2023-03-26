from moviepy.editor import AudioFileClip
from pytube import YouTube


def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    return youtubeObject.download()


def convert_to_mp3(mp4, mp3):
    file = AudioFileClip(mp4)
    file.write_audiofile(mp3)
    file.close()
