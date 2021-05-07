import React from 'react';
import {Text, View, StyleSheet, Image, ImageBackground, TextInput, Dimensions, TouchableOpacity} from 'react-native';
import Icon from "react-native-vector-icons/Ionicons";

const {width: WIDTH} = Dimensions.get('window')

const App = () => {
  return (
      <ImageBackground source={{uri: 'https://i.pinimg.com/originals/b9/84/00/b98400eea2b884c8950c77d9072c6256.jpg'}}
                       style={styles.backgroundContainer}>
        <View style={styles.logoContainer}>
          <Image source={{uri: 'https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png'}}
                 style={styles.logo}/>
          <Text style={styles.logoText}>Song helper</Text>
        </View>
        <View style={styles.inputContainer}>
          <Icon name={'happy-outline'} size={28} color={'rgba(255, 255, 255, 0.7)'} style={styles.inputIcon}/>
          <TextInput
              style={styles.input}
              placeholder={'Your mood'}
              placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
              underlineColorAndroid='transparent'
          />
        </View>
        <View style={styles.inputContainer}>
          <Icon name={'md-musical-notes-outline'} size={28} color={'rgba(255, 255, 255, 0.7)'} style={styles.inputIcon}/>
          <TextInput
              style={styles.input}
              placeholder={'Spotify song id'}
              placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
              underlineColorAndroid='transparent'
          />
        </View>
        <TouchableOpacity style={styles.btnLogin}>
          <Text style={styles.text}>Login</Text>
        </TouchableOpacity>
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
    alignItems: 'center',
    marginBottom: 50
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
  },
  inputIcon: {
    position: 'absolute',
    top: 8,
    left: 37
  },
  inputContainer: {
    marginTop: 10
  },
  btnLogin: {
    width: WIDTH - 55,
    height: 45,
    borderRadius: 25,
    backgroundColor: '#432577',
    justifyContent: 'center',
    marginTop: 20
  },
  text: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: 16,
    textAlign: 'center'
  }
})

export default App;
