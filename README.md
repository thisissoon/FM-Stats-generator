# FM-Stats-generator

FM-Stats-generator is a python celery application which generate weekly stats from
Soon FM api

## Environment

- `RABBITMQ_URI`: url to RabbitMQ (amqp://tbseen:tbseen@rabbitmq:5672/%2F)
- `AWS_S3_ACCESS_KEY': AWS S3 access key
- `AWS_S3_SECRET_KEY': AWS S3 access secret key
- `EXPORT_BUCKET_NAME': AWS S3 bucket


### Development:

Example of fugu file. Once you build it you can run CMS by `fug run api`. CMS and API
should be accessible on your localdocker on `/admin` and `/api`.

``` yaml
base: &base
  image: registry.soon.build/fm/stats
  rm: true
  interactive: true
  tty: true
  link:
    - rabbitmq:rabbit
  env:
    - DEBUG=True
    - AWS_S3_ACCESS_KEY=...
    - AWS_S3_SECRET_KEY=...
    - EXPORT_BUCKET_NAME=...
    - RABBITMQ_URI=...
  volume:
    - .../FM-Stats-generator/src:/src

test:
  <<: *base
  command: /bin/bash

bash:
  <<: *base
  command: /bin/bash

```

### Run it manually

```
celery -A app.tasks worker -B -l info
```
