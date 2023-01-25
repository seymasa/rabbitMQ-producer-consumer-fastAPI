import uvicorn
from config.config import config
import os

import asyncio
import threading
import uvicorn
from config.config import config
import os
from app.server import init_queue


if __name__ == "__main__":
    os.environ["ENV"] = config.ENV  # uygulama çalıştırılırken parametre olarak girilmesi sağlanıp,
    os.environ["DEBUG"] = str(True if config.ENV != "production" else False)
    t1 = threading.Thread(target=uvicorn.run, args=("app.server:app",), kwargs={"host": config.APP_HOST,
                                                                                "port": config.APP_PORT,
                                                                                "timeout_keep_alive":
                                                                                    config.MICROSERVICE_CLIENT_TIMEOUT})

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    t2 = threading.Thread(target=loop.run_until_complete, args=(init_queue(),))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
