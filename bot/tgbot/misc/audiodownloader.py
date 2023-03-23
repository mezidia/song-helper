import pafy


def audio_downloader(url: str) -> str:
    """
    Download music by url and return path to the downloaded file
    :param url: url address of the song
    :return: path to the downloaded path
    """
    video = pafy.new(url)
    audiostreams = video.audiostreams
    for i in range(len(audiostreams)):
        if 'm4a' in str(audiostreams[i]):
            audiostreams[i].download(filepath='./bot/')
            return f'bot/{video.title}.{audiostreams[i].extension}'
