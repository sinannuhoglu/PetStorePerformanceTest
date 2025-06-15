from locust import HttpUser, task, between
import json

USER_ID = 1001
USERNAME = "testuser01"
FIRST_NAME = "Sinan"
LAST_NAME = "Nuhoglu"
EMAIL = "sinan.nuhoglu@example.com"
PASSWORD = "password123"
PHONE = "1234567890"

UPDATED_FIRST_NAME = "Simon"
UPDATED_EMAIL = "simon.nuhoglu@example.com"
UPDATED_PASSWORD = "newpass456"
UPDATED_PHONE = "9876543210"

headers_json = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


class UserTestUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Test başladığında kullanıcıyı oluştur
        user_data = {
            "id": USER_ID,
            "username": USERNAME,
            "firstName": FIRST_NAME,
            "lastName": LAST_NAME,
            "email": EMAIL,
            "password": PASSWORD,
            "phone": PHONE,
            "userStatus": 1
        }
        response = self.client.post("/v2/user", data=json.dumps(user_data), headers=headers_json)
        print(f"[on_start - Create] Status: {response.status_code}")

    @task
    def get_user(self):
        response = self.client.get(f"/v2/user/{USERNAME}", headers=headers_json)
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"[Get] Username: {data.get('username')}")
            except Exception:
                print("[Get] JSON parse failed.")
        else:
            print(f"[Get] User not found. Status: {response.status_code}")

    @task
    def update_user(self):
        updated_data = {
            "id": USER_ID,
            "username": USERNAME,
            "firstName": UPDATED_FIRST_NAME,
            "lastName": LAST_NAME,
            "email": UPDATED_EMAIL,
            "password": UPDATED_PASSWORD,
            "phone": UPDATED_PHONE,
            "userStatus": 1
        }

        response = self.client.put(f"/v2/user/{USERNAME}", data=json.dumps(updated_data), headers=headers_json)
        print(f"[Update] Status: {response.status_code}")

    @task
    def verify_updated_user(self):
        response = self.client.get(f"/v2/user/{USERNAME}", headers=headers_json)
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"[Verify Update] Name: {data.get('firstName')}, Email: {data.get('email')}")
            except Exception:
                print("[Verify Update] JSON parse failed.")
        else:
            print(f"[Verify Update] User not found. Status: {response.status_code}")

    @task
    def delete_user(self):
        response = self.client.delete(f"/v2/user/{USERNAME}", headers=headers_json)
        print(f"[Delete] Status: {response.status_code}")

    @task
    def verify_user_deleted(self):
        response = self.client.get(f"/v2/user/{USERNAME}", headers=headers_json)
        if response.status_code == 404:
            print("[Verify Delete] User deletion confirmed.")
        else:
            print(f"[Verify Delete] Warning: User still exists. Status: {response.status_code}")
