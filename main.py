import sys
import argparse
from src.register_jobs import JOBS


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Discord jobs by interval.")
    parser.add_argument('--interval', choices=['hourly', 'daily'], required=False, help='Which interval jobs to run')
    args = parser.parse_args()

    interval = args.interval
    for job in JOBS:
        job_interval = job.interval
        if interval is None or job_interval == interval:
            job.run()
