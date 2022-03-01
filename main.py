import uvicorn
from api.app import init_app
from config.environoment import get_settings

_SETTINGS = get_settings()

web_app = init_app(_SETTINGS)

def start_web_server() -> None:
    settings = get_settings()
    uvicorn.run(
        "main:web_app",
        host=settings.WEB_SERVER_HOST,
        port=settings.WEB_SERVER_PORT,
        reload=settings.WEB_SERVER_RELOAD,

    )

if __name__ == '__main__':
    start_web_server()