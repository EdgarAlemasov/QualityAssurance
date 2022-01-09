import requests


path = 'hello_world'
token = 'AQAAAAAZBVfCAADLW9y7rtLhAEDCjLKWeUqxUCQ'


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }


def create_folder(path):
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    resp = requests.put(f'{upload_url}?path={path}', headers=get_headers())
    return resp.status_code


def list_folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.get(f'{url}?path={path}', headers=get_headers())
    return response.status_code


if __name__ == '__main__':
    path = 'hello_world'
    token = 'AQAAAAAZBVfCAADLW9y7rtLhAEDCjLKWeUqxUCQ'
    create_folder(path)
    list_folder(path)
