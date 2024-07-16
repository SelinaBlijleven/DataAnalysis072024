"""
call_api.py

We can call any kind of API with the requests library. Usually the code for the
GET-request is fairly simple, while the processing of the data requires more specific knowledge.

The GET-request is used to retrieve information. Other popular types of requests are POST/PUT and DELETE.
We can only use these if we have permission to edit the data in the application, while GET is mostly
used to read data and usually requires fewer permissions.
"""

# The requests library is for basic HTTP requests
import requests

URL = "https://api.openweathermap.org/data/2.5/weather?appid=d1526a9039658a6f76950cff21823aff&units=metric&mode=json" \
      "&lang=nl&q=Amsterdam"


def get_request(url: str):
    res: requests.Response = requests.get(url)

    # We can check the status code of the response, which should be
    # 200 (ok) if we were able to fetch the data.
    if res.status_code == 200:
        print(res.json())
        return res.json()

    # If we get here, the request was not successful
    print(f"Request unsuccessful")
    return None


if __name__ == "__main__":
    get_request(URL)
