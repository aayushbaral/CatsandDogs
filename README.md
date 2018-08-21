### Project Description

Building a RESTful API using Flask to predict if a certain image is a cat or a dog.

### Framework and Libraries used:

- keras with tensorflow backend
- Flask
- opencv
- Docker

### Getting Started Guide

Run Docker on your local machine

Go to the root of project directory using command line
Build the docker image for the api using

`docker-compose build`

After the build is successful, run the docker conainer using

`docker-compose run`

Fire up another commandline shell
Go to the root of the project directory and connect to the port 5000 where Flask app is running and post the image using
`curl -X POST -F file=@filename 'http://0.0.0.0:5000/'`

filename needs to be substituted by the image test files which are in the testimages folder inside the project folder. 


The returned result would be a JSON onject telling us whether the image is of a cat or a dog.

If you have any further questions, email me at aayushbaral@bennington.edu













