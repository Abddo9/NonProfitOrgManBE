import requests

# url = 'http://127.0.0.1:8000/npom/detect_and_count'

# image_path = '../data/test.jpg'

# classes = "pipe, duct, mechanical equipment, valve, pump"

# with open(image_path, 'rb') as image_file:
#     files = {'image': image_file}
#     data = {'classes': classes}  # Optional classes parameter
#     response = requests.post(url, files=files, data=data)

# #data = response.json()

# print(("data: ", response))
# print(("data: ", response.json()))




url = 'http://127.0.0.1:8000/npom/get_products_records'
response = requests.get(url)
print(response)
print(response.json())


url = 'http://127.0.0.1:8000/npom/get_volunteers'
response = requests.get(url)
print(response)
print(response.json())