import DiveInClient as dic
import os 

def check_file():
    if os.path.exists('./.access_token.txt'):
        file_exists = True 
    else:
        file_exists = False
    
    return file_exists

def client_driver():
    at_present = check_file()
    if at_present:
        print("Access token file exists. Now retreiving your access token...")
        dic.choose_random_article(dic.get_articles_list())
    else:
        print("Access token file not found. Commencing authentication process...")
        code = dic.get_auth_code()['body']
        auth_status, uak = dic.authorize_app(code)
        if auth_status:
            print("Authentication successful. Now writing access token to file...")
            dic.write_to_file(uak)
            dic.choose_random_article(dic.get_articles_list())

def main():
    client_driver()
    
if __name__=="__main__":
    main()