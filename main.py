import sys
import requests
import json, os
import zipfile


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        str = f.read()
        config = json.loads(str)

    headers = config["headers"]
    
    for task in config["tasks"]:
        if "headers" in task:
            headers = task["headers"]
        else:
            headers = config["headers"]
        try:
            with open(task["file_name"],"wb") as file:
                response = requests.get(task["file_url"], stream=True, headers=headers, timeout=30)
                for data in response.iter_content(chunk_size=1024*1024):
                    if data:
                        file.write(data)
                response.close()
        except Exception as e:
            print(e)
    
    
    f = zipfile.ZipFile(config["output"], 'w', zipfile.ZIP_DEFLATED)
    for task in config["tasks"]:
        f.write(task["file_name"], task["file_name"])
    f.close()
    