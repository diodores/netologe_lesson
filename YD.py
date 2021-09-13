import requests


class YaUploader:

    def __init__(self, token):
        self.token = token
        self.the_path_to_yandex_disk = "Test/"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, disk_file_path):
        the_path_to_yandex_disk = self.the_path_to_yandex_disk + '\\'.join(disk_file_path.split('\\')[:1:-1])
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": the_path_to_yandex_disk, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href", "")
        response = requests.put(href, data=open(disk_file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    path_to_file = "D:\Решение задач\Поиск друга.py"
    token = ""
    the_path_to_yandex_disk = "Test/"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)