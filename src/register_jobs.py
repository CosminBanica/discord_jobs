import os
import json

from src.jobs.player_count import SteamPlayerCountJob
from src.jobs.release_countdown import SteamReleaseCountdownJob

# CONSTANTS
PLAYER_COUNT_WEBHOOK_URL = os.getenv("PLAYER_COUNT_WEBHOOK_URL")  # Set this in your environment variables
RELEASE_COUNTDOWN_WEBHOOK_URL = os.getenv("RELEASE_COUNTDOWN_WEBHOOK_URL")  # Set this in your environment variables
JOBS_CONFIG = os.getenv("JOBS_CONFIG")  # Should be a JSON string

JOBS = []
if JOBS_CONFIG:
    try:
        jobs_data = json.loads(JOBS_CONFIG)
        for job_def in jobs_data:
            job_type = job_def.get("type")
            app_id = job_def.get("app_id")
            game_name = job_def.get("game_name")
            if job_type == "player_count":
                JOBS.append(SteamPlayerCountJob(PLAYER_COUNT_WEBHOOK_URL, app_id, game_name))
            elif job_type == "release_countdown":
                JOBS.append(SteamReleaseCountdownJob(RELEASE_COUNTDOWN_WEBHOOK_URL, app_id, game_name))
    except Exception as e:
        print(f"Error parsing JOBS_CONFIG: {e}")