# for Accurate (main)
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download en_core_web_trf
# for faster
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download en_core_web_sm

import spacy

# Load the spacy model that you have installed
nlp = spacy.load('en_core_web_trf')

# process a sentence using the model
doc = nlp("Sad")

# It's that simple - all of the vectors and words are assigned after this point
# Get the vector for 'text':
doc[3].vector

# Get the mean vector for the entire sentence (useful for sentence classification etc.)\
doc.vector
print("Some")
