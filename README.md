By Muhammad Ilham Adhim


This repository is my exercise which is derived from Corey Schafer youtube tutorial

Python Flask Tutorial: Full-Featured Web App
link : https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

In this directory. the important one is run.py and flaskblog



17 March 2019 
    -) Getting started on Flask 
    -) Make some basic routes : login , home , register , about


18 March 2019 
    -) Editing HTML with jinja   -> allows developer to make conditions, loops , etc inside the html file
                                 -> extends html layout from each other
    -) Login and Registration form created. Third day flask web activities
    -) Delivering flash messages to the user if they are finished signing up or signing in by using bootstrap extension for flask


21 March 2019
    -) Setting Secret Key for the blog, by generating python random hex number
    -) Getting started to SQLAlchemy and connecting SQLite to app
    -)Added author and reference inside the SQLite database using SQLAlchemy ORM
    -) Setting rules for each column in SQLite table 


23 March 2019 
    -) Increase Security on user passwords, using hash approach by flask-bcrypt
    -) Make user validation. when the user is already logged in, no need to show login and register in web page
    -) Redirect users to login page if they haven't logged in yet access the profile page
    -) Restructuring modules in the project. allows for better layout and effectiveness of codes
    
7 April 2019
    -) Added features that handle updating profile picture , username , and email of logged in user with certain conditions
    -) Importing OS and Pillow libraries to handle pictures , storages , and directories
            -> OS is used to add uploaded photo to profile_pics folder.
            -> Pillow is used to resize image to smaller pixels, so that the web loads faster and less storage used
