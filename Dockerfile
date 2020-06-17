FROM ubuntu:18.04
RUN apt-get update 
RUN apt-get install python3 -y
RUN apt-get install software-properties-common -y && apt-add-repository universe -y
RUN apt-get update
RUN apt-get install python3-pip -y
ADD ./test.py .
#RUN pip3 install -r requirements.txt
RUN pip3 install flask
CMD ["python3","test.py"]
