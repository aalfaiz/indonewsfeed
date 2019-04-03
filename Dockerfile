# Scrapy run on python. choose official python docker image
FROM python:3.6

# set working directory to /usr/scr/app
WORKDIR /usr/scr/app

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python3", "./run.py"]