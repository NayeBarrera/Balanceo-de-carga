from locust import HttpUser, task, between
class MyUser(HttpUser):
    wait_time=between(1,2)
    @task
    def index(self):
        responese=seslf.client.get("http://Servidor1:5000/")