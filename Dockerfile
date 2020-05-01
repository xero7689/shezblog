FROM python:3.7
ENV PYTHONUNBUFFERED 1
# Creating working directory
RUN mkdir /shezblog
WORKDIR /shezblog
# Copying requirements
COPY ./requirements.txt /shezblog/
RUN pip install -r requirements.txt
COPY . /shezblog/

EXPOSE 8000

