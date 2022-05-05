from repositories.job_repos import JobRepos


def test_create_a_new_job(database_mock, job):

    # arrange
    job_repos = JobRepos()

    # action
    job_repos.create_table()
    job_repos.add(job)
    saved_job = job_repos.get_job_by_id(id=1)

    # assert
    assert saved_job.id == 1


def test_get_jobs(database_mock, job):

    # arrange
    job_repos = JobRepos()
    job_repos.create_table()
    job_repos.add(job)

    # action
    jobs = job_repos.get_jobs()

    # assert
    assert len(jobs) == 1

def test_get_job_by_id(database_mock, job):

    # arrange
    job_repos = JobRepos()
    job_repos.create_table()
    job_repos.add(job)

    # action
    saved_job = job_repos.get_job_by_id(id=1)

    # assert
    assert saved_job.id == 1


def test_delete_job_by_id(database_mock, job):

    # arrange
    job_repos = JobRepos()
    job_repos.create_table()
    job_repos.add(job)

    # action
    job_repos.delete_job_by_id(id=1)
    job = job_repos.get_job_by_id(id=1)

    # assert
    assert job == None
