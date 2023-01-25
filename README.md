# ConsumerExample-service
This project was created with Python and FastAPI framework.

- Please check out FastAPI documentation: https://fastapi.tiangolo.com/

## Environment

Please set up your Python version to `3.10`

- `
python3 --version
`

Create your `.env` file.

- `cd <project-directory>`
- 
```bash
    $ touch .env
```

```bash
APP_NAME=Example
APP_VERSION=1.0.1
ENV=local
APP_PORT=3002
APP_HOST=localhost
BODY_LIMIT=12000
LOG_LEVEL=info
SWAGGER_ENABLED=true
DEBUG=true
MICROSERVICE_CLIENT_TIMEOUT=60
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
RABBITMQ_EXCHANGE_NAME=message_exchange
RABBITMQ_EXCHANGE_TYPE=fanout
RABBITMQ_QUEUE=message_queue
RABBITMQ_ROUTING_KEY=0
RABBITMQ_CONNECTION_ATTEMPTS=0
RABBITMQ_RETRY_DELAY=0
```

## Setting Development Environment

- Install virtual environment
```bash
    $ pip install virtualenv
```

- Created virtual environment
```bash
    $ virtualenv env
```

- Activate the virtual environment
```bash
    $ source env/bin/activate
```

- Install libraries
```bash
    $ pip install -r requirements.txt
```

## Run Service

```bash
    $ python3 main.py
```

## Swagger Documents

* Open browser and direct to http://127.0.0.1:3000/docs or http://127.0.0.1:3000/redoc 

# Producer Exec

- Setup RabbitMQ

```bash
    $ brew update
    $ brew install rabbitmq
    $ brew info rabbitmq
```

- Configration RabbitMQ

CONF_ENV_FILE="/opt/homebrew/etc/rabbitmq/rabbitmq-env.conf" /opt/homebrew/opt/rabbitmq/sbin/rabbitmq-server

- RabbitMQ service start & stop

```bash
    $ brew services start rabbitmq
```
&&
```bash
    $ brew services stop rabbitmq
```
### Run Producer

**Don't forget to enable virtual environment**

```bash
    $ cd producer
```

```bash
    $ python3 app.py
```