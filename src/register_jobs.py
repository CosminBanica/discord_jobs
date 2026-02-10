import os

from src.jobs.player_count import PlayerCountJob

# CONSTANTS
PLAYER_COUNT_WEBHOOK_URL = os.getenv("PLAYER_COUNT_WEBHOOK_URL")  # Set this in your environment variables
HIGHGUARD_APP_ID = "4128260"  # Replace with your game's Steam App ID
HIGHGUARD_GAME_NAME = "Highguard"  # Replace with your game name

JOBS = [
    PlayerCountJob(PLAYER_COUNT_WEBHOOK_URL, HIGHGUARD_APP_ID, HIGHGUARD_GAME_NAME),
]