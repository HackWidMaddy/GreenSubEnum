import re
import sys
import requests
import threading
def print_colored_banner():
    banner = '''
   \033[92m_____                      _____       _     ______                       
  \033[92m/ ____|                    / ____|     | |   |  ____|                      
 \033[92m| |  __ _ __ ___  ___ _ __ | (___  _   _| |__ | |__   _ __  _   _ _ __ ___  
 \033[92m| | |_ | '__/ _ \/ _ \ '_ \ \___ \| | | | '_ \|  __| | '_ \| | | | '_ ` _ \ 
 \033[92m| |__| | | |  __/  __/ | | |____) | |_| | |_) | |____| | | | |_| | | | | | |
  \033[92m\_____|_|  \___|\___|_| |_|_____/ \__,_|_.__/|______|_| |_|\__,_|_| |_| |_|
                                                                  
    '''
    name = "\033[97m~ Madhav Shah \033[0m"
    print(f"{banner}\n{name:^150s}")

print_colored_banner()

def check_subdomain(sub, domain):
    try:
        subdomain = sub + '.' + domain
        response_443 = requests.get('https://' + subdomain)
        response_80 = requests.get('http://' + subdomain)
        if response_443.status_code == 200:
            print('https://' + subdomain)
        elif response_80.status_code == 200:
            print('http://' + subdomain)
    except:
        pass

def main():
    domain = input("Enter the domain name: ")
    domain_regex = r'^(?!:\/\/)(?![0-9]+$)(?!-)[a-zA-Z0-9-]{1,63}(?<!-)(\.[a-zA-Z]{2,})+$'
        
    if not re.match(domain_regex, domain):
        print("Enter valid domain: example.com")    
        sys.exit()
    
    num_threads = int(input("Enter the number of threads: "))
    if num_threads <= 0:
        print("Number of threads should be greater than 0.")
        sys.exit()
    
    with open('wordlist.txt') as var:
        data = var.read()
    
    data = data.split('\n')
    
    threads = []
    for i in range(min(num_threads, len(data))):
        t = threading.Thread(target=check_subdomain, args=(data[i], domain))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
