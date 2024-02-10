import concurrent.futures
import requests
import sys

try:
    
    target_url = input('[*] Enter Target URL: ')
    file_name = input('[*] Enter Name Of The File Containing Directories: ')

    def request(url):
        try:
            response = requests.get("http://" + url)
            return response
        except requests.exceptions.ConnectionError:
            pass

    def process_directory(directory):
        full_url = f'{target_url}/{directory}'
        response = request(full_url)

        if response:
            status_code = response.status_code
            redirect_url = response.url

            print(f'/{directory.ljust(20)} (Status: {status_code}) [--> {redirect_url}]')

    if __name__ == "__main__":
        with open(file_name, 'r') as file:
            directories = [line.strip() for line in file]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit tasks for each directory using the ThreadPoolExecutor
            futures = [executor.submit(process_directory, directory) for directory in directories]

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)

except Exception as e:
    print(e)
    sys.exit()



