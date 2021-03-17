from keras.models import Sequential
from keras.layers import Dense


def make_model():
    """Create Keras model"""
    # Sequential provides training and inference features on this model.
    model = Sequential()
    # Add regular densely-connected NN layer with 8 units
    model.add(Dense(8, input_dim=10, activation='relu'))
    # Add one more regular densely-connected NN layer with 4 units
    model.add(Dense(4, activation='softmax'))
    # Compile the model using sigmoid loss function and adam optimizer
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    return model
