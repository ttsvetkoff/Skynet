FROM ubuntu:latest

ADD main.py .

RUN pip install Pillow
RUN pip install tk
RUN apt-get install xeyes
RUN apt-get update
RUN apt-get install -y x11-apps

WORKDIR /Users/tsvetomir.tsvetkov/Skynet

CMD [ "python", "./main.py" ]