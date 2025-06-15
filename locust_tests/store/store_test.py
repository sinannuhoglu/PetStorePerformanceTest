from locust import HttpUser, between, task
import json
from datetime import datetime

ORDER_ID = 90001
PET_ID = 100001

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


class StoreTestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_inventory_status(self):
        self.client.get("/v2/store/inventory", headers=headers)

    @task
    def place_order(self):
        order = {
            "id": ORDER_ID,
            "petId": PET_ID,
            "quantity": 2,
            "shipDate": datetime.utcnow().isoformat() + "Z",
            "status": "placed",
            "complete": True
        }
        self.client.post("/v2/store/order", data=json.dumps(order), headers=headers)

    @task
    def get_order_by_id(self):
        self.client.get(f"/v2/store/order/{ORDER_ID}", headers=headers)

    @task
    def delete_order(self):
        self.client.delete(f"/v2/store/order/{ORDER_ID}", headers=headers)

    @task
    def verify_order_deleted(self):
        self.client.get(f"/v2/store/order/{ORDER_ID}", headers=headers)
