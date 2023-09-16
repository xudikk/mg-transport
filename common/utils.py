import requests
from typing import List, Tuple, Dict

BASE_URL = "https://mahalla.technocorp.uz/api"


class TechnoCorpClient:
    def __init__(self, *args, **kwargs):
        self.username = "Mahmudov"
        self.password = "FFzbcYh9"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        }
        self.LoginUrl = "%s/auth/login" % BASE_URL
        self.GetRegionUrl = "%s/v1/regions?direction=true" % BASE_URL
        self.GetDistrictsUrl = "%s/v1/districts?direction=true&size=300" % BASE_URL
        self.GetNeighborhoodsUrl = (
            "%s/v1/mahalla?size=10000&sort=name&direction=true&districtId=200"
            % BASE_URL
        )
        self.GetNeighborhoodInfo = f"{BASE_URL}/v1/mahalla/%s/info"

    def login(self) -> Tuple[bool, dict]:
        data = {
            "username": self.username,
            "password": self.password,
        }
        try:
            response = requests.post(
                url=self.LoginUrl,
                headers=self.headers,
                json=data,
                timeout=5,
            )
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return False, {
                "message": "Connection Error or Timeout",
            }

        if response.status_code != 200:
            return False, {
                "message": "Invalid username or password",
            }

        self.headers["Cookie"] = response.headers["Set-Cookie"]
        return True, response.json()

    def get_list(self, url: str) -> List[dict]:
        login_status, login_data = self.login()
        if not login_status:
            return []

        try:
            response = requests.get(url=url, headers=self.headers, timeout=5)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print("Connection Error or Timeout")
            return []

        if response.status_code != 200:
            print(f"Status Code: {response.status_code}")
            return []

        try:
            data = response.json()["data"]["content"]
        except KeyError:
            return []

        return data

    def get_regions(self) -> List[Dict]:
        return self.get_list(url=self.GetRegionUrl)

    def get_districts(self) -> List[Dict]:
        return self.get_list(url=self.GetDistrictsUrl)

    def get_neighborhoods(self) -> List[Dict]:
        return self.get_list(url=self.GetNeighborhoodsUrl)

    def get_neighborhood_info(self, neighborhood_id: int) -> Tuple[bool, Dict]:
        login_status, login_data = self.login()
        if not login_status:
            return False, {}

        try:
            response = requests.get(
                url=self.GetNeighborhoodInfo % neighborhood_id,
                headers=self.headers,
                timeout=5,
            )
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print("Connection Error or Timeout")
            return False, {}

        if response.status_code != 200:
            print(f"Status Code: {response.status_code}")
            return False, {}

        try:
            data = response.json()["data"]
        except KeyError:
            return False, {}

        return True, data
