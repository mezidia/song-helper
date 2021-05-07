import React from 'react';
import {Text, View, StyleSheet, Image, ImageBackground, TextInput, Dimensions} from 'react-native';
import Header from "./components/Header";
import Input from "./components/Input";

const {width: WIDTH} = Dimensions.get('window')

const App = () => {
  return (
      <ImageBackground source={{uri: 'https://i.pinimg.com/originals/b9/84/00/b98400eea2b884c8950c77d9072c6256.jpg'}}
                       style={styles.backgroundContainer}>
        <View style={styles.logoContainer}>
          <Image source={{uri: 'https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png'}}
                 style={styles.logo}/>
          <Text style={styles.logoText}>Another text</Text>
        </View>
        <View>
          <TextInput
              style={styles.input}
              placeholder={'Username'}
              placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
              underlineColorAndroid='transparent'
          />
        </View>
      </ImageBackground>
  );
}

const styles = StyleSheet.create({
  backgroundContainer: {
    flex: 1,
    width: null,
    height: null,
    justifyContent: 'center',
    alignItems: 'center'
  },
  logo: {
    width: 120,
    height: 120
  },
  logoContainer: {
    alignItems: 'center'
  },
  logoText: {
    color: 'black',
    fontSize: 20,
    fontWeight: '500',
    marginTop: 10,
    opacity: 0.5,
    textTransform: 'uppercase'
  },
  input: {
    width: WIDTH - 55,
    height: 45,
    borderRadius: 25,
    fontSize: 16,
    paddingLeft: 45,
    backgroundColor: 'rgba(0, 0, 0, 0.35)',
    color: 'rgba(255, 255, 255, 0.7)',
    marginHorizontal: 25
  }
})

export default App;
