# Documentation for setting the TV up 

## Stack 
THe frontend page uses `reveal.js` to make a dynamic presentation. Content is delivered from the web server (Flask). 

The project is split into two categories: the tv "application" and the web server - powered by Flask. 
The application is just a python program that opens a fullscreen webview and routes to localhost (web servers address)

## Setting the web server up 
First, you must install all python packages by running `pip -r install requiremets.txt` under `/webserver` directory. After installing, just run `python app-py` 
and the web server will be up and running.
