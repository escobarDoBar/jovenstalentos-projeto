import uvicorn

from api import api

if __name__ == "__main__":
    config = uvicorn.Config("server:api", host='127.0.0.1', port=1337, log_level="debug", reload=True)
    server = uvicorn.Server(config)
    server.run()