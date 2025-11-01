import requests

# Your Render API token
API_TOKEN = 'your-render-api-token'

# Service IDs for your Spring backend services
SERVICE_ID_1 = 'your-service-id-1'
SERVICE_ID_2 = 'your-service-id-2'

# Base URL for Render API
BASE_URL = "https://api.render.com/v1/services"

# Headers to pass the API Token for authorization
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

# Function to stop a service
def stop_service(service_id):
    url = f"{BASE_URL}/{service_id}/stop"
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"Service {service_id} stopped successfully.")
    else:
        print(f"Failed to stop service {service_id}. Response: {response.text}")

# Function to start a service
def start_service(service_id):
    url = f"{BASE_URL}/{service_id}/start"
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"Service {service_id} started successfully.")
    else:
        print(f"Failed to start service {service_id}. Response: {response.text}")

# Stop both services
def stop_services():
    print("Stopping services...")
    stop_service(SERVICE_ID_1)
    stop_service(SERVICE_ID_2)

# Start both services
def start_services():
    print("Starting services...")
    start_service(SERVICE_ID_1)
    start_service(SERVICE_ID_2)

# Main function to decide what to do
if __name__ == "__main__":
    action = input("Enter 'stop' to stop services or 'start' to start services: ").strip().lower()
    if action == 'stop':
        stop_services()
    elif action == 'start':
        start_services()
    else:
        print("Invalid input! Please enter either 'stop' or 'start'.")
