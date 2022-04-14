
# Lab - Dockerizing a python app

Docker lab to deploy multiples python app. 




## Authors

- [@chrisart10](https://www.github.com/chrisart10)


## Tech specs

**Language:** Python

**Library:** FastAPI, Streamlit 

**Server:** Play with docker (PWD)

**Tools:** Docker, Git

## Installation

*Installation commands:*
 
Clone the project

```bash
$ git clone git://github.com/chrisart10/docker-lab-python-app
```

Go to the project directory

```bash
$ cd docker-lab-python-app
```

Run with docker to start services
```bash
$ docker-compose up --build -d
```

verify containers
```bash
$ docker ps -a
```

Kill containers to stop services
```bash
$ docker-compose down
```


## Feedback

If you have any feedback, please reach out to me at @chris_art10 on twitter. 

## 🔗 Links
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/chris_art10)


## Lessons Learned

I've learned to deploy app using docker compose, make dockerfile to build images, and understand networking to communicate contianers each other.

