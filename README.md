# CS 673 Project: Communication App

A web-based application to facilitate real-time communication between members of an organization.

## Built With

* Python 3.7.4
* Django 2.2.5
* Django Channels 2.3.0
* HTML/CSS, JavaScript
* Redis 2.8
* Amazon
    * Amazon Web Services (AWS) Elastic Beanstalk
    * Amazon Relational Database Service (RDS)
        * PostgreSQL 11.5

## Main Features

* Secure user registeration and login
* Update user profile (email, name, password, avatar)
* Join a workspace
* Within a workspace
    * Send and receive messages directly with another user, one-on-one
    * Send and receive messages in a group
* Communicate in real-time with little or no latency

## Design

### Front-End

The front-end is built with HTML/CSS, JavaScript, and Bootstrap.

### Back-End

#### Server

AWS Elastic Beanstalk is used to deploy and manage the web application in the AWS cloud.

#### Frameworks

Django 2.2.5 and Django Channels 2.3.0 are used as the back-end frameworks. Django Channels is a project that takes vanilla Django and extends its abilities beyond HTTP to handle WebSockets, chat protocols, IoT protocols, and more. Static webpages, such as user login, registration, will leverage vanilla Django while the chat pages, which require websockets and asynchronous communication, will leverage Djagno Channels.

#### Database

Amazon RDS is used to setup, host and operate the database. PostgreSQL 11.5 is included as a free database in Amazon RDS and is supported by Django, so this is the RDBMS used.

## Installation and Deployment

1. Download and install [Python 3.7.4](https://www.python.org/downloads/release/python-374/)
2. Upgrade [pip](https://pip.pypa.io/en/stable/installing/)

On Linux or macOS
```
$ pip3 install -U pip
```
On Windows
```
$ python3 -m pip install -U pip
```
3. Download and install [Docker](https://www.docker.com/get-started) from the official website
4. Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
```
$ pip3 install virtualenv
```
5. We will use a channel layer that uses Redis as its backing store. To start a Redis server on port 6379, run the following command
```
$ docker run -p 6379:6379 -d redis:2.8
```
6. Clone the cs673-project-team-2 repository locally
```
$ git clone https://github.com/bumetcs673f19/cs673-project-team-2.git
```
7. Create a Python virtual enviornment. Create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, is venv) can be anything; omitting the name "venv" will place the files in the current directory instead.
```
$ virtualenv venv
```
8. Activate the script
```
$ source venv/bin/activate
```
9. cd into the cs673-project-team-2 repository
```
(venv) $ cd /path/to/cs673-project-team-2
```
10. Install the requirements
```
(venv) $ pip3 install -r requirements.txt
```
11. cd into /communication_app
```
(venv) $ cd communication_app/
```
12. Copy env_var.py into this folder. This file contains the information to connect to the database. It is not published on GitHub for security reasons.
13. Start a lightweight development Web server locally.
```
(venv) $ python3 manage.py runserver
```
14. Go to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
15. You should be all set!

## Team

* Jhuanderson Macias
* Laura Kocubinski
* Hang Shi
* Xi You
* Bofeng Liu
* Mikhail Chertushkin

## Tools

* Communication
    * Slack - Chat
        * https://join.slack.com/t/bumetcs673f19/shared_invite/enQtNzM4OTc1MTQwNDUwLThiNmI2NmJlMDUyOTkxOTc0Njk4MzJiYWZiYTQwYjUxOTdiZWRmZTg1ODg1NjVkNzAyZjYxYzQyNTY0NGZmYTY
    * Zoom - Remote Meeting
            * Blackboard > MET CS673 Software Engineering > Live Classroom

* Requirement Management
    * Pivotal Tracker
        * https://www.pivotaltracker.com/n/projects/2397582

* Document Sharing
    * Google Drive
        * https://drive.google.com/drive/u/1/folders/1KnrpGFOuKGM2V2Pk0DaVOGoXRf7QMGpA

## Acknowledgments

* Boston University MET Master of Science Computer Science Program
* MET CS 673 Software Engineering

