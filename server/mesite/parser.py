"""Search song on YouTube"""
from youtubesearchpython import VideosSearch


def search_youtube(value: str, parameters=None) -> dict:
    search = VideosSearch(value, **parameters)
    result = search.result()['result'][0]
    return {
        'title': result['title'],
        'duration': result['duration'],
        'views': result['viewCount']['short'],
        'link': result['link'],
    }


# params = {'limit': 1}
# r = search_youtube('python', params)
# print(r)
