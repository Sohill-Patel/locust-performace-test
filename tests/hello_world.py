from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://petstore.octoperf.com/actions/Catalog.action;jsessionid=6D891EFE7BF37FDF95AF907160A313AC?viewCategory=&categoryId=FISH")