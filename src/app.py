from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import job


app = FastAPI(title='UniJobs API')
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
# include API routes from routers module
app.include_router(job.router)
