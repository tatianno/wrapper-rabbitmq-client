#  RabbitMQProducer

## Overview

It is a message producer for a RabbitMQ Server.


## Installing AMI2RabbitMQ and Supported Versions

RabbitMQProducer is available on PyPI:

`$ python -m pip install wrapper-rabbitmq-client`

RabbitMQProducer officially supports Python 3.8+.

## Cloning the repository

`$ git clone https://github.com/tatianno/wrapper-rabbitmq-client.git`

## Example


```
from wrapper_rabbitmq_client import RabbitMQProducer


RABBITMQ_SETTINGS = RABBITMQ_SETTINGS = {
    'host' : 'localhost',
    'user' : 'user',
    'password' : 'password',
    'queuename' : 'online'
}

producer = RabbitMQProducer(
    RABBITMQ_SETTINGS
)

producer.send(
    {
        'test' : 1234
    }
)
```