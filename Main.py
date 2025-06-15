import subprocess
import os


def run_locust():
    print("=== PetStore Locust Load Test Runner ===")
    print("Test Seçenekleri:")
    print("1 - Pet Test")
    print("2 - Store Test")
    print("3 - User Test")

    choice = input("Lütfen çalıştırmak istediğiniz testi seçin (1/2/3): ").strip()

    path_map = {
        "1": "locust_tests/pet/pet_test.py",
        "2": "locust_tests/store/store_test.py",
        "3": "locust_tests/user/user_test.py"
    }

    if choice not in path_map:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3 giriniz.")
        return

    selected_path = path_map[choice]
    if not os.path.exists(selected_path):
        print(f"Hata: {selected_path} dosyası bulunamadı.")
        return

    print(f"\n'{selected_path}' çalıştırılıyor...\n")
    subprocess.run(f"locust -f {selected_path}", shell=True)


if __name__ == "__main__":
    run_locust()
