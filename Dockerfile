# Install the base requirements for the app.
# This stage is to support development.
FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
CMD cat LICENSE
