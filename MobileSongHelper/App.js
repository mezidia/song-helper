import React, {Component} from 'react';
import {Text, View, StyleSheet, Image, ImageBackground, Dimensions, TouchableOpacity, Alert} from 'react-native';
import Input from "./components/Input";

const {width: WIDTH} = Dimensions.get('window')

class App extends Component {
  state = {
    myState: 'This is a text component, created using state data. It will change or updated on clicking it.'
  }
  btnPress = async () => {
    await fetch('https://api.github.com/users/mezgoodle')
        .then(res => res.json())
        .then(json => console.log(json))
    Alert.alert('Your result', 'Main message', [
      {text: 'Ok', onPress: () => console.log('Yes button')},
      {text: 'Cancel', onPress: () => console.log('No button')}
    ]);
  };

  render() {
    return (
        <ImageBackground source={{uri: 'https://i.pinimg.com/originals/b9/84/00/b98400eea2b884c8950c77d9072c6256.jpg'}}
                         style={styles.backgroundContainer} blurRadius={4}>
          <View style={styles.logoContainer}>
            <Image
                source={{uri: 'https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png'}}
                style={styles.logo}/>
            <Text style={styles.logoText}>Song helper</Text>
          </View>
          <Input iconName={'happy-outline'} placeholder={this.state.myState}/>
          <Input iconName={'md-musical-notes-outline'} placeholder={'Spotify song id'}/>
          <TouchableOpacity style={styles.btnLogin} onPress={this.btnPress}>
            <Text style={styles.text}>Login</Text>
          </TouchableOpacity>
        </ImageBackground>
    )
  };
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
