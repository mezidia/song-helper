from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

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
        self.button.bind(on_press=self.btn_callback)
        self.input_data = TextInput(hint_text='Text your mood here', multiline=True)
        self.link = Label(text='')

    def btn_callback(self, instance):
        # TODO: check if input is not blank
        """
        Callback for out button
        :param instance: required parameter, but not used
        :return: nothing to return
        """
        data = self.input_data.text
        print(f'The data {data}')
        self.input_data.text = ''
        self.link.text = data

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

    def make_request(self, mood_text: str) -> str:
        # TODO: Write logic for this function. Make requests with https://docs.python-requests.org/en/master/. Maybe
        #  async
        """
        Function that makes request to server and gets link
        :param mood_text: text from input field
        :return: link to youtube video with song
        """
        pass


if __name__ == '__main__':
    MainApp().run()
