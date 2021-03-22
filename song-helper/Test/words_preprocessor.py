# Load english for parsing
from spacy.lang.en import English


class WordPreprocessor:
    """[summary]

    Returns:
        [type]: [description]
    """
    # Basic function to clean the text
    def clean_text(self, text):
        return text.strip().lower()
