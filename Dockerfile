FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

ENV FLASK_APP="/python-docker/app.py"

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]