from fastapi import FastAPI, Header

from routers import job

app = FastAPI(title='UniJobs API')

app.include_router(job.router)


@app.get("/ping")
def ping():
    return "PONG!"
