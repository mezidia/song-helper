import React, {Component} from 'react'
import {Text, View, StyleSheet, Image, ImageBackground, Alert, Linking} from 'react-native'
import Input from './components/Input'
import Button from './components/Button'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      moodText: '',
      songId: '',
    }
  }

  updateState = (text, type) => {
    if (type === 'first') this.setState({moodText: text})
    else if (type === 'second') this.setState({songId: text})
  }
  makeRequest = async (link) => {
    let result = ''
    try {
      await fetch(link)
        .then(res => res.json())
        .then(json => result = json)
    } catch (e) {
      this.alertNoResult()
    }
    return result
  }
  alertNoResult = () => {
    Alert.alert('No result', 'Press any button to continue', [
      {text: 'Ok', onPress: () => console.log('Yes button')},
      {text: 'Cancel', onPress: () => console.log('No button')}
    ])
  }
  alertEmptyMessage = () => {
    Alert.alert('Empty message', 'Enter the text', [
      {text: 'Ok', onPress: () => console.log('Yes button')},
      {text: 'Cancel', onPress: () => console.log('No button')}
    ])
  }
  searchBtnPress = async () => {
    if (this.state.moodText) {
      let result = await this.makeRequest(`https://api.github.com/users/${this.state.moodText}`)
      console.log(result)
      Alert.alert('Your result', 'Press OK to open', [
        {text: 'Ok', onPress: async () => await Linking.openURL(result.html_url)},
        {text: 'Cancel', onPress: () => console.log('No button')}
      ])
    } else {
      this.alertEmptyMessage()
    }
  };
  addBtnPress = async () => {
    if (this.state.songId) {
      let result = await this.makeRequest(`https://jsonplaceholder.typicode.com/posts/${this.state.songId}`)
      console.log(result)
      Alert.alert('Your result', 'Press OK to open', [
        {text: 'Ok', onPress: async () => await Linking.openURL(result.id)},
        {text: 'Cancel', onPress: () => console.log('No button')}
      ])
    } else {
      this.alertEmptyMessage()
    }
  };

  render() {
    return (
      <ImageBackground source={{uri: 'https://i.pinimg.com/originals/b9/84/00/b98400eea2b884c8950c77d9072c6256.jpg'}}
        style={styles.backgroundContainer} blurRadius={4}>
        <View style={styles.logoContainer}>
          <Image
            source={{uri: 'https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png'}}
            style={styles.logo}/>
          <Text style={styles.logoText} onPress={() => Linking.openURL('https://github.com/mezidia/song-helper')}>Song
              helper</Text>
        </View>
        <Input iconName={'happy-outline'} placeholder={'Your mood'} method={this.updateState} id={'first'}/>
        <Input iconName={'md-musical-notes-outline'} placeholder={'Spotify song id'} method={this.updateState}
          id={'second'}/>
        <Button text={'Search song'} method={this.searchBtnPress}/>
        <Button text={'Add song'} method={this.addBtnPress}/>
      </ImageBackground>
    )
  }
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
  }
})

export default App
