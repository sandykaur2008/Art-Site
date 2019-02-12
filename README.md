# Project Title
This project is called "Art Site" and it's a simple social media site where artists can post pieces and comment on the pieces of others. It was built using Django (backend), GraphicsMagick and Grunt (for image re-sizing), Bootstrap, and Sass. It is deployed with Heroku at https://sandys-artsite.herokuapp.com/.

# Getting Started
To contribute:
- Navigate to this repo: sandykaur2008/Art-Site
- Follow these instructions: https://help.github.com/articles/fork-a-repo/

To simply view: 
- Navigate to this repo: sandykaur2008/Art-Site
- Follow these instructions: https://help.github.com/articles/cloning-a-repository/

# Prerequisites
Aside from a working browser and Python 3, you will also need:

- the dependencies in requirements.txt 

## To install dependencies in requirements.txt
Make sure you're in root directory of repo and execute:

```pip install -r requirements.txt```

## To actually run website once repo cloned, css compiled, and dependencies installed
- Navigate to root directory
- Execute: 

```gunicorn ArtSite.wsgi```

- Navigate to link provided 

# Built With
- Visual Studio Code 1.24.1
- Ruby Sass 3.5.6 
- Django 2.0.6 (also see requirements.txt)
- Grunt 0.4.5

# Authors
Satinder Kaur 

# License
All images are mine. 

# Acknowledgments
Thanks, @github/markalexandercastillo, for reviewing and giving me tips! 
:relaxed: 
Also, found https://simpleisbetterthancomplex.com/ very helpful! 

# To Do
Need to fix tests and also Amazon S3 storage settings. Also, would like to work more on styling. 
