# set base image (host OS)
FROM python:3.8-slim

#install update
RUN apt-get update

# add code to src
ADD src /src
ADD requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# set the working directory in the container
WORKDIR /src

# command to run on container start
CMD ["streamlit","run","main.py","--server.port","80"]
