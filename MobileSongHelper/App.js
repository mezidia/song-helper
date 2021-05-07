import {StatusBar} from 'expo-status-bar';
import React from 'react';
import {Text, View, StyleSheet, Image} from 'react-native';

export default function App() {
  return (
      <View style={styles.container}>
        <Text style={styles.text}>Hello world!</Text>
        <StatusBar style="auto"/>
        <Image
            source={{uri: 'https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png'}}
            style={styles.img}/>
      </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  text: {
    color: 'darkslateblue',
    fontSize: 30
  },
  img: {
    width: 100,
    height: 100
  }
})
