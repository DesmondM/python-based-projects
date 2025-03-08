import requests

def normalize_url(url):
    if not url.startswith(('http://', 'https://')):
        return 'http://' + url  # Default to http if no scheme is present
    return url

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        return "up" if response.status_code == 200 else "down"
    except requests.RequestException:
        return "down"

def main():
    try:
        with open("addresses.txt", "r") as file:
            addresses = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: addresses.txt not found.")
        return

    for address in addresses:
        url = normalize_url(address)
        status = check_website(url)
        print(f"{address}: {status}")

if __name__ == "__main__":
    main()
