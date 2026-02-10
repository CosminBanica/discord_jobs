from src.register_jobs import JOBS

if __name__ == "__main__":
    for job in JOBS:
        job.run()
