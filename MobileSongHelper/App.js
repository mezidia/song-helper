import React from 'react';
import {Text, View, StyleSheet, Image, ImageBackground} from 'react-native';
import Header from "./components/Header";
import Input from "./components/Input";

const App = () => {
  return (
      <ImageBackground style={styles.backgroundContainer}>

      </ImageBackground>
  );
}

const styles = StyleSheet.create({
  backgroundContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF'
  }
})

export default App;
