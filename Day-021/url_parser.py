from urllib.parse import urlparse

url = "https://example.com:443/products?id=10&name=phone"

result = urlparse(url)

print("Scheme :", result.scheme)
print("Host   :", result.hostname)
print("Port   :", result.port)
print("Path   :", result.path)
print("Query  :", result.query)
