import React from 'react';
import {Text, View, StyleSheet, Image, ImageBackground} from 'react-native';
import Header from "./components/Header";
import Input from "./components/Input";

const App = () => {
  return (
      <ImageBackground source={'https://i.pinimg.com/originals/b9/84/00/b98400eea2b884c8950c77d9072c6256.jpg'}
                       style={styles.backgroundContainer}>
        <View style={styles.logoContainer}>
          <Image source={'https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png'}
                 style={styles.logo}/>
          <Text style={styles.logoText}>Song helper</Text>
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
  }
})

export default App;
