# Discord Jobs Runner

This repository provides a simple framework for running automated jobs that update your Discord server with information from external sources.

## Project Structure

```
main.py                  # Entry point for running jobs
src/
    register_jobs.py       # Dynamically loads jobs from environment config
    jobs/
        job_base.py          # Abstract base class for jobs
        player_count.py      # Steam player count job
        release_countdown.py # Steam release countdown job
.env                     # Local environment variables (not committed)
README.md                # This file
```

### How It Works

1. Jobs are defined as classes inheriting from `Job` (see `src/jobs/job_base.py`).
2. Jobs are dynamically loaded from a JSON configuration in the `JOBS_CONFIG` environment variable.
3. Each job type (player count, release countdown) is specified in the config with its Steam App ID and game name.
4. Running `main.py` with an interval argument executes only the jobs for that interval (`12h` or `1d`).

## Dynamic Job Configuration

You can add, remove, or modify jobs without changing the code by editing the `JOBS_CONFIG` environment variable. This can be set in your `.env` file for local development or as a GitHub Actions secret for CI/CD.

**Example `JOBS_CONFIG` value:**

```text
[{"type": "player_count", "app_id": "4128260", "game_name": "Highguard"}, {"type": "release_countdown", "app_id": "3065800", "game_name": "Marathon"}]
```

## Environment Variables

- `PLAYER_COUNT_WEBHOOK_URL`: The Discord webhook URL where updates will be posted.
- `RELEASE_COUNTDOWN_WEBHOOK_URL`: The Discord webhook URL for release countdown updates.
- `JOBS_CONFIG`: JSON array of job definitions (see above).

## Running Locally

1. Create a `.env` file in the project root:

    ```text
    PLAYER_COUNT_WEBHOOK_URL=your_webhook_url_here
    RELEASE_COUNTDOWN_WEBHOOK_URL=your_webhook_url_here
    JOBS_CONFIG=[{"type": "player_count", "app_id": "4128260", "game_name": "Highguard"}, {"type": "release_countdown", "app_id": "3065800", "game_name": "Marathon"}]
    ```

2. Run with uv (or python) and specify the type of jobs to run, by their interval:

    ```bash
    uv run main.py --interval 12h   # For 12-hour jobs (e.g., player count)
    uv run main.py --interval 1d    # For daily jobs (e.g., release countdown)
    ```

    or just run all jobs:

    ```bash
    uv run main.py
    ```

### Adding New Jobs

Create a new class in `src/jobs/` that inherits from `Job` and implements the `run()` method.

---
