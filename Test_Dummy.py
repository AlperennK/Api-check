import pytest
from pytest import mark
import requests

class Test_Check_Status_Code():

    def test_check_status_code(self):
        url = "https://jsonplaceholder.typicode.com/posts/1/comments"
        response = requests.request("GET", url)
        assert response.status_code == 200
