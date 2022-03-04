FROM python:3.9

WORKDIR /usr/local/app
COPY . .
RUN apt-get -y update
RUN apt-get -y install xauth
RUN python -m pip install -r requirements.txt

EXPOSE 8887
CMD ["python", "main.py"]
