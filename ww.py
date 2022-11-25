import requests
import io
from PIL import Image

r = requests.post("http://118.69.82.135:5000/remove", files={ "file" : open("/home/aia/Nhat/AIA-Nodes/test_1.png","rb") }, timeout=300)
if r.status_code == 200:
    img = r.content
    imageStream = io.BytesIO(img)
    imageFile = Image.open(imageStream)
    imageFile.save("sample.png")