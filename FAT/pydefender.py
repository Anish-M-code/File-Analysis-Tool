# PYDEFENDER
# Developed by Raagul26, Gowtham758550, sanjeevi1277
# Scans files and urls using virustotal API built using python

''' /* This module was patched by Anish M to make it work with
       this File Analysis tool Project Please ensure to undo patches for other use. */'''
 
import hashlib
import os
import urllib.request
import time
import getpass

#PATCH 1
import menu                                  #For use in File Analysis Tool only.

def pause():
    x=input('\nPress any Key to continue...\n\n')

#Patch 2
#Beginning of Patch
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
#end of patch

# Print message function
def msg():
    print('Scanning', end='')
    for _ in range(5):
        time.sleep(0.4)                                             # prints statement after 0.4 sec
        print('.', end='')


# Function to check whether the api key is valid or not
def check_api(key):
    try:
        urllib.request.urlopen('https://www.duckduckgo.com')        # opens url to check internet connection
        scanner = Virustotal(key)
        scanner.url_scan(['www.vulnweb.com'])
        report = scanner.url_report(['www.vulnweb.com'])
        if report['status_code'] == 403:                            # checks if status code is 403
            return True
        else:
            return False
    except urllib.error.URLError:
        input('Connect to internet...')
        exit()


# Function to get api key from user
def get_api():
    if os.path.isfile('api_key'):                                   # checks api_key file is there are not
        pass
    else:
        try:
            key = getpass.getpass(prompt='Enter your Virustotal API key: ')  # If no api_key file,then get key from user
            if check_api(key):                                      # checks api key is valid or not (True or False)
                while True:
                    if check_api(key):                              # checks api key is valid or not (True or False)
                        print('Invalid API Key')
                        key = getpass.getpass(prompt='EnterValid Virustotal API key: ')  # If api_key is invalid,then get key from user
                    else:
                        break
            with open('api_key', 'w') as key_file:                  # Opens file name api_key in write mode
                key_file.write(key)                                 # Writes api key in a file
            print('API Key is stored in a file\n')
        except:
            print('Something went wrong')


# Function to fetch api key from file
def fetch_api():
    if os.path.isfile('api_key'):                                   # checks api_key file is there are not
        with open('api_key') as key_file:                           # opens api_key file in read mode
            key = key_file.read()                                   # reads key from the file
            if check_api(key):                                      # checks api key is valid or not (True or False)
                input('Invalid API...')
                exit()                                              # exits the program
        return key                                                  # returns api key
    else:
        print('File not found!!!')


# Function to get file for scanning
def get_file():
    print("\n!! Don't upload personal files")
    file = input('Enter file path: ')                               # get file path from user
    if os.path.isfile(file):                                        # checks entered file is there are not
        return file                                                 # returns entered file name
    else:
        print('\nUnable to access the file')
        while True:
            file = input('Enter file path: ')                       # get file path from user
            if os.path.isfile(file):                                # checks entered file is there are not
                return file                                         # returns entered file name


# Function to check file for virus
def check_file(key, file):
    msg()                                                           # prints scanning message
    scanner = Virustotal(key)                                       # passing api key to Virustotal class
    scanner.file_scan(file)                                         # scans the file for virus
    with open(file, 'rb') as f:                                     # opens file in read binary mode
        read = f.read()                                             # reads opened file
        file_hash = hashlib.sha256(read).hexdigest()                # Get sha256 hash of file
    report = scanner.file_report([file_hash])    # passing hash value of file to file_report function and returns report
    try:
        print('\n\nREPORT:\nStatus code:', report['status_code'])   # Prints all the reports
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
    url = input('\nEnter URL: ')                                    # Get url from the user
    try:
        urllib.request.urlopen('http://' + url)                     # Checks the given url is valid
        msg()                                                       # prints scanning message
        scanner = Virustotal(key)                                   # passing api key to Virustotal class
        scanner.url_scan([url])                                     # passing url to url_scan function
        report = scanner.url_report([url])                          # returns report of the url
        try:
            print('\n\nREPORT:\nStatus_code:', report['status_code'])  # Prints all the reports
            print('Scan date:', report['json_resp']['scan_date'])
            print('URL:', report['json_resp']['url'])
            print('Verbose msg:', report['json_resp']['verbose_msg'])
            print('Total Scanned:', report['json_resp']['total'])
            print('Positives:', report['json_resp']['positives'])
        except KeyError:
            print('\n""Maximum four scans per minute""')            # prints if you reach maximum attempts
    except:
        print('Invalid URL')


# Main function
def main():
    while True:
        try:
            urllib.request.urlopen('https://www.duckduckgo.com')    # checks if you have internet connection
            print('''
    ██████╗ ██╗   ██╗██████╗ ███████╗███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ██████╔╝ ╚████╔╝ ██║  ██║█████╗  █████╗  █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██╔═══╝   ╚██╔╝  ██║  ██║██╔══╝  ██╔══╝  ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ██║        ██║   ██████╔╝███████╗██║     ███████╗██║ ╚████║██████╔╝███████╗██║  ██║
    ╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                               
            ''')
            get_api()                                               # invoking get_api function
            print('\n1) File Scan\n2) Url Scan\n3) Exit')           # displays menu
            choice = input('\nEnter your choice: ')                 # get user choice
            if choice == '1':
                key = fetch_api()                                   # invokes fetch_api function
                file = get_file()                                   # invokes get_file function
                check_file(key, file)                               # invokes check_file function
            elif choice == '2':
                key = fetch_api()                                   # invokes fetch_api function
                check_url(key)                                      # invokes check_url function
            elif choice == '3':
                print('Closing...')
#PATCH 3
                menu.menu()

            input('\nPress enter to continue...')
            os.system('clear')
        except urllib.error.URLError:
            input('Connect to internet...')
            break


# Invoking main fn
if __name__ == '__main__':
    main()
