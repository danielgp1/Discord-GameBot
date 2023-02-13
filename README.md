![](https://graphicsfamily.com/wp-content/uploads/edd/2021/09/Gaming-Logo-Design-Template-1180x664.jpg)

<h3 align="center">Discord GameBot</h3>

---

<p align="center">
    My project for the FMI Python Course 2023
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Games](#games)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The project represents an implementation of a discord game bot. <br>
You can play Tic-Tac-Toe, Rock-Paper-Scissors, Hangman and Akinator. <br>
More games to be added soon or later.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

-  Download or clone the repository

```
$ git clone https://github.com/danielgp1/Discord-GameBot.git
```
    
-  Install the necessary plugins using

```
$ pip install -r requirements.txt
```

-  Create a Discord Bot in the Discord Developer Portal

```
https://discord.com/developers/applications
```
    
-  Give the bot Administrator Rights and invite it to your server
    
-  Replace the TOKEN and CHANNEL_ID values in the config.py file

```
PREFIX = "!"
TOKEN = 'YOUR DISCORD BOT TOKEN'
CHANNEL_ID = YOUR TEXT CHANNEL ID
```

-  To start the bot, run the following file from the project

```
main.py
```

## 🎈 Usage <a name="usage"></a>

In order to be able to play games with the bot, you have to be assigned the <code>Games</code> role. <br>
First, add the roles Blue,Red and Games to your server. Write <code>!teams</code> in a text channel and copy the ID of the message <br>
Replace the  <code>ourMessageID = ID</code> with the ID of your message in the functions <code>on_raw_reaction_add</code> and <code>on_raw_reaction_remove</code> in <code>main.py </code> <br>
You can be granted the role by clicking on the 🎮 emoji on the message

![](https://i.imgur.com/Zp4xYpc.png)

By writing <code>!games</code> in a discord channel, you can check the list of the available games.<br>
Click on a desired number reaction to play the corresponding game

![](https://i.imgur.com/PiEj67Q.png)

## 🎮 Games <a name = "games"></a>

-  Tic-Tac-Toe <br>
    
![](https://i.imgur.com/2ZrZYgT.png)

-  Rock-Paper-Scissors <br>
    
![](https://i.imgur.com/6Ok6pq2.png)

-  Hangman <br>
    
![](https://i.imgur.com/gQnC2YF.png)

-  Akinator <br>
    
![](https://i.imgur.com/PalgoMM.png)
    

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) 
- [Visual Studio Code](https://code.visualstudio.com/) 


## ✍️ Authors <a name = "authors"></a>

- [@danielgp1](https://github.com/danielgp1)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- [Stack Overflow](https://stackoverflow.com/)
