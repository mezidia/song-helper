import React from 'react';
import {Text, View, StyleSheet, Image} from 'react-native';

const Header = props => {
  return (
      <View style={styles.header}>
        <Text style={styles.text}>{props.title}</Text>
      </View>
  );
}

const styles = StyleSheet.create({
  header: {
    height: 60,
    padding: 15,
    backgroundColor: 'darkslateblue'
  },
  text: {
    color: '#fff',
    fontSize: 23,
    textAlign: 'center'
  }
})

export default Header;
