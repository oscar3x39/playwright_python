FROM ubuntu:20.04

## install python3.8
RUN apt-get update -y
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

## install playwright
RUN pip install playwright
RUN pip install pytest-playwright
RUN pip install pytest
RUN pip install pytest-html
RUN pip install python-slugify

# install playwright chromium depends
RUN playwright install
RUN playwright install-deps

WORKDIR /code