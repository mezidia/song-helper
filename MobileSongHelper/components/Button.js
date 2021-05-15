import React from 'react'
import {StyleSheet, Dimensions, TouchableOpacity, Text} from 'react-native'

const {width: WIDTH} = Dimensions.get('window')

const Button = props => {
  return (
    <TouchableOpacity style={styles.btnLogin} onPress={props.method}>
      <Text style={styles.text}>{props.text}</Text>
    </TouchableOpacity>
  )
}

Button.defaultProps = {
  text: 'happy-outline',
  method: () => console.log('Default property')
}

const styles = StyleSheet.create({
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

export default Button
