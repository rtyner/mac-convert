# MAC Converter

#### Python script to convert a MAC to different formats

##### Types of MAC addresses that this program has been tested with:
* EUI48 - 71-54-ED-69-9B-E9
* Unix - 71:54:ed:69:9b:e9
* Cisco - 7154.ed69.9be9
* Bare - 7154ED699BE9

##### Ubuntu/Bash on Windows 10
* ````
  sudo apt install python3 python3-pip
  sudo pip3 install netaddr
  ````
* Clone the repo and give the script a file as the argument
  * `python3 mac_convert.py macs.txt`
