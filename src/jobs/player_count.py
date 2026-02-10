import requests

from src.jobs.job_base import Job

def get_player_count(app_id: str) -> int:
    url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}"
    response = requests.get(url)
    data = response.json()
    return data['response']['player_count']

def send_to_discord(message: str, webhook_url: str):
    data = {"content": message}
    requests.post(webhook_url, json=data)

class PlayerCountJob(Job):
    def __init__(self, webhook_url: str, app_id: str, game_name: str):
        self.webhook_url = webhook_url
        self.app_id = app_id
        self.game_name = game_name

    def run(self):
        try:
            players = get_player_count(self.app_id)
            message = f"🎮 **{self.game_name}** currently has **{players:,}** players online!"
            send_to_discord(message, self.webhook_url)
            print(f"Update sent: {players} players")
        except Exception as e:
            print(f"Error: {e}")