# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

COPY . /opt

RUN pip install -r /opt/requirements.txt

WORKDIR /opt/server
CMD ["/bin/bash", "-c", "python manage.py migrate && python manage.py runserver"]
