import os
from decouple import config
from pydantic import BaseSettings


class Config(BaseSettings):
    APP_NAME: str = config('APP_NAME')
    APP_VERSION: str = config('APP_VERSION')
    ENV: str = config('ENV')
    BODY_LIMIT: int = config('BODY_LIMIT')
    DEBUG: bool = True
    APP_HOST: str = config('APP_HOST')
    APP_PORT: int = config('APP_PORT')
    LOG_LEVEL: str = config('LOG_LEVEL')
    SWAGGER_ENABLED: str = config('SWAGGER_ENABLED')
    RABBITMQ_HOST: str = config('RABBITMQ_HOST')
    RABBITMQ_PORT = config('RABBITMQ_PORT')
    RABBITMQ_USERNAME = config('RABBITMQ_USERNAME')
    RABBITMQ_PASSWORD = config('RABBITMQ_PASSWORD')
    RABBITMQ_EXCHANGE_NAME = config('RABBITMQ_EXCHANGE_NAME')
    RABBITMQ_EXCHANGE_TYPE = config('RABBITMQ_EXCHANGE_TYPE')
    RABBITMQ_QUEUE = config('RABBITMQ_QUEUE')
    RABBITMQ_ROUTING_KEY = config('RABBITMQ_ROUTING_KEY')
    RABBITMQ_CONNECTION_ATTEMPTS: int = config('RABBITMQ_CONNECTION_ATTEMPTS')
    RABBITMQ_RETRY_DELAY: int = config('RABBITMQ_RETRY_DELAY')
    MICROSERVICE_CLIENT_TIMEOUT: int = config('MICROSERVICE_CLIENT_TIMEOUT')



class DevelopmentConfig(Config):
    ENV: str = "dev"


class LocalConfig(Config):
    ENV: str = "local"


class ProductionConfig(Config):
    ENV: str = "prod"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
