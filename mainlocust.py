import locust
import requests
from locust import HttpUser
from locust import between
from locust import task

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_api(self):
        resp = self.client.get('http://172.31.0.67:8080/')
        assert resp.status_code == 200

if __name__ == "__main__":
    import os
    os.system("locust -f mainlocust.py --host=http://172.31.0.67:8080")
    """浏览器访问：http://localhost:8089/"""
