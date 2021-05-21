import React from 'react'
import {SafeAreaView, StyleSheet, TextInput, Dimensions} from 'react-native'
import Icon from 'react-native-vector-icons/Ionicons'
import PropTypes from 'prop-types'

const {width: WIDTH} = Dimensions.get('window')

const Input = props => {
  return (
    <SafeAreaView style={styles.inputContainer}>
      <Icon name={props.iconName} size={28} color={'rgba(255, 255, 255, 0.7)'} style={styles.inputIcon}/>
      <TextInput
        style={styles.input}
        placeholder={props.placeholder}
        placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
        underlineColorAndroid="transparent"
        multiline
        onChangeText={text => props.method(text, props.id)}
      />
    </SafeAreaView>
  )
}

Input.defaultProps = {
  iconName: 'happy-outline',
  placeholder: 'Your mood'
}

Input.propTypes = {
  iconName: PropTypes.any,
  placeholder: PropTypes.any,
  method: PropTypes.func,
  id: PropTypes.any
}

const styles = StyleSheet.create({
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
    color: 'white',
    marginTop: 10
  }
})

export default Input
