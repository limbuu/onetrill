FROM ubuntu:16.10
RUN apt-get update && apt-get install python3.6
ADD . .
RUN python main.py
