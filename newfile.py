list_3 = ['Accidental', '4daa7fe9', 'eM131Me', 'Y!.90']
secret = []

for x in list_3:
    secret.append(x[:1])

print(''.join(secret))

# testing fibonacci sequence
squares = [x**2 for x in range(5)]
print(squares)

multiples_of_three = [i * 3 for i in range(10) if i % 3 != 0]
print(multiples_of_three)


'''
import requests

def dir_enum(base_url, wordlist):
    try:
        with open(wordlist, 'r') as file:
            directories = file.readlines()

        for directory in directories:
            directory = directory.strip()  # Remove leading/trailing whitespaces
            url = f"{base_url}/{directory}"

            response = requests.get(url)

            if response.status_code == 200:
                print(f"[+] Directory found: {url}")
            elif response.status_code == 403:
                print(f"[-] Forbidden: {url}")
            elif response.status_code == 404:
                print(f"[-] Not Found: {url}")
            else:
                print(f"[?] Status {response.status_code}: {url}")

    except FileNotFoundError:
        print("Error: Wordlist file not found.")

if __name__ == "__main__":
    base_url = input("Enter the base URL (e.g., http://example.com): ")
    wordlist = input("Enter the path to the wordlist file: ")

    dir_enum(base_url, wordlist)












    import concurrent.futures
import requests

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
        size = len(response.content)
        redirect_url = response.url

        print(f'/{directory.ljust(20)} (Status: {status_code}) [Size: {size}] [--> {redirect_url}]')

if __name__ == "__main__":
    with open(file_name, 'r') as file:
        directories = [line.strip() for line in file]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each directory using the ThreadPoolExecutor
        futures = [executor.submit(process_directory, directory) for directory in directories]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)



'''
