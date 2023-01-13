import uvicorn
from config.config import config
import os


def main():
    os.environ["ENV"] = config.ENV
    os.environ["DEBUG"] = str(True if config.ENV != "production" else False)
    uvicorn.run(
        app="app.server:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True,
    )


if __name__ == "__main__":
    main()
