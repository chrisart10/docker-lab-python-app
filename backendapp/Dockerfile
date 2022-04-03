# set base image (host OS)
FROM python:latest

#install update
RUN apt-get update

# add code to src
ADD . /src

# set the working directory in the container
WORKDIR /src

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]