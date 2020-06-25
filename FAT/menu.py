import passwordcrack
import metadata
import os
import pydefender

def pause():
    x=input('\nPress any Key to continue...\n\n')

def menu():
  os.system('clear')
  print('''
______ _ _         ___              _           _       _____           _ 
|  ___(_) |       / _ \            | |         (_)     |_   _|         | |
| |_   _| | ___  / /_\ \_ __   __ _| |_   _ ___ _ ___    | | ___   ___ | |
|  _| | | |/ _ \ |  _  | '_ \ / _` | | | | / __| / __|   | |/ _ \ / _ \| |
| |   | | |  __/ | | | | | | | (_| | | |_| \__ \ \__ \   | | (_) | (_) | |
\_|   |_|_|\___| \_| |_/_| |_|\__,_|_|\__, |___/_|___/   \_/\___/ \___/|_|
                                       __/ |                              
                                      |___/                               
''')
  print('\n\nMenu\n\n1)Analyze Metadata \n2)Check For Suspicious Document\n3)Crack Password Protected Files \n4)Detect Filetype\n5)About this software\n\n')
  x=input('Enter choice:')
  if x=='1':
       metadata.main()
       pause()
       menu()
       exit()
  elif x=='2':
       pydefender.main()
       pause()
       menu()
       exit()
  elif x=='3':
       passwordcrack.engine()
       pause()
       menu()
       exit()
  elif x=='4':
       fil=input('\nEnter Filename:')
       if os.path.exists(fil):
          print('\n\nDetected File Type:\n\n') 
          os.system('file -b '+fil) 
          pause()
          menu()
          exit()
  elif x=='5':
        print('''\n\nFile Analysis Tool : A simple Tool for Kali Linux to Analyze Files 
\n\n Developed by :- \n
M.Anish       [ Team Leader ] 
Rahul         [ Pydefender Module ]
Gautham S     [ Pydefender module] 
Godwin U      [ Metadata Component ]
Godwin Joy    [ Metadata Component ]''')
        pause()
        menu()
        exit()
  else:
        print('\nIncorrect choice!')
        pause()
        menu()
        exit() 
  
