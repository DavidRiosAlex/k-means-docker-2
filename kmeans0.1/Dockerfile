FROM python:3.7.3

ENV PYTHONUNBUFFERED 1



RUN pip install numpy
RUN pip install matplotlib
RUN pip install pandas
RUN pip install sklearn
RUN pip install jupyter

RUN mkdir src
WORKDIR /src
COPY ./src /src

RUN adduser -disabled-login user
USER user
