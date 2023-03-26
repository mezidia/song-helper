<h1 id="project-title" align="center">
  Song Helper <img alt="logo" width="40" height="40" src="https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png" /><br>
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mezidia/song-helper.svg?style=flat-square&logo=github&logoColor=white">
  <img alt="language" src="https://img.shields.io/badge/language-python-brightgreen?style=flat-square" />
  <img alt="language" src="https://img.shields.io/github/issues/mezgoodle/song-helper?style=flat-square" />
  <img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/mezgoodle/song-helper?style=flat-square" />
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mezgoodle/song-helper?style=flat-square" />
  <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/mezgoodle/song-helper?style=flat-square" />
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/mezgoodle/song-helper?style=flat-square" />
  <img alt="Latest Github release" src="https://img.shields.io/github/release/mezgoodle/song-helper?style=flat-square" />
  <img alt="Theme" src="https://img.shields.io/badge/Theme-AI-brightgreen?style=flat-square" />
</h1>

<p align="center">
 🌟Hello everyone! This is Our repository about project on Python "Song-Helper"🌟
</p>

## Overview

This project isn't deployed, and some parts of code could don't work...but main idea is realised. Here you can see work server on _Django_, bot on _Aiogram_, AI on _Keras_ and _Tensorflow_, mobile app on _React Native_.

## Specification

### Context
-----------

This project is developing by 4 members of Mezidia: 
- Zavalniuk Maxim and Dominskyi Valentyn - AI
- Sichkar Tetiana - Website
- Dmytrenko Roman - Telegram Bot

It is planned to deploy the project in the form of a server on the Django web framework

### Tasks
---------

This project will give You some music depending on Your mood, which will be represented by You as a words.

AI won't create any sort of music depending on Your mood

### Functional requirements
-----------------------

The only functional requirement is to give a song. In additional anyone can add new songs in the database of AI model.

### Scenarios
-----------

- We get a description of the mood in _different ways_: through a **bot** (Telegram, Discord) in the form of a text message, through a form on the **site** (Django) , through a form on the **mobile app** (React Native). Next, the text is converted to a vector, compared with the mood vectors, getting a random song with this mood from databae and the result is returned as a song reference (in each cases).
- The site will have one more page with a form for entering a song id from _Spotify_. This is for making database bigger. Also you can do it from bots in Telegram and Discord.

### Use case diagram
-----------
![Use case diagram](https://user-images.githubusercontent.com/54878089/226972900-7c445e7f-54bf-4352-97f3-f80e4021592a.png)

## Build status :hammer:

[![Bot CI](https://github.com/mezidia/song-helper/actions/workflows/bot.yml/badge.svg)](https://github.com/mezidia/song-helper/actions/workflows/bot.yml)
[![Docker](https://github.com/mezidia/song-helper/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/mezidia/song-helper/actions/workflows/docker-publish.yml)
[![Docker Image CI](https://github.com/mezidia/song-helper/actions/workflows/docker-image.yml/badge.svg)](https://github.com/mezidia/song-helper/actions/workflows/docker-image.yml)
[![song-helper CI](https://github.com/mezidia/song-helper/actions/workflows/song-helper.yml/badge.svg)](https://github.com/mezidia/song-helper/actions/workflows/song-helper.yml)
[![Django CI](https://github.com/mezidia/song-helper/actions/workflows/django.yml/badge.svg)](https://github.com/mezidia/song-helper/actions/workflows/django.yml)
[![Mobile App CI](https://github.com/mezidia/song-helper/actions/workflows/mobile-app.yml/badge.svg)](https://github.com/mezidia/song-helper/actions/workflows/mobile-app.yml)

## Tech/framework used :wrench:

**Built with**

- [Django](https://www.djangoproject.com/)
- [NumPy](https://numpy.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [aiogram](https://github.com/aiogram/aiogram)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [React Native](https://reactnative.dev/)
- [pandas](https://pandas.pydata.org/)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Docker](https://www.docker.com/)

## Installation :computer:

To install our project and use it, enter the following command: docker-compose up.

## Tests :microscope:

We use [unittest](https://docs.python.org/3/library/unittest.html) as framework for testing. All results you can see [here](https://github.com/mezidia/song-helper/actions). For tests look in folders of each part of this project.

## Contribute :running:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](link).

## Credits :cat::handshake:

| <a href="https://github.com/mezgoodle" target="_blank">**Mezgoodle⭐️**</a> | <a href="https://github.com/Dmytrenko-Roman" target="_blank">**Dmytrenko-Roman**</a> | <a href="https://github.com/fhrr-sht" target="_blank">**Fhrr-sht**</a> | <a href="https://github.com/VsIG-official" target="_blank">**VsIG**</a> |
| :---: |:---:| :---:| :---: |
| [![Mezgoodle](https://avatars.githubusercontent.com/u/41520940?s=400&u=530e013f3714e81792fc6b99399c7a6eda6ea63d&v=4)](https://github.com/mezgoodle) | [![Dmytrenko-Roman](https://avatars.githubusercontent.com/u/54878089?s=400&u=075796965fc5db27cc5b6b179b9325bf312ce0b9&v=4)](https://github.com/Dmytrenko-Roman) | [![Fhrr-Sht](https://avatars.githubusercontent.com/u/54956154?s=400&v=4)](https://github.com/fhrr-sht) | [![VsIG](https://avatars0.githubusercontent.com/u/50269023?s=400&u=522283a8fce57866b73427f94a742fb83e0b1b40&v=4)](https://github.com/VsIG-official)  |
| <a href="https://github.com/mezgoodle" target="_blank">`github.com/mezgoodle`</a> | <a href="https://github.com/Dmytrenko-Roman" target="_blank">`github.com/Dmytrenko-Roman`</a> | <a href="https://github.com/fhrr-sht" target="_blank">`github.com/fhrr-sht`</a> | <a href="https://github.com/VsIG-official" target="_blank">`github.com/VsIG-official`</a> |

## License :bookmark:

MIT © [Mezidia](https://github.com/mezidia)
