FROM python:3.11
#!/bin/bash
# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
RUN mkdir /app
ADD . /app
WORKDIR  /app

#to COPY the remote file at working directory in container
RUN pip install --user -r requirements.txt
COPY scripts/main.py ./
COPY  scripts/settings.py ./
CMD [ "python","-u", "./main.py"]
