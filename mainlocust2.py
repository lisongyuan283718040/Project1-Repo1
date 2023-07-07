# 保存为main2.py
# coding:utf-8
from locust import HttpUser
from locust import TaskSet
from locust import task
import requests
import locust

class BlogDemo(TaskSet):
    """用户行为：打开我的博客首页demo"""
    @task(1)
    def open_blog(self):
        # 定义requests的请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        r = self.client.get("/yoyoketang", headers=header, verify=False)
        print(r.status_code)
        assert r.status_code == 200

class websitUser(HttpUser):
    task_set = BlogDemo
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒
    # host = "http://localhost:8888"  #（待测试的ip或者域名）

if __name__ == "__main__":
    import os
    os.system("locust -f mainlocust2.py --host=https://www.cnblogs.com")
    """浏览器访问：http://localhost:8089/"""