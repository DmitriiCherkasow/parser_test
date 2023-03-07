import requests

data = {"custname": "login",
        "custtel": "455465454",
        "custemail": "remail@loin.com",
        "size": "medium",
        "topping": "bacon",
        "delivery": "",
        "comments": ""}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6405b5af-5aeabb232d52971671cdd3d6"
  }

variable = requests.Session()

aaa = variable.get("https://httpbin.org/forms/post")
response = variable.post("https://httpbin.org/post", headers=headers, data=data, allow_redirects=True)

print(response.text)
