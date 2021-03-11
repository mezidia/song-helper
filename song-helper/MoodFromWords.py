import spacy

# Load the spacy model that you have installed
nlp = spacy.load('en_core_web_md')

# process a sentence using the model
doc = nlp("I am very sad")
tokens = doc

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)

print(doc.vector)

# It's that simple - all of the vectors and words are assigned after this point
# Get the vector for 'sad':
# vector3 = doc[3].vector

# Get the mean vector for the entire sentence (useful for sentence classification etc.)\
# vector = doc.vector
