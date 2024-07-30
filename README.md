# Snake-Tournament

### Welcome Apolo to the Snake-Tournament!

## Introduction
Welcome to the Snake-Tournament, a battle between bots that will be ranked and scored based on the ELO rating system, revealing the best programmer around us! 

## How the Game Works
- Each participating player will create a bot, which will be put aginst another bot to try to get as many points, and win the game! The program will be limited to 512 tokens, making the game even more challenging.
- Every bot will play randomaly against other bot, and will get an ELO rating on how good it performed.



## How to participate
To participate in the Snake-Tournament, follow these steps:
1. Clone the repository
2. Change the get_direction function in the exampleBot.py file, to include whatever logic you see fit
3. Send me the file when the time for developing ends (Give it a cool name to differentiate yourself from other competitors)
4. I will run all the bots against each other using the ELO rating system, and will annouce the winner at the end!

## Rules
### The general rule is just participate normally, most of these rules are just to stop you from being a dick
- As part of the challenge, your function(s) will have to stay under 512 tokens! (To check how many tokens your code is, use the Token_Counter.py file which is provided). A Python token is a basic unit of code that represents a specific element, such as a keyword, identifier, operator, or literal value (e.g. `if`, `else`, `int`, etc..).
- You can only change/add functions to the Bot class in the Bot.py file, any modifications to the rest of the code won't take into affect.
- You must not include any libraries that will do the heavy lifting for you. You can only include libraries like math, random, etc..
- Your code should be self contained, meaning it cannot go to the internet for help, or use any other files other then Bot.py. 
- You must implement the get_direction function in Bot.py, and you must return one of the values: "UP", "DOWN", "LEFT", "RIGHT".
- You must not change any values in the Snake/Board/Game/GUI classes


