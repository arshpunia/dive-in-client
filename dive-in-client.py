import requests
import json
import sys
import webbrowser as wb

def get_auth_code():
    url = "https://6imslhj39g.execute-api.ca-central-1.amazonaws.com/default/LambdaTest"
    sample_event = {'key':'value'}
    resp = requests.post(url,sample_event)
    
    print(str(json.loads(resp.text)))
    return str(json.loads(resp.text))

def generate_auth_url(req_code):
    auth_url = "https://getpocket.com/auth/authorize?request_token="+req_code[1:-1]+"&redirect_uri=https://google.com"
    print(auth_url)
    return auth_url   

def generate_access_token(code):
    api_key = get_api_key(event)
    code = "734d00b4-b070-3a95-1d9c-f07ca0"
    pocket_auth = requests.post('https://getpocket.com/v3/oauth/authorize', data = {'consumer_key':api_key, 'code': code})
    print(pocket_auth.text)
    return pocket_auth.text

def register_browser():
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))

    
def authorize_app(code):
    register_browser()
    auth_url = generate_auth_url(code)
    
    wb.get('chrome').open(str(auth_url))
    while True:
        try:
            confirmed = input("Press y if you confirmed it: ")
            if confirmed == "y":
                break
            print("Invalid option. Please press y.")
        except Exceeption as e:
            print(e)
    
def main():
    code = get_auth_code()
    ##generate_auth_url(code)
    ##authorize_app(code)
    
if __name__=="__main__":
    main()