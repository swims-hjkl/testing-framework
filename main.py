import requests
import os

backend_url = os.getenv("BACKEND_URL")
backend_url = "http://localhost:5002"


def main():
    response = requests.get(backend_url)
    if response.text != "hello":
        with open("results.txt", "w"):
            print("test case 1: failed")
    else:
        with open("results.txt", "w"):
            print("test case 1: passed")


if __name__ == "__main__":
    main()
