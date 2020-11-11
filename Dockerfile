FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libpq-dev python3-dev python3-pip build-essential

WORKDIR  /strangerchatbot
COPY ./strangerchatbot /strangerchatbot

RUN pip3 install -r requirements.txt

CMD ["./wait-for-it.sh", "postgres:5432", "--", "python3", "app.py"]
