import os
from sqlalchemy import create_engine
from sqlalchemy import text

from models.job import JobModel


class JobRepos:

    def __init__(self, database_uri=None):
        self.database_uri = os.getenv('DATABASE_URI') or database_uri
        self.database_uri = self.database_uri or 'sqlite:///unijobstestdb.db'
        self.engine = create_engine(self.database_uri, connect_args={
            "check_same_thread": False}, future=True)

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, employer TEXT, location TEXT)"

        with self.engine.begin() as conn:
            conn.execute(text(sql))

    def add(self, job):
        sql = f"INSERT INTO jobs (title, description, employer, location) VALUES (:title, :description, :employer, :location)"

        with self.engine.begin() as conn:
            conn.execute(text(sql), [job.dict()])

        return job

    def get_jobs(self):
        sql = 'SELECT * FROM jobs'

        with self.engine.connect() as conn:
            result = conn.execute(text(sql))
            jobs = [JobModel(**row) for row in result.mappings()]

        return jobs

    def get_job_by_id(self, id):
        sql = f"SELECT * FROM jobs where id={id}"

        with self.engine.connect() as conn:
            result = conn.execute(text(sql))
            job = result.mappings().first()

        if job:
            return JobModel(**job)

        else:
            return None

    def delete_job_by_id(self, id):
        job = self.get_job_by_id(id=id)
        sql = f"DELETE FROM jobs WHERE id={id}"

        if not job:
            return {}

        with self.engine.begin() as conn:
            conn.execute(text(sql))

        return job
