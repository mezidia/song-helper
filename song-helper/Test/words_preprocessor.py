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

    def spacy_tokenizer(self, sentence):
        parser = English()
        mytokens = parser(sentence)
        mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
        return mytokens