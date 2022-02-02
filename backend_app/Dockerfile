# pull official base image
FROM python:3.9.6
# set work directory
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
COPY entrypoint.sh .
RUN pip install -r requirements.txt
# run entrypoint.sh
RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["sh", "/app/entrypoint.sh"]