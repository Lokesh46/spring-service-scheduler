import sys
import requests
import os

RENDER_API_TOKEN = os.getenv("RENDER_API_TOKEN")
SERVICE_ID_1 = os.getenv("SERVICE_ID_1")
SERVICE_ID_2 = os.getenv("SERVICE_ID_2")

def stop_service(service_id):
    url = f"https://api.render.com/v1/services/{service_id}/suspend"
    headers = {
        "Authorization": f"Bearer {RENDER_API_TOKEN}",
    }
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an error if the request fails
        print(f"Service {service_id} stopped successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error stopping service {service_id}: {e}")
        return False
    return True

def start_service(service_id):
    url = f"https://api.render.com/v1/services/{service_id}/resume"
    headers = {
        "Authorization": f"Bearer {RENDER_API_TOKEN}",
    }
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an error if the request fails
        print(f"Service {service_id} started successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error starting service {service_id}: {e}")
        return False
    return True

if __name__ == "__main__":
    # Ensure that the action ('start' or 'stop') is passed as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide 'start' or 'stop' as an argument.")
        sys.exit(1)

    action = sys.argv[1].lower()  # Get the first argument passed to the script

    if action == "stop":
        stop_service(SERVICE_ID_1)
        stop_service(SERVICE_ID_2)
    elif action == "start":
        start_service(SERVICE_ID_1)
        start_service(SERVICE_ID_2)
    else:
        print("Invalid action. Please use 'start' or 'stop'.")
        sys.exit(1)
