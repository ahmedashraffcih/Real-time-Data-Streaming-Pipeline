def stream_data():
    import json 
    import requests
    
    res = requests.get('https://randomuser.me/api/')
    res = res.json()
    res = res['results'][0]
    print(json.dumps(res, indent=3))

stream_data()