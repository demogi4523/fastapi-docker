from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'key' : 'value'}


if __name__ == '__main__':
    import asyncio
    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    port = 8001
    bind = [f"0.0.0.0:{port}"]
    config = Config()
    config.bind = bind
    asyncio.run(serve(app, config))