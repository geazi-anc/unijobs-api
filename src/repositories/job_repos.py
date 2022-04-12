from models.job import JobModel


class JobRepos:

    def __init__(self):
        self.db = []

    def add(self, job):
        id = len(self.db)+1
        job = JobModel(id=id, **job.dict())

        self.db.append(job)
        return job

    def get_jobs(self):
        return self.db

    def get_job_by_id(self, id):
        job = [job for job in self.db if job.id == id]

        return job.pop() if job else {}

    def delete_job_by_id(self, id):
        job = self.get_job_by_id(id=id)

        try:
            self.db.remove(job)

        except ValueError as exc:
            return {}

        else:
            return job
