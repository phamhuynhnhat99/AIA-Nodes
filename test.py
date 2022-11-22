import requests
import io
from PIL import Image  


def make_request():

    try:
        api = 'https://118.69.190.178:5000/remove'
        image_file = "/home/aia/Nhat/AIA-Nodes/test.png"
        files = {'file': open(image_file, 'rb')}

        response = requests.post(api, files=files, timeout=300, verify=False)
        if response.status_code == 200:
            try:
                image_path = image_file.split(".")[0] + "_rb.png"

                imageStream = io.BytesIO(response.content)
                imageFile = Image.open(imageStream)
                imageFile.save(image_path)

                image = Image.open(image_path)
                image.show()

            except requests.exceptions.RequestException:
                print(response.text)

    except Exception as e:
        print(e)


make_request()
