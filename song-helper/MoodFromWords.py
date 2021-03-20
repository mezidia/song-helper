import spacy as sp

class MoodOfWords:
    """
    This class receives sentences from the user and analyzes them
    for belonging to one of the four emotions:
    Happy, Sad, Calm (Neutral) and Energetic (Angry)
    Returns:
        [Mood]: [emotional represantion of sentences]
    """

    # Load the spacy model that you have installed
    nlp = sp.load('en_core_web_sm')

    # User text
    # There You should read input
    user_text = "This is how John Walker was walking. He was also running beside the lawn."

    # Load text as spacy component
    doc = nlp(user_text)

def create_tokens(doc):
    token_list = [token for token in doc]
    print(type(token_list))

#    def lemmatize():

