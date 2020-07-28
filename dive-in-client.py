import requests
import json
import sys
import webbrowser as wb

def get_auth_code_url():
    url = "https://6imslhj39g.execute-api.ca-central-1.amazonaws.com/default/LambdaTest"
    sample_event = {'key':'value'}
    resp = requests.post(url,sample_event)
    
    return str(json.loads(resp.text)['body'])

def register_browser():
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))

    
def authorize_app():
    register_browser()
    auth_url = get_auth_code_url()
    
    wb.get('chrome').open(str(auth_url)[1:-1])
    while True:
        try:
            confirmed = input("Press y if you confirmed it: ")
            if confirmed == "y":
                break
            print("Invalid option. Please press y.")
        except Exceeption as e:
            print(e)
    
def main():
    ##get_auth_code_url()
    authorize_app()
    
if __name__=="__main__":
    main()