# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r server/requirements.txt
RUN pip install -r bot/requirements.txt
#RUN pip install -r song-helpe/rrequirements.txt

CMD ["/bin/bash", "-c", "python server/manage.py migrate && python server/manage.py runserver 0.0.0.0:8000"]
