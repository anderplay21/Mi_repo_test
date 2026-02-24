import requests
import json

#Metodo GET

if __name__ == '__main__':
    url='https://httpbin.org/get'
    args={'nombre':'Juan', 'curso':'APIs', 'nivel':'Intermedio'}

    response=requests.get(url, params=args)

    if response.status_code==200:
       
        #response_json=response.json() #Dic
        #origin=response_json['origin']
        #print(origin)
        response_json=response.json()
        print(json.dumps(response_json, indent=2))
        origin=response_json['origin']
