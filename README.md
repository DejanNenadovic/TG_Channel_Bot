# README.md - Telegram Forward and Send Bot

This python script can make a telegram "bot" that I can have enter ~50 public TG groups and forward all the messages from all the groups into one centralized TG. I then want a bot in that TG to forward the messages to a second TG which which will have other people in it.

The purpose of the two groups is I not want people to be able to tell who/what is forwarding the messages from the different rooms, otherwise that entity will get kicked out of those rooms.

## Table of Contents

-forwardbot.py
-sendbot.py
-.env

processing-result
-night.session(is created while forwardbot.py is performing)
-fury.session(is created while sendbot.py is performing)

## Requirements

- Fill to .env file  reference: https://my.telegram.org/apps

  API_ID = "2163410"
  API_HASH = "3d63708646c1231212312338b27b5adb34d3"
  SOURCE_GROUP_CENTER = "@Room1_CenterGroup"
  TARGET_GROUP_FINAL = "@Room2_TargetGroup"
  PHONE_NUMBER = "12062128541"

- Delete to run scripts if following files exist

  night.session
  fury.session

## Usage

1. run forwardbot.py
2. run sendbot.py
