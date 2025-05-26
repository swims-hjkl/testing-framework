import requests
import os

backend_url = os.getenv("BACKEND_URL")
backend_url = "http://localhost:5002"


def main():
    response = requests.get(backend_url)
    if response.text != "hello":
        print("error: not passing")
    else:
        print("pass")


if __name__ == "__main__":
    main()
