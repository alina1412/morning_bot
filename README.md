# Telegram Morning bot

### (in the process of updating)

## Description

Sends to a subscriber a random picture or a temperature in Moscow at the morning. Asks a user to choose one of those options (the choice can be changed).

## Usage

To start a bot user types "/start".

Then he gets a keyboard with options what morning information he wants to receive from bot.

## Structure

```py
.env.example                    # environmental variables - token for 
                                # telegram and sites.
.gitignore                      #
config.py                       #  

morning_bot.py                  # main funcion for running the program

				# requests to api.telegram.org with such 
								# methods as getFile, sendMessage,
								# sendAudio, getUpdates
```

![scheme](https://user-images.githubusercontent.com/8655093/164984131-7546e538-025e-4a4f-9b12-30f92941c79a.jpg)
