from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.lang import Builder
import styles
import asyncio
import aiohttp

import webbrowser

Window.size = (350, 400)
Window.clearcolor = (43 / 255, 76 / 255, 186 / 255, 1)


class MainApp(MDApp):
    def __init__(self):
        """
        Constructor for class. Set all elements here
        """
        super().__init__()
        self.label = Builder.load_string(styles.Label)
        self.input_data = Builder.load_string(styles.TextField)
        self.button = MDFlatButton(text='Search the user in GitHub API', pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.input_btn_callback)
        self.link = MDFlatButton(text='[b]Here[/b] will be your link', markup=True, pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.link_btn_callback)

    def input_btn_callback(self, instance):
        """
        Callback for input button
        :param instance: required parameter, but not used
        :return: nothing to return
        """
        input_text = self.input_data.text
        if not input_text:
            self.link.text = 'Enter the nickname'
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
            instance.text = 'Try another one'
        else:
            instance.text = 'This is not a link'

    def mark_icon_callback(self, instance):
        """
        Callback for link button
        :param instance: required parameter
        :return: nothing to return
        """
        webbrowser.open_new_tab('https://google.com.ua')

    def build(self):
        """
        Override build function
        :return: box layout
        """
        # TODO: Make label, input, button in layouts and add to screen them
        self.title = 'Song Helper'
        self.theme_cls.primary_palette='Blue'
        self.theme_cls.theme_style = 'Dark'
        screen = MDScreen()
        box = MDBoxLayout(orientation='vertical')
        box.add_widget(Builder.load_string(styles.Toolbar))
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.button)
        box.add_widget(self.link)

        screen.add_widget(box)
        return screen


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
