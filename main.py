import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token)}
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()
    def upload(self, disk_file_path: str):
        href = self._get_upload_link(disk_file_path=d_file_path).get("href", "")
        response = requests.put(href, data=open(d_file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
if __name__ == '__main__':
    TOKEN = ''
    d_file_path = 'one.txt'
    uploader = YaUploader(token=TOKEN)
    uploader.upload('one.txt')