import requests
import json
import sys
import webbrowser as wb
import os
import random

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
    print("Authorization URL: "+auth_url)
    print("If browser window does not open automatically, please paste the above URL into your browser")
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
    ##register_browser()
    auth_url = generate_auth_url(code)
    
    ##wb.get('chrome').open(str(auth_url))
    wb.open(str(auth_url))
    auth_successful = False
    uak = ''
    while True:
        try:
            confirmed = input("Press y if you allowed dive-in access to your Pocket collection: ")
            if confirmed == "y":
                uak = get_user_access_key(code)['body'][13:]
                auth_successful = True
                break
            print("Invalid option. Please press y.")
        except Exceeption as e:
            print(e)
    return (auth_successful,uak)

def write_to_file(text):
    with open('.access_token.txt','w') as f:
        f.write(text)
    f.close()

def get_user_auth_code():
    uatoken = ''
    with open('./.access_token.txt') as at:
        uatoken = at.read().strip('\n')
    at.close()
    return uatoken

def get_articles_list():
    uatoken = get_user_auth_code()
    articles_list = {}
    
    url = "https://6imslhj39g.execute-api.ca-central-1.amazonaws.com/default/LambdaTest"
    sample_event = {'mode':'gar','token':uatoken}
    resp = requests.post(url,sample_event)
    if 'message' in json.loads(resp.text):
        print("There was an error in retreiving your articles.\nPlease reauthenticate the app by deleting the .access_token.txt file and try again.")
        articles_list = {'123456789':{'given_title':'Help Document','given_url':'https://github.com/arshpunia/dive-in-client/blob/master/README.md#help-the-script-is-redirecting-me-to-this-page'}}
    else:
        articles_list = json.loads(resp.text)['body']['list']
    return articles_list

def choose_random_article(article_list):
    ##register_browser()
    article_count = len(article_list.keys())
    article_num = random.randint(0,article_count-1) 
    cc = 0
    for key in article_list.keys():
        if cc == article_num:
            print(article_list[key]['given_title'])
            print(article_list[key]['given_url'])
            ##wb.get('chrome').open(article_list[key]['given_url'])
            wb.open(article_list[key]['given_url'])
            break
        else:
            cc+=1

def main():
    user_articles = get_articles_list()
    choose_random_article(user_articles)
    ##code = get_auth_code()['body']
    ##auth_status, uak = authorize_app(code)
    ##if auth_status:
      ##  write_to_file(uak)
    
    
if __name__=="__main__":
    main()