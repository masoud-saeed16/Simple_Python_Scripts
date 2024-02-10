import concurrent.futures
import requests
import sys

target_domain = input('[*] Enter Target Domain: ')
wordlist_file = input('[*] Enter Name Of The File Containing Subdomains: ')

def request(subdomain):
    try:
        response = requests.get(f"http://{subdomain}.{target_domain}")
        return response
    except requests.exceptions.ConnectionError:
        pass

def process_subdomain(subdomain):
    full_url = f'http://{subdomain}.{target_domain}'
    response = request(subdomain)

    if response:
        status_code = response.status_code
        redirect_url = response.url

        print(f'{subdomain.ljust(20)} (Status: {status_code}) [--> {redirect_url}]')

if __name__ == "__main__":
    with open(wordlist_file, 'r') as file:
        subdomains = [line.strip() for line in file]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each subdomain using the ThreadPoolExecutor
        futures = [executor.submit(process_subdomain, subdomain) for subdomain in subdomains]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)
