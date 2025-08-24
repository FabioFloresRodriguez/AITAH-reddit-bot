# AITAH Reddit bot

## It's a Reddit bot that pulls the stories of the top ten posts from the AITAH subreddit's "hot" section.

This project originally started out as a anniversary gift for my girlfriend. She loves the "Am I the Asshole?" stories on Tik Tok, but she always watches all of the posts before new ones release and doesn't like to use Reddit. The bot is made to automatically get the top ten posts of the hot section from the AITAH subreddit, goes through each post author's profile to look for extra parts of the story, and adds the full story in a word document that the user can access. 

# Prerequisites

Made with Python

The following packages are used in the project:
* Praw
* re
* docx
* pathlib
* datetime

Also, make another directory inside the directory named "Weekly AITAH stories". That's where all the word documents will go.

## Cloning the repository
To obtain everythin in the repository, open a terminal and input 

```bash
git clone https://github.com/FabioFloresRodriguez/AITAH-reddit-bot.git
```

## Installing packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install docx and praw.
```bash
pip install python-docx
pip install praw
```

## Creating a Reddit application
To create a Reddit application, click on the link:

https://new.pythonforengineers.com/blog/build-a-reddit-bot-part-1/

and follow the steps on the Create Reddit App section. It's a good tutorial on how to set it up. I also recommend reading the API rules linked higher up in the article so you don't accidentally break one. 

Some things that are mentioned in the article but I want to reiterate.
1. Make a copy of praw.ini in your directory, and add the bot1 section inside the copy.
2. Be careful with how many requests you're making per minute. 
3. Make a unique user-agent, I recommend following the format given in here

https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki

# Usage
Once everything is installed and set up, you can just run it manually in whatever code editor you use. 

If you wish to automate it, the link where it led you to create a Reddit App is actually a series that includes a tutorial on how to create a linux virtual environment and how you can automate it inside the VM. However, there are two caveats with the tutorial, 
1. The tutorial is old and uses precise32, which is outdated. What I do is substitute precise32 for "hashicorp/bionic64". 
2. It uses python 2.7 as the default, so you have to install python3 and pip3 and set those as the default of the virtual environment.

Either way, the output of the code will look like this 

https://1drv.ms/w/c/E9B1CB7392497D84/ESWxWoNjSFNHvwmIhn26214BuF5U75So0nLxxPZJ11n6lg?e=Er5tl0

# Acknowledgments
Thank you to Shatnu Tiwari from the pythonforengineers link for the tutorial on how to make a simple Reddit Bot. And to my girlfriend for needing more AITAH stories.
