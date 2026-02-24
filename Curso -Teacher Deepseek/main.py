import requests
import json

if __name__ == "__main__":
    url = 'https://app.bird.com/'
    args = {
        'name': 'Deepseek',
        'age': 30,
        'city': 'Madrid'
    }
    response = requests.get(url, params=args)
    if response.status_code == 200:  
        content = response.content
        print(content)
        file = open('httpbin.html', 'wb')
        file.write(content)
        file.close()
      
      #  file = open('github.html', 'wb')
       # file.write(content)
        #file.close()