import requests

# url = 'http://127.0.0.1:8000/npom/detect_and_count'

# image_path = '../data/test2.png'

# # classes = "pipe, duct, mechanical equipment, valve, pump"

# with open(image_path, 'rb') as image_file:
#     files = {'image': image_file}
#     data =  {}  # 'is_debug': False 'classes': classes Optional classes parameter
#     response = requests.post(url, files=files, data=data)

# #data = response.json()

# print("data: ", response)
# print("data: ", response.json())



# http://127.0.0.1:8000/npom/products

# http://127.0.0.1:8000/npom/products

# http://127.0.0.1:8000/npom/products_records

# http://127.0.0.1:8000/npom/volunteers



url = 'http://127.0.0.1:8000/npom/products/'

data =  {'name': 'chair', 'description': 'a chair'}
response = requests.post(url, data=data)

#data = response.json()

print("data: ", response)
print("data: ", response.json())