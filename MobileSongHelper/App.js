import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View style={{flex: 1, justifyContent: 'center', alignItems: 'center'}}>
      <Text style={{color: 'darkslateblue', fontSize: 30}}>Hello world!</Text>
      <StatusBar style="auto" />
    </View>
  );
}
