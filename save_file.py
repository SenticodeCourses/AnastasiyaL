import json, os


def create_dir(url):
    url_split = url.split('/')
    file_name = url_split[-2] + '.' + url_split[-1] + '.json'
    folder_name = url_split[-3]
    path = "data\\" + folder_name + "\\"
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = path + file_name
    return file_path


def save_json(url, data):
    file_path = create_dir(url)
    json_rows = json.dumps(data, ensure_ascii=False)
    file = open(file_path, 'w')
    file.write(json_rows)
    file.close()
