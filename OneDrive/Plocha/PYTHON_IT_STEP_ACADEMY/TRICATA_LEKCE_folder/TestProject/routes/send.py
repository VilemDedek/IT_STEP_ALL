from app import send_post_request
import json

url = "http://127.0.0.1:5000"

data = {"data":"this is data"}

if __name__ == '__main__':
    send_post_request(url, data)
    print("sent the data")