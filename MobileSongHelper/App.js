import React from 'react';
import {Text, View, StyleSheet, Image} from 'react-native';
import Header from "./components/Header";

const App = () => {
  return (
      <View style={styles.container}>
        <Header title='Song helper' />
        <Image
            source={{uri: 'https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png'}}
            style={styles.img}/>
      </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    paddingTop: 60
  },
  img: {
    width: 100,
    height: 100
  }
})

export default App;
