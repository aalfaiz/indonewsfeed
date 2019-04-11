# Scrapy run on python. choose official python docker image
FROM python:3.6-slim

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
    && apt-get install -y --no-install-recommends build-essential gcc cron \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install awscli && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential gcc

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Apply cron job
RUN crontab /etc/cron.d/hello-cron

COPY . .

#ENTRYPOINT [ "python3", "./run.py"] 

# Run the command on container startup
CMD ["crond", "-f"]