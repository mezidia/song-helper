from keras.models import Sequential
from keras.layers import Dense


def make_model():
    # Create the model
    model = Sequential()
    # Add 1 layer with 8 nodes,input of 4 dim with relu function
    model.add(Dense(8, input_dim=10, activation='relu'))
    # Add 1 layer with output 3 and softmax function
    model.add(Dense(4, activation='softmax'))
    # Compile the model using sigmoid loss function and adam optim
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    return model
