import React from 'react';
import {Text, View, StyleSheet, TextInput} from 'react-native';

const Input = () => {
  return (
      <View>
        <TextInput multiline='true' placeholder='useless placeholder' width='40' height='100'/>
      </View>
  );
}

export default Input;
