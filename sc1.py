import requests

sites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]

for site in sites:
    try:
        res = requests.get(site, timeout=5)
        print(f"Site: {site}, Status Code: {res.status_code}")
    except Exception as e:
        print(f"Site:{site} error: {e} ")