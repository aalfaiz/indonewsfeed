# Scrapy run on python. choose official python docker image
FROM python:3.6-slim

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/indonewsfeed-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/indonewsfeed-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

#Install Cron
RUN apt-get update
RUN apt-get -y install cron


# SET arguments
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

# SET environment
ENV AWS_ACCESS_KEY_ID = ${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY = ${AWS_SECRET_ACCESS_KEY}
ENV AWS_DEFAULT_REGION =${AWS_DEFAULT_REGION}

# set working directory to /usr/scr/app
WORKDIR /usr/scr/app

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install awscli && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential gcc

COPY . .

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

#CMD [ "python3", "./run.py"] 