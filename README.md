# Discord Jobs Runner

This repository provides a simple framework for running automated jobs that update your Discord server with information from external sources.

## Project Structure

``` python
main.py                  # Entry point for running all jobs
src/
    register_jobs.py       # Registers and configures all jobs
    jobs/
        job_base.py          # Abstract base class for jobs
        player_count.py      # Example job: posts Steam player count to Discord
README.md                # This file
```

### How It Works

1. Jobs are defined as classes inheriting from `Job` (see `src/jobs/job_base.py`).
2. Each job implements a `run()` method containing its logic.
3. Jobs are instantiated and added to the `JOBS` list in `src/register_jobs.py`.
4. Running `main.py` executes the `run()` method of each job in the list.

#### Environment Variables

Set the following environment variable before running:

- `PLAYER_COUNT_WEBHOOK_URL`: The Discord webhook URL where updates for Steam player count will be posted.

### Running locally

Just run with uv:

``` bash
uv run main.py
```

### Adding New Jobs

1. Create a new class in `src/jobs/` that inherits from `Job` and implements the `run()` method.
2. Import and instantiate your job in `src/register_jobs.py`, adding it to the `JOBS` list.

---
