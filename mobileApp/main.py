from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import asyncio
import aiohttp

import webbrowser

Window.size = (250, 300)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)


class MainApp(App):
    def __init__(self):
        """
        Constructor for class. Set all elements here
        """
        super().__init__()
        self.label = Label(text='Enter your mood', font_size='20sp', bold=True)
        self.button = Button(text='Search the song', background_color=(0, 0, 0, 0))
        self.button.bind(on_press=self.input_btn_callback)
        self.input_data = TextInput(hint_text='Text your mood here', multiline=True)
        self.link = Button(text='[b]Here[/b] will be your link', markup=True, background_color=(0, 0, 0, 0))
        self.link.bind(on_press=self.link_btn_callback)

    def input_btn_callback(self, instance):
        """
        Callback for input button
        :param instance: required parameter, but not used
        :return: nothing to return
        """
        input_text = self.input_data.text
        if not input_text:
            self.link.text = 'Enter the mood'
        else:
            loop = asyncio.get_event_loop()
            link = loop.run_until_complete(make_request(input_text))
            self.input_data.text = ''
            try:
                self.link.text = link['html_url']
            except KeyError:
                self.link.text = 'This user is not found'

    def link_btn_callback(self, instance):
        """
        Callback for link button
        :param instance: required parameter
        :return: nothing to return
        """
        if instance.text.startswith('https://'):
            webbrowser.open_new_tab(instance.text)
        else:
            instance.text = 'This is not a link'

    def build(self):
        """
        Override build function
        :return: box layout
        """
        self.title = 'Song Helper'
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.button)
        box.add_widget(self.link)

        return box


async def make_request(mood_text: str) -> dict:
    """
    Function that makes request to server and gets link
    :param mood_text: text from input field
    :return: link to youtube video with song
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.github.com/users/{mood_text}') as response:
            return await response.json()


if __name__ == '__main__':
    MainApp().run()
