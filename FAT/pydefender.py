# PYDEFENDER
# Developed by Raagul26, Gowtham758550, sanjeevi1277
# Scans files and urls using virustotal API built using python

import hashlib
import os
import urllib.request
import time
import menu

def pause():
    x=input('\nPress any Key to continue...\n\n')

try:
 from virustotal_python import Virustotal
except ModuleNotFoundError:
     x=os.system('python3 -m pip install virustotal_python')
     if x==0:
       print('\nInstallation Done...\n')
     else:
       print('\nInstallation Failed \n\nPlease install virustotal_python module manually...\n')
     print('\n\nPlease Restart This Program After Installation...')
     pause()
     exit()

# Print message function
def msg():
    print('Scanning', end='')
    for _ in range(5):
        time.sleep(0.4)
        print('.', end='')


# Function to check whether the api key is valid or not
def check_api(key):
    try:
        urllib.request.urlopen('https://www.duckduckgo.com')
        scanner = Virustotal(key)
        scanner.url_scan(['www.vulnweb.com'])
        report = scanner.url_report(['www.vulnweb.com'])
        if report['status_code'] == 403:
            return True
        else:
            return False
    except urllib.error.URLError:
        print('Connect to internet...')
        exit()


# Function to get api key from user
def get_api():
    if os.path.isfile('api_key'):
        pass
    else:
        try:
            key = input('Enter your Virustotal API key: ')
            if check_api(key):
                while True:
                    if check_api(key):
                        print('Invalid API Key')
                        key = input('Enter Valid Virustotal API key: ')
                    else:
                        break
            with open('api_key', 'w') as key_file:
                key_file.write(key)
            print('API Key is stored in a file\n')
        except:
            print('Something went wrong')


# Function to fetch api key from file
def fetch_api():
    if os.path.isfile('api_key'):
        with open('api_key') as key_file:
            key = key_file.read()
            if check_api(key):
                input('Invalid API...')
                exit()
        return key
    else:
        print('File not found!!!')


# Function to get file for scanning
def get_file():
    print("\n!! Don't upload personal files")
    file = input('Enter file path: ')
    if os.path.isfile(file):
        return file
    else:
        print('\nUnable to access the file')
        while True:
            file = input('Enter file path: ')
            if os.path.isfile(file):
                return file


# Function to check file for virus
def check_file(key, file):
    msg()
    scanner = Virustotal(key)
    scanner.file_scan(file)
    with open(file, 'rb') as f:
        read = f.read()
        file_hash = hashlib.sha256(read).hexdigest()
    report = scanner.file_report([file_hash])
    try:
        print('\n\nREPORT:\nStatus code:', report['status_code'])
        print('Scan date:', report['json_resp']['scan_date'])
        print('Verbose msg:', report['json_resp']['verbose_msg'])
        print('Antivirus Scanned:', report['json_resp']['total'])
        print('Positives:', report['json_resp']['positives'])
        print('sha256:', report['json_resp']['sha256'])
        print('md5:', report['json_resp']['md5'])
    except KeyError:
        print('\n""Maximum four scans per minute""')


# Function to check URL
def check_url(key):
    url = input('\nEnter URL: ')
    try:
        urllib.request.urlopen('http://' + url)
        msg()
        scanner = Virustotal(key)
        scanner.url_scan([url])
        report = scanner.url_report([url])
        try:
            print('\n\nREPORT:\nStatus_code:', report['status_code'])
            print('Scan date:', report['json_resp']['scan_date'])
            print('URL:', report['json_resp']['url'])
            print('Verbose msg:', report['json_resp']['verbose_msg'])
            print('Total Scanned:', report['json_resp']['total'])
            print('Positives:', report['json_resp']['positives'])
        except KeyError:
            print('\n""Maximum four scans per minute""')
    except:
        print('Invalid URL')


# Main function
def main():
    while True:
        try:
            urllib.request.urlopen('https://www.duckduckgo.com')
            print('''
    ██████╗ ██╗   ██╗██████╗ ███████╗███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ██████╔╝ ╚████╔╝ ██║  ██║█████╗  █████╗  █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██╔═══╝   ╚██╔╝  ██║  ██║██╔══╝  ██╔══╝  ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ██║        ██║   ██████╔╝███████╗██║     ███████╗██║ ╚████║██████╔╝███████╗██║  ██║
    ╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                               
            ''')
            get_api()
            print('\n1) File Scan\n2) Url Scan\n3) Exit')
            choice = input('\nEnter your choice: ')
            if choice == '1':
                key = fetch_api()
                file = get_file()
                check_file(key, file)
            elif choice == '2':
                key = fetch_api()
                check_url(key)
            elif choice == '3':
                print('Closing...')
                exit(0)

            input('\nPress enter to continue...')
            os.system('cls' or 'clear')
        except urllib.error.URLError:
            input('Connect to internet...')
            break


# Invoking main fn
if __name__ == '__main__':
    main()
