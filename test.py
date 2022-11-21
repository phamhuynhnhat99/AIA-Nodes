import requests
import io
from PIL import Image  


def make_request():

    try:
        api = 'https://118.69.190.178:5000/remove'
        image_file = 'test.png'
        files = {'file': open(image_file, 'rb')}

        response = requests.post(api, files=files, timeout=300, verify=False)
        if response.status_code == 200:
            try:
                image_path = "test_rm.png"

                img = response.content
                imageStream = io.BytesIO(img)
                imageFile = Image.open(imageStream)
                imageFile.save(image_path)

            except requests.exceptions.RequestException:
                print(response.text)

    except Exception as e:
        print(e)


make_request()
