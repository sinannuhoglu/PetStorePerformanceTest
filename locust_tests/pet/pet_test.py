from locust import HttpUser, between, task
import json
import random

headers_json = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


class PetTestUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.pet_id = random.randint(100000, 999999)

    def build_pet_payload(self, name, image_url, tag_name, status):
        return {
            "id": self.pet_id,
            "category": {"id": 1, "name": "dog"},
            "name": name,
            "photoUrls": [image_url],
            "tags": [{"id": 1, "name": tag_name}],
            "status": status
        }

    @task
    def create_pet(self):
        payload = self.build_pet_payload(
            "Karabas",
            "https://petstore.com/images/karabas.jpg",
            "friendly",
            "available"
        )
        self.client.post("/v2/pet", data=json.dumps(payload), headers=headers_json)

    @task
    def update_pet(self):
        updated_payload = self.build_pet_payload(
            "Karabas Updated",
            "https://petstore.com/images/karabas_new.jpg",
            "guard",
            "sold"
        )
        self.client.put("/v2/pet", data=json.dumps(updated_payload), headers=headers_json)

    @task
    def verify_updated_pet(self):
        response = self.client.get(f"/v2/pet/{self.pet_id}", headers=headers_json)
        try:
            if response.status_code == 200:
                data = response.json()
                name = data.get("name", "")
                status = data.get("status", "")
                print(f"Verified pet name: {name}, status: {status}")
            else:
                print(f"verify_updated_pet failed with status: {response.status_code}")
        except Exception:
            print("Failed to parse pet update response.")

    @task
    def update_pet_with_form(self):
        form_headers = {"accept": "application/json"}
        form_data = {
            "name": "Karabas",
            "status": "available"
        }
        response = self.client.post(
            f"/v2/pet/{self.pet_id}",
            data=form_data,
            headers=form_headers
        )
        print("Form data update response:", response.text)

    @task
    def verify_pet_after_form_update(self):
        response = self.client.get(f"/v2/pet/{self.pet_id}", headers=headers_json)
        try:
            if response.status_code == 200:
                data = response.json()
                name = data.get("name", "")
                status = data.get("status", "")
                print(f"Pet after form update - Name: {name}, Status: {status}")
            else:
                print(f"verify_pet_after_form_update failed with status: {response.status_code}")
        except Exception:
            print("Failed to verify pet after form update.")

    @task
    def delete_pet(self):
        self.client.delete(f"/v2/pet/{self.pet_id}", headers=headers_json)

    @task
    def verify_deleted_pet(self):
        response = self.client.get(f"/v2/pet/{self.pet_id}", headers=headers_json)
        if response.status_code == 200:
            print("Warning: Pet still exists. Deletion might have failed.")
        elif response.status_code == 404:
            print(f"Deletion verified. Status code: {response.status_code}")
        else:
            print(f"Unexpected response during deletion check: {response.status_code}")
