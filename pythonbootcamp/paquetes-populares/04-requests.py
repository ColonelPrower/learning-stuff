"""
Requests
Nota: no hay archivos anteriores ya que requerian de servicios no gratuitos. twilio(mandar sms) y sendgrid(mandar correos)
"""

import requests

url = "https://jsonplaceholder.typicode.com/users"

r = requests.get(url, timeout=10)

# print(r.status_code, r.text)
r = r.json()
for user in r:
    print(user["name"])


url = "https://jsonplaceholder.typicode.com/users/1"
r = requests.get(url, timeout=10)
print(r.json())
