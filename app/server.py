from fastapi import FastAPI
from api import router
from config.pika.mq_service import MQService
from config.logger.log_config import LogConfig
from logging.config import dictConfig


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def init_logger():
    dictConfig(LogConfig().dict())


async def init_queue():
    mq_service = await MQService()
    mq_service.message_handler.register_handler("a", mq_service.get_a_message)
    mq_service.message_handler.register_handler("b", mq_service.get_b_message)
    await mq_service.listen()


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="GIS Analytics Service",
        description="GIS Analytics Service",
        version="1.0.0",
    )
    init_routers(app_=app_)
    init_logger()
    init_queue()

    return app_


app = create_app()
