import requests
import time
import ast
def get_service():
    url='http://192.168.200.129:8000/sync_request'
    response=requests.get(url)
    sync_inf=response.text
    return sync_inf

if __name__ == "__main__":
    count=0
    while True:
        sync_inf_str=get_service()
        sync_inf=ast.literal_eval(sync_inf_str)#字符串转字典
        count +=1
        print('sync_inf',count)
        print(sync_inf)
        time.sleep(1)