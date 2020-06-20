#!/usr/bin/python3.7

import os
from prompt_toolkit import prompt



def begin():
    return("\nENTER YOUR CHOICE\n1.Exiftool\n2.MAT2\n\n0.EXIT")


def main():
    while 1:
        print(begin())

        user_input = input('Enter Your Choice >> ')

        if len(user_input) != 1:
            os.system('clear')
            print("ENTER CORRECT CHOICE\n")
            continue
        try:
            choice = int(user_input)
        except ValueError:
            print("ENTER CORRECT CHOICE\n")
            continue

        if choice == 1:
            os.system('clear')
            
            while 1:
                exif_tool()
                break
            continue

        elif choice == 2:
            os.system('clear')
            
            while 1:
                mat2_tool()
                break
            continue

        elif choice == 0:
            os.system('clear')
            exit()


# ********************* Exif *****************************

def exif_tool():
    pwd = os.getcwd()
    print('Enter the File (or) Folder name >> ')
    file = prompt()
    os.system('exiftool -c "%.6f" {0}'.format(file))
    os.system('exiftool -c "%.6f" {0} -gpsposition > out.txt'.format(file))
    with open('out.txt',"r") as s:
    	file_read('s')


    try:
        input("\nPress Enter To Continue.....")
        os.system('clear')

    except e:
        
        os.system('clear')
        pass



# ******************* MAT2 **********************************

def mat2_tool():
    print('Enter the File (or) Folder name >> ')
    file = prompt()
    os.system('mat2 -s {0}'.format(file))

    try:
        input("\nPress Enter To Continue.....")
        os.system('clear')

    except e:
        
        os.system('clear')
        pass


def file_read(s):
	with open('out.txt',"r") as f:
		l=f.readlines()
	try:
		if (len(l) != 0 ):
			a=l[0]
			lat = a[34:43]
			lon = a[47:56]
			print("\n\nOpen this link in browser to see the location :\n")
			print("http://maps.google.com/maps?q={0},{1}".format(lat,lon))
			os.remove('out.txt')
		else:
			print("No Location Details Was Found!!!")
			os.remove('out.txt')
	except e:
		pass


try:
    
    main()
except KeyboardInterrupt:
    os.system('clear')
    quit("")

