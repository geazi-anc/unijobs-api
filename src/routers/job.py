import os

from fastapi import APIRouter, HTTPException, Depends, status, Header


from models.job import Job, JobModel

from repositories.job_repos import JobRepos


# ingections
router = APIRouter(
    tags=['jobs'],
    responses={404: {'description': 'Job not found'},
               201: {'description': 'Job successfully created'}}
)

job_repos=JobRepos()
job_repos.create_table()
API_KEY = os.getenv('API_KEY') or 'myapikey'


##### DEPENDENCIES #####
def is_authorized(x_apikey: str = Header(...)):

    if x_apikey != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='You do not have permission to delete a job. Please add a valid API Key in x-apikey header.')

    return x_apikey


##### ROUTES #####
@router.post('/jobs', status_code=201, response_model=Job)
def post_a_new_job(job: Job):
    job = job_repos.add(job)
    return job


@router.get('/jobs', response_model=list[JobModel])
def get_jobs():
    jobs = job_repos.get_jobs()
    return jobs


@router.get('/jobs/{id}', response_model=JobModel)
def get_job_by_id(id: int):
    job = job_repos.get_job_by_id(id=id)

    if not job:
        raise HTTPException(status_code=404, detail='Job not found.')

    return job


@router.delete('/jobs/{id}', dependencies=[Depends(is_authorized)], response_model=JobModel)
def delete_job_by_id(id: int):
    job = job_repos.delete_job_by_id(id=id)

    if not job:
        raise HTTPException(status_code=404, detail='Job not found.')

    return job
