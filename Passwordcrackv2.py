
#Developed By M.Anish <aneesh25861@gmail.com> only.

import os

#Function to get File Extension.
def extension(file):
  if os.path.isfile(file):
     file=file.split('.')[-1]
     return file
  else:
     print('File Not Found!')
     exit(0)

def crack():
  os.system('sudo john passwordhash.txt')
  os.system('sudo john passwordhash.txt --show')
  os.remove('passwordhash.txt')
  
def wcrack(wordlist):
  if os.path.isfile(wordlist):
    os.system('sudo john passwordhash.txt --wordlist='+wordlist+' --progress-every=10')
    os.system('sudo john passwordhash.txt --show')
    os.remove('passwordhash.txt')
  else:
    print('Wordlist Not Found!')
    exit(0)

#To crack zip files.
def zip(file):
  os.system("sudo zip2john "+file+" >passwordhash.txt")

#To crack rar files.
def rar(file):
  os.system("sudo rar2john "+file+" >passwordhash.txt")

#To crack keepass files.
def keepass(file):
  os.system("sudo keepass2john "+file+" >passwordhash.txt")

#To crack gnupg files.
def gpg(file):
  os.system("sudo gpg2john "+file+" >passwordhash.txt")

#To crack Office files.
def office(file):
  os.system("sudo python office2john "+file+" >passwordhash.txt")

#To crack dmg files.
def dmg(file):
  os.system("sudo dmg2john "+file+" >passwordhash.txt")

def main(mode):
  flag=0
  file=input('\nEnter Password Protected File:')
  if mode!=0:
    wordlist=input('\nEnter Wordlist:')
  if extension(file).lower()=='zip':
     zip(file)
  elif extension(file).lower()=='rar':
     rar(file)
  elif extension(file).lower()=='gpg':
     gpg(file)
  elif extension(file).lower()=='dmg':
     dmg(file)
  elif extension(file).lower()=='kdbx':
     keepass(file)
  elif extension(file).lower() in ['pptx','docx','xlsx']:
     office(file)
  else:
     print('Not supported')
     flag=1
  if flag==0 and mode==0:
     crack()
  elif mode!=0 and flag==0:
     wcrack(wordlist)
  

def engine():
  print('\nMenu\n\n1)Crack Password using Wordlist \n2)Crack password without Wordlist\n\n')
  x=input('Enter choice:')
  if x=='1':
     main(1)
  elif x=='2':
     main(0)
  else:
     print('Incorrect Choice!')
     exit(0)

if __name__=='__main__':
  engine()
