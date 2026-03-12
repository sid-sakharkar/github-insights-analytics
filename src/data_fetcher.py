import requests
import time

class GitHubDataFetcher:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://api.github.com'
        self.headers = {'Authorization': f'token {self.token}', 'Accept': 'application/vnd.github.v3+json'}
        self.rate_limit_remaining = None
        self.rate_limit_reset = None

    def fetch_data(self, endpoint):
        self._check_rate_limit()
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, headers=self.headers)
        self._handle_response(response)
        return response.json()

    def _check_rate_limit(self):
        if self.rate_limit_remaining is None:
            self.rate_limit_remaining, self.rate_limit_reset = self._get_rate_limit() 
        if self.rate_limit_remaining == 0:
            sleep_time = self.rate_limit_reset - int(time.time())
            if sleep_time > 0:
                print(f'Rate limit exceeded. Sleeping for {sleep_time} seconds.')
                time.sleep(sleep_time)
            self.rate_limit_remaining, self.rate_limit_reset = self._get_rate_limit()

    def _get_rate_limit(self):
        response = requests.get(f'{self.base_url}/rate_limit', headers=self.headers)
        data = response.json()
        remaining = data['rate']['remaining']
        reset = data['rate']['reset']
        return remaining, reset

    def _handle_response(self, response):
        if response.status_code != 200:
            raise Exception(f'Error fetching data: {response.status_code} - {response.text}')