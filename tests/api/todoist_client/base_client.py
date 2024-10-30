class BaseClient:
    def __init__(self, api_token: str) -> None:
        self.base_url = "https://api.todoist.com"
        self.headers = {"Authorization": f"Bearer {api_token}"}
