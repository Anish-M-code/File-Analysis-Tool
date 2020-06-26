# File-Analysis Tool
<p align = "center">
<img src = "https://img.shields.io/badge/License-GPL%20v3.0-green">
<img src = "https://img.shields.io/badge/Platform-linux-inactive">
</p>

It is a simple Tool for Analysing  Files , developed in Python For Kali Linux.

## ***Install requirements***
```
$ python3 requirements.txt
```

## ***Setup***
```
$ python3 setup.py
```

## ***Usage***
```
$ python3 FAT
```
![](https://github.com/Anish-M-code/File-Analysis-Tool/blob/master/DEMO/signal-2020-06-25-220856.png)
## ***Features***

* Metadata Analysis

* File Type Detection

* Password Cracking

* Check Suspicious Files using Virustotal.

## ***Metadata Analysis***
* We use state of art  [exiftool](https://exiftool.org/) and [mat2](https://pypi.org/project/mat2/) to extract interesting metadata from
files.
![](https://github.com/Anish-M-code/File-Analysis-Tool/blob/master/DEMO/signal-2020-06-25-222429.png)

## ***File Type Detection***
* Our File type detection allows to analyze a variety of filetypes by analyzing file structure.
![](https://github.com/Anish-M-code/File-Analysis-Tool/blob/master/DEMO/signal-2020-06-25-222329~2.png)

## ***Password Cracking***
* We use [John the ripper](https://en.m.wikipedia.org/wiki/John_the_Ripper) to do password cracking with ease. 
![](https://github.com/Anish-M-code/File-Analysis-Tool/blob/master/DEMO/signal-2020-06-25-222424.png)

## ***Upload Suspicious Files to Virustotal***
* We use  [virustotal](https://www.virustotal.com/gui/home/upload), via  [virustotal API](https://pypi.org/project/virustotal-python/) to check files if it is malicious or not.
![](https://github.com/Anish-M-code/File-Analysis-Tool/blob/master/DEMO/signal-2020-06-25-221317.png)

## ***Note***
* This software uses office2john module to deal with ms office documents. which has different 
[License](https://github.com/magnumripper/JohnTheRipper/blob/bleeding-jumbo/run/office2john.py).

## ***Contributors***
* [Anish](https://www.github.com/anish-m-code)
* [Gowtham](https://www.github.com/gowtham758550)
* [Raagul](https://www.github.com/raagul26)
* [Godwin](https://www.github.com/godwinujeen)
* [Godwin Joy](https://www.github.com/god-dark)
