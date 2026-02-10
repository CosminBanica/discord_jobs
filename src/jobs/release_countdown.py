import requests
from datetime import datetime, timezone
from src.jobs.job_base import Job


class SteamReleaseCountdownJob(Job):
    interval = 'daily'

    def __init__(self, webhook_url: str, app_id: str, game_name: str):
        self.webhook_url = webhook_url
        self.app_id = app_id
        self.game_name = game_name

    def get_release_date(self):
        url = f"https://store.steampowered.com/api/appdetails?appids={self.app_id}&cc=us&l=en"
        response = requests.get(url)
        data = response.json()
        app_data = data.get(str(self.app_id), {}).get('data', {})
        release_date = app_data.get('release_date', {})
        if release_date.get('coming_soon') and release_date.get('date'):
            # Try to parse the date string
            try:
                # Steam dates are often like '10 Feb, 2026' or 'Q1 2026'
                return release_date['date']
            except Exception:
                return None
        return None

    def parse_release_date(self, date_str):
        # Try to parse common Steam date formats
        for fmt in ("%d %b, %Y", "%b %d, %Y", "%Y-%m-%d"):  # Add more as needed
            try:
                return datetime.strptime(date_str, fmt).replace(tzinfo=timezone.utc)
            except Exception:
                continue
        return None

    def run(self):
        try:
            date_str = self.get_release_date()
            if not date_str:
                message = f"Release date for **{self.game_name}** is not available."
            else:
                release_dt = self.parse_release_date(date_str)
                if release_dt:
                    now = datetime.now(timezone.utc)
                    days_left = (release_dt - now).days
                    if days_left > 0:
                        message = f"**{self.game_name}** releases in **{days_left}** days! (on {release_dt.strftime('%d %b, %Y')})"
                    elif days_left == 0:
                        message = f"**{self.game_name}** releases today!"
                    else:
                        message = f"**{self.game_name}** has already released!"
                else:
                    message = f"Release date for **{self.game_name}**: {date_str}"
            data = {
                "embeds": [
                    {
                        "title": f"{self.game_name} Release Countdown",
                        "description": message,
                        "color": 15844367,  # Orange
                        "footer": {"text": "Steam Tracker"}
                    }
                ]
            }
            requests.post(self.webhook_url, json=data)
            print(f"Release countdown sent: {message}")
        except Exception as e:
            print(f"Error: {e}")
