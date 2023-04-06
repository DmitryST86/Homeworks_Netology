import requests


class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        file_name = file_path.split('\\', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"{file_name}", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href", "")
        href_response = requests.put(href, data=open(file_path, 'rb'))
        href_response.raise_for_status()
        if href_response.status_code == 201:
            return 'Success'
        else:
            return f"Error: {href_response.status_code}"


if __name__ == '__main__':
    token = 'y0_AgAAAAA0t7BgAADLWwAAAADf663XRkuCdePFTMCNfkLJ3BtgFrUMXSI'
    path_to_file = r"C:\Users\stadn\Downloads\GGeCCSo.jpg"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
