"""Search song on YouTube"""
from youtubesearchpython import VideosSearch


def search_youtube(value: str, parameters=None) -> dict:
    """
    Function to search only first video on YouTube
    :param value: what we need to search
    :param parameters: some parameters, such as limit, language, region
    :return: dictionary with main information
    """
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
