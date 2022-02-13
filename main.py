import uvicorn
from api.app import init_app

web_app = init_app

def start_web_server() -> None:
    uvicorn.run(
        "main:web_app",

    )

if __name__ == '__main__':
    start_web_server()