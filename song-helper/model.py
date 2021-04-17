from keras.models import Sequential
from keras.layers import Dense


def make_model():
    """Create Keras model"""
    # Sequential provides training and inference features on this model.
    model = Sequential()
    model.add(Dense(8, input_dim=10, activation='relu'))
    model.add(Dense(4, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    return model
