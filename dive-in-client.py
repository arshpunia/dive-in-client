import requests
import json
import sys
import webbrowser as wb
import os

##Supported modes
##gac: Get auth code
##gak: Get user access key
##gar: Get articles

def get_auth_code():
    url = "https://6imslhj39g.execute-api.ca-central-1.amazonaws.com/default/LambdaTest"
    sample_event = {'mode':'gac'}
    resp = requests.post(url,sample_event)
    
    ##print(str(json.loads(resp.text)))
    return json.loads(resp.text)

def generate_auth_url(req_code):
    auth_url = "https://getpocket.com/auth/authorize?request_token="+req_code+"&redirect_uri=https://google.com"
    print(auth_url)
    return auth_url   

def generate_access_token(code):
    api_key = get_api_key(event)
    pocket_auth = requests.post('https://getpocket.com/v3/oauth/authorize', data = {'consumer_key':api_key, 'code': code})
    print(pocket_auth.text)
    return pocket_auth.text

def register_browser():
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))

def get_user_access_key(code):
    url = "https://6imslhj39g.execute-api.ca-central-1.amazonaws.com/default/LambdaTest"
    sample_event = {'mode':'gak','code':code}
    resp = requests.post(url,sample_event)
    ##print(str(json.loads(resp.text)))
    return json.loads(resp.text)    
    
def authorize_app(code):
    register_browser()
    auth_url = generate_auth_url(code)
    
    wb.get('chrome').open(str(auth_url))
    auth_successful = False
    uak = ''
    while True:
        try:
            confirmed = input("Press y if you confirmed it: ")
            if confirmed == "y":
                uak = get_user_access_key(code)['body'][13:]
                auth_successful = True
                break
            print("Invalid option. Please press y.")
        except Exceeption as e:
            print(e)
    return (auth_successful,uak)

def write_to_file(text):
    with open('access_token.txt','w') as f:
        f.write(text)
    f.close()

def get_user_auth_code():
    valid_token = False
    uatoken = ''
    if os.path.exists('./access_token.txt'):
        with open('access_token.txt') as at:
            uatoken = at.read().strip('\n')
        at.close()
        valid_token = True
    return (valid_token, uatoken)

def get_articles_list():
    is_valid, uatoken = get_user_auth_code()
    if is_valid:
        print("Token is valid")
        url = "https://6imslhj39g.execute-api.ca-central-1.amazonaws.com/default/LambdaTest"
        sample_event = {'mode':'gar','token':uatoken}
        resp = requests.post(url,sample_event)
        print(str(json.loads(resp.text)))
        print(json.loads(resp.text))
    else: 
        print("Invalid token")

def main():
    get_articles_list()
    ##code = get_auth_code()['body']
    ##auth_status, uak = authorize_app(code)
    ##if auth_status:
      ##  write_to_file(uak)
    
    
if __name__=="__main__":
    main()