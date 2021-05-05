import aiohttp


async def make_request(mood_text: str) -> dict:
    """
    Function that makes request to server and gets link
    :param mood_text: text from input field
    :return: link to youtube video with song
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.github.com/users/{mood_text}') as response:
            return await response.json()
