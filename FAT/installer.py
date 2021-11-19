
''' Installer for File Analysis Tool Developed by M.Anish
    Installs thirdparty tools requied for this tool. ''' 


import platform
import os


if platform.system().lower()!='linux':
   print('Platform not supported!')
   

flag=0

def detect(tool,cmd):
  print('\n\nDetecting '+tool+' ...\n')
  x=os.system(cmd)
  if x!=0:
     print('\nInstalling '+tool)
     global flag
     if flag==0:
        os.system('sudo apt-get update')
        flag=1
     x=os.system('sudo apt-get install '+tool)
     if x==0:
        print(tool+' installed successfully')

def detect_mat2():
  detect('mat2','mat2 -v')

def detect_exiftool():
  detect('exiftool','exiftool -ver')

def detect_pip():
  detect('python3-pip','python3 -m pip --version')

def first_run():
    os.chdir('FAT')
    if os.path.exists('init.dat')==False:
       detect_mat2()
       detect_exiftool()
       detect_pip()
       os.system('echo >init.dat')
    os.chdir('..')
    
  
  

   
