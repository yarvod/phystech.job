# pull official base image
FROM python:3.9.6
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
COPY entrypoint.sh .
RUN pip install -r requirements.txt
# copy project
COPY backend_app .

# run entrypoint.sh
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]