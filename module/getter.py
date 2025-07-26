import requests

class Getter():

    BASE_URL = "https://rdb.altlinux.org/api/export/branch_binary_packages/"

    def get_packages(self, branch: str):
        url = f"{self.BASE_URL}{branch}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
