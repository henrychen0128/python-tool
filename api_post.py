import json
import requests

if __name__ == '__main__':
   my_data = {'store_no':'1',''}
   headers = {'Content-Type': 'application/json'}
   url = ''
<<<<<<< HEAD
   r = requests.post(url, data=json.dumps(my_data), headers=headers)  
=======
   r = requests.post(url, data=json.dumps(my_data), headers=headers)
>>>>>>> test
   print(r.status_code)


