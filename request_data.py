import requests

url = "http://localhost:5000/avalanche"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print("Response:")
print(response.json())