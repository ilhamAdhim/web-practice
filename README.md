This repository is my exercise which is derived from Corey Schafer youtube tutorial

Python Flask Tutorial: <br>Full-Featured Web App
link : https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

In this directory. the important one is run.py and flaskblog <br><br>
17 March 2019 <br>
    - Getting started on Flask <br>
    - Make some basic routes : login , home , register , about<br><br>


18 March 2019 <br>
    - Editing HTML with jinja  <br> 
      - allows developer to make conditions, loops , etc inside the html file <br>
      - extends html layout from each other <br>
    - Login and Registration form created. Third day flask web activities <br>
    - Delivering flash messages to the user if they are finished signing up or signing in by using bootstrap extension for flask
    <br><br>

21 March 2019 <br>
    - Setting Secret Key for the blog, by generating python random hex number <br>
    - Getting started to SQLAlchemy and connecting SQLite to app<br>
    - Added author and reference inside the SQLite database using SQLAlchemy ORM<br>
    - Setting rules for each column in SQLite table <br><br>


23 March 2019 <br>
    - Increase Security on user passwords, using hash approach by flask-bcrypt<br>
    - Make user validation. when the user is already logged in, no need to show login and register in web page<br>
    - Redirect users to login page if they haven't logged in yet access the profile page<br>
    - Restructuring modules in the project. allows for better layout and effectiveness of codes<br><br>
    
7 April 2019<br>
    - Added features that handle updating profile picture , username , and email of logged in user with certain conditions<br>
    - Importing OS and Pillow libraries to handle pictures , storages , and directories<br>
      - OS is used to add uploaded photo to profile_pics folder<br>
      - Pillow is used to resize image to smaller pixels, so that the web loads faster and less storage used<br><br>
