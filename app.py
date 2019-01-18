"""use this for main page info // response = requests.get("https://api.github.com/users/ChristinaDRoberts")
use this for repository page //response = requests.get("https://api.github.com/users/ChristinaDRoberts/repos")"""


import csv

from flask import Flask
from flask import request
from flask import render_template

import requests

#load all the packages
app = Flask(__name__)   #load all the packages ??? where does it look for packages

#this says if the search bar shows / , not clicking on tab, insert the info from this function
@app.route("/", methods=["GET", "POST"])
# defining function that will get my info for page from github
def index():
    # gets info from api and stores it in variable response
    response = requests.get("https://api.github.com/users/ChristinaDRoberts")
    # gets info and stores it in response 2
    response2 = requests.get("https://api.github.com/users/ChristinaDRoberts/repos")
    # uses buit in function to read json and convert it to python, stores that in data variable
    data = response.json()
    data2 = response2.json()

    # print(data)  # list of dict
    # print(data[1])

    # create a dictionary and assign it a key of repos and a value of the info from second api
    info_repo = {
        'repos': data2, 'general': data #also assign it another key of general and value of repos info
    }

    # sends the info back to program using render template function
    # in index file which we will be using for repos page, and replace the {% %} values with
    # key : value data that we call out of the api data se
    return render_template('index.html', **info_repo)




######## how to make tab sent tp followers , not to self in slack , put in html ############

#############################################################################


#if query string has followers included bc the tab was clicked it will GET (using get mehtod)info from api
# an api is literally a collection of data and these apis are listsof dictionaries

@app.route('/followers/', methods=["GET"])

def following_people():
    response = requests.get("https://api.github.com/users/ChristinaDRoberts/followers")
    data_followers = response.json()

    info_followers = {
        "followers" : data_followers}

    print(data_followers)

    return render_template('followers.html', **info_followers)



