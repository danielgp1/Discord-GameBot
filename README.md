
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
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The project represents an implementation of a discord game bot. <br>
You can play Tic-Tac-Toe, Rock-Paper-Scissors, Hangman and Akinator. <br>
More games to be added soon or later.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<ul>
<li>Download or clone the repository</li>

```
$ git clone https://github.com/danielgp1/Discord-GameBot.git
```
    
<li>Install the necessary plugins using</li>

```
$ pip install -r requirements.txt
```

<li>Create a Discord Bot in the Discord Developer Portal</li>

```
https://discord.com/developers/applications
```
    
<li>Give the bot Administrator Rights and invite it to your server</li>
    
<li>Replace the TOKEN and CHANNEL_ID values in the config.py file</li>

```
PREFIX = "!"
TOKEN = 'YOURK DISCORD BOT TOKEN'
CHANNEL_ID = YOUR TEXT CHANNEL ID
```

<li>To start the bot, run the following file from the project</li>

```
main.py
```

</ul>


## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

In order to be able to play games with the bot, you have to be assigned the <code>Games</code> role. <br>
You can be granted the role by clicking on the 🎮 emoji on the message in the <code>welcome-channel</code>

![](https://i.imgur.com/Zp4xYpc.png)

By writing <code>!games</code> in a discord channel, you can check the list of the available games.<br>
Click to a desired number reaction to play the corresponding game

![](https://i.imgur.com/PiEj67Q.png)

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) 
- [Visual Studio Code](https://code.visualstudio.com/) 


## ✍️ Authors <a name = "authors"></a>

- [@danielgp1](https://github.com/danielgp1)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Stack Overflow

