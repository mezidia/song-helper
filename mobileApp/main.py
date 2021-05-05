from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.lang import Builder
import styles
import utils
import asyncio

import webbrowser

Window.size = (350, 400)
Window.clearcolor = (43 / 255, 76 / 255, 186 / 255, 1)


class MainApp(MDApp):
    def __init__(self):
        """
        Constructor for class. Set all elements here
        """
        super().__init__()
        self.greeting_label = Builder.load_string(styles.Label)
        self.input_data = Builder.load_string(styles.TextField)
        self.search_button = MDFlatButton(text='Search the user in GitHub API',
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          on_release=self.input_btn_callback)
        self.result_link = MDFlatButton(text='[b]Here[/b] will be your link', markup=True,
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.link_btn_callback)

    def input_btn_callback(self, instance):
        """
        Callback for input button
        :param instance: required parameter, but not used
        :return: nothing to return
        """
        input_text = self.input_data.text
        if not input_text:
            self.result_link.text = 'Enter the nickname'
        else:
            loop = asyncio.get_event_loop()
            link = loop.run_until_complete(utils.make_request(input_text))
            self.input_data.text = ''
            try:
                self.result_link.text = link['html_url']
            except KeyError:
                self.result_link.text = 'This user is not found'

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
        self.title = 'Song Helper'
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
        screen = MDScreen()
        mainBox = MDBoxLayout(orientation='vertical')
        mainBox.add_widget(Builder.load_string(styles.Toolbar))
        mainBox.add_widget(self.greeting_label)
        mainBox.add_widget(self.input_data)
        mainBox.add_widget(self.search_button)
        mainBox.add_widget(self.result_link)

        screen.add_widget(mainBox)
        return screen


if __name__ == '__main__':
    MainApp().run()
