import requests
import io
from PIL import Image  


def make_request():

    try:
        api = 'https://118.69.190.178:5000/remove'
        image_file = "/home/aia/Nhat/AIA-Nodes/test_2.png"

        img = Image.open(image_file)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # files = {'file': open(image_file, 'rb')}
        files = {'file': img_byte_arr}

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
