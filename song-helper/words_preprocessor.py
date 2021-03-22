class WordPreprocessor:
    """
    Class for preprocessing some text for future use
    """
    # Basic function to clean the text
    def clean_text(self, text):
        return text.strip().lower()
