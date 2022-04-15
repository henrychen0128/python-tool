import json
import requests

if __name__ == '__main__':
   my_data = {'store_no':'1',''}
   headers = {'Content-Type': 'application/json'}
   url = ''
   r = requests.post(url, data=json.dumps(my_data), headers=headers)
   print(r.status_code)


