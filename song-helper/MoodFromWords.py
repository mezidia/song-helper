import spacy as sp

# class MoodOfWords:
#     """
#     This class receives sentences from the user and analyzes them
#     for belonging to one of the four emotions:
#     Happy, Sad, Calm (Neutral) and Energetic (Angry)
#     Returns:
#         [Mood]: [emotional represantion of sentences]
#     """

# Load the spacy model that you have installed
nlp = sp.load('en_core_web_sm')

# User text
# There You should read input
user_text = "This is how John Walker was walking. He was also running beside the lawn."

# Load text as spacy component
doc = nlp(user_text)

# Create tokens
token_list = [token for token in doc]
print(token_list)

# Create and filter tokens
filtered_tokens = [token for token in doc if not token.is_stop]
print(filtered_tokens)

# Lemmanization
lemmas = [
    f"Token: {token}, lemma: {token.lemma_}"
    for token in filtered_tokens
]
print(lemmas)

#    def lemmatize():

