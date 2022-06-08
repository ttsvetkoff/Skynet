FROM python:latest

ADD main.py .

RUN pip install Pillow
RUN pip install tk

WORKDIR /Users/tsvetomir.tsvetkov/Skynet

CMD [ "python", "./main.py" ]