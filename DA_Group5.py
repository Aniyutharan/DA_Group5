# T3
import requests
# T4
url = 'https://brickset.com/sets/year-2002'
# T5 i
r = requests.get(url)
print(r.text)
# T5 ii
print("Status code:")
print("\t *", r.status_code)
# T5 iii
h = requests.head(url)
print("Header:")
print("*********")
for x in h.headers:
    print("\t", x, ":", h.headers[x])
print("***********")
# T5 iv
headers = {
    'User-Agent':'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
# Source reference from "Lab 10b - Spoofing header in HTTP Get request"
# ~Aniyutharan

