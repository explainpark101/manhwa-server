import uvicorn
from main import app
DEBUG = True

if __name__=="__main__":
    if DEBUG:
        uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    else:
        uvicorn.run(app, host="0.0.0.0", port=8080)
