## Why I'm learning `pygame`

I'm interested in learning `pygame` to explore how I can use data science to answer this question:

> How does the probability of individual game events affect game outcomes of interest?

I figure, in order to do this, I need a feeling for how game data is generated, the logic of the code that produces it. I actually see a lot of video game data at work, but we have a lot of exploratory and dev ops work before I will have time to work on models. This is a hobby project. 

I'm more interested in data science than in becoming a game developer (I _love_ my job), so a core component of my game is that it is simple in the ways that are not crucial to data analysis. For this reason, it's a satirical text-based anti-venture into `data theatre`.   

## Some data science bits

Keeping things simple, suppose the player only ever has two choices, and that these two choices carry weights specific to the game event. There must also be win and loss conditions. 

### Data science questions to explore

- What are the optimal probability mass functions for each game event that provide the given desired game outcome?
- What are the optimal game outcomes for the given probability mass functions of the game events?

## Design document

These notes suggest writing a [design document](https://web.eecs.utk.edu/~huangj/netgames/notes/designdoc.html) as a first step. 

### Overview

The goal of the game is for Y-Corp to go IPO and all employees become millionaires overnight. As a data scientist, the player must help the company achieve their goal SAS goal of implementing new features, and removing bugs.  

### Story of the game

The player begins as a data scientist at Y-Corp, an unspecified SAS company. Although their job title and department change, their job, pressing buttons, remains the same. The player presses buttons to validate data, produce reports, and fix bugs.  

### Targeted audience

Me and my friends.

### Expected results

Current goal is to produce a game that 
- prompts the player to start
- welcomes the player and invites them to progress to onboarding
- provides a quietly rage quit button 
- onboards the player by prompting them to press a button
- provides the player with at least 2 prompts and outputs, with probabilistic outcomes, and text rendered for the outcome dependent on the outcome's random sampling. 
- tracks how many bugs and other win/loss conditions in a dataframe and stores that dataframe in game-data/ output
- end of game report for player 

### Evaluation

Use data science to check evaluate the effect of game event probabilities on win/loss outcomes. 

### Initial list of tasks

- [ ] resonably sensible structure to game logic: extensible and ease of refactoring
- [ ] get the scenarios (welcome, prompts and outcomes) to run
- [ ] output text in a pretty-enough way


## File structure

- game.py is the game script
- game_fns.py contains game functions
- things-to-fiddle-with/ contains small .csvs and text files that are have ease of input
- game-data/ contains computationally-generated data that should not be modified 
- game-text-png/ contains hack image pipeline output for text rendering  
- make_game_text.R is the hack image pipeline script 
- blackboard.py is a scratchpad
- data-theatre.iynb is first thoughts on data analysis
- text_wrap.py is where the text wrapping functions are being developed
- ui_fns.py is currently there for a user interface, but may be restructured out