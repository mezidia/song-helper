import spacy as sp
import csv
import os
import random

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

def load_training_data(
    data_directory: str = "song-helper\docs\OurData.csv",
    split: float = 0.8,
    limit: int = 0
) -> tuple:
    # Load from file
    reviews = []
    for label in ["HAPPY", "SAD", "CALM", "ENERGETIC"]:
        text = str.read()
        if text.strip():
            spacy_label = {
                "cats": {
                    "HAPPY": "HAPPY" == label,
                    "SAD": "SAD" == label,
                    "CALM": "CALM" == label,
                    "ENERGETIC": "ENERGETIC" == label}
            }
            reviews.append((text, spacy_label))
    random.shuffle(reviews)

    if limit:
        reviews = reviews[:limit]
    split = int(len(reviews) * split)
    return reviews[:split], reviews[split:]

