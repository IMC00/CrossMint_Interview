import json

import tenacity
from requests import Session, Response, HTTPError
from tenacity import wait_incrementing

from src.config import EXERCISE_API, CANDIDATE_ID
from src.enumerates import HTTPStatusCode


class TooManyRequests(Exception):
    """Too many requests"""


class AstralApiHelper:
    def __init__(self):
        self.api_url = EXERCISE_API
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    @staticmethod
    def __generate_base_params__():
        params = {'candidateId': CANDIDATE_ID}
        return params

    @tenacity.retry(wait=wait_incrementing(start=0, increment=1, max=10))
    def api_call(self, type_request: HTTPStatusCode, endpoint: str, params: dict = None) -> Response:
        message_params = AstralApiHelper.__generate_base_params__()
        if params:
            message_params.update(params)
        payload = json.dumps(message_params)

        url = self.api_url + endpoint

        response = self.session.request(str(type_request), url, data=payload)
        if response.status_code == 429:
            raise TooManyRequests

        return response

    def get_astral_board(self) -> dict:
        endpoint = '/map/' + CANDIDATE_ID + '/goal'
        response = self.api_call(HTTPStatusCode.GET, endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.content)
            raise HTTPError('Unable to retrieve goal board')


ASTRAL_API_HELPER = AstralApiHelper()
