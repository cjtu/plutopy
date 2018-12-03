# Download the image from Google Drive if it does not exist
# See: https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url
import gdal
import requests
from os import path

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def get_pluto_image():
    d = path.dirname(path.realpath(__file__))
    f = path.join(d, 'data/pluto.tif')
    if not path.exists(f):
        file_id = '1oRetMNV-FAu-qog2ckJaFZECMzawTGIE'
        with open(f, 'w+'):
            download_file_from_google_drive(file_id, f)
    return gdal.Open(f)
