import requests

r = requests.get("https://smrabbireza.xyz")
print(r.status_code)
print(r.ok)