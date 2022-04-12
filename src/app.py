from fastapi import FastAPI

from routers import job


app = FastAPI(title='UniJobs API')

# include API routes from routers module
app.include_router(job.router)
