FROM alpine:3.2

# Install OS Dependencies
RUN apk update && apk add \
    ca-certificates \
    python-dev \
    build-base \
    && rm -rf /var/cache/apk/*

# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py -O - | python

# Ensure a SOON user exists
RUN adduser SOON -D


WORKDIR /src
COPY ./src/ /src

EXPOSE 5000

RUN pip install -r requirements.txt

CMD celery -A app.tasks worker -B -l info
