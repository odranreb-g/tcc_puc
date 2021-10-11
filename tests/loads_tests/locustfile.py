from locust import FastHttpUser, task


class DeliveriesEndpoint(FastHttpUser):
    @task
    def develiveries(self):
        self.client.get("/deliveries/?format=json")
