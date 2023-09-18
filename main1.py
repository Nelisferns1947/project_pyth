import os
import webbrowser as wp
import time
import subprocess

def Docker():
	while True:
		os.system("clear")
		os.system("tput setaf 6")
		print("\t\tMenu Program in Python:-")
		print("\t1. Docker Start")
		print("\t2. Docker Run")
		print("\t3. Run Python code on Docker")
		print("\t4. Run Web Server on Docker")
		print("\t5. Remove Docker image")
		print("\t6. See all images")
		print("\t7. Show all running container ")
		print("\t8. Show all container")
		print("\t9. Docker Stop")
		print("\t0. Exit")
		os.system("tput setaf 3")
		choice=int(input("Enter your choice: "))
		if choice==1:
			os.system("systemctl start docker")
			os.system("tput setaf 4")
			print("Docker Started")
		elif choice==2:
			print("Available docker images")
			print("1. centos:latest")
			print("2. centos:7 ")
			print("3. ubuntu")
			img=input("Enter the image name: ")
			name=input("Enter the container name: ")
			os.system("docker run -dit --name {} {}".format(name,img))
			os.system("tput setaf 4")
			print("Container successfully launched")
		elif choice==3:
			print("List of Available containers:- ")
			os.system("docker ps -a")
			name=input("Enter the name of container on which you wish to setup Python Interpreter: ")
			os.system("docker start {}".format(name))
			os.system("docker exec {} yum install python3 -y".format(name))
			os.system("docker exec {} python3".format(name))
			os.system("tput setaf 4")
			print("Python Interpreter Successfully setup on {} container".format(name))
		elif choice==4:
			print("List of Available containers:- ")
			os.system("docker ps -a")
			name=input("Enter the name of container on which you wish to configure web server:- ")
			os.system("docker start {}".format(name))
			os.system("docker exec {}  yum install httpd -y".format(name))
			os.system("docker exec {}  /usr/sbin/httpd ".format(name))
			os.system("tput setaf 4")
			print("Web server successfully configured on {} container".format(name))
		elif choice==5:
			os.system("docker ps -a")
			name=input("Enter the name of the container to remove: ")
			os.system("docker stop {}".format(name))	
			os.system("docker rm  {}".format(name))
			os.system("tput setaf 4")
			print("Container {} successfully removed".format(name))
		elif choice==6:
			os.system("tput setaf 4")
			print("The docker images in this system are:-")
			os.system("docker images ")
		elif choice==7:
			os.system("tput setaf 4")
			print("The currently running containers on this system are:-")
			os.system("docker ps")
		elif choice==8:
			os.system("tput setaf 4")
			print("These are containers present on this system:- ")
			os.system("docker ps -a")
		elif choice==9:
			os.system("systemctl stop docker")
			os.system("tput setaf 4")
			print("Docker Stopped")
		elif choice==0:
			print("Thank You")
			break
		else:
			print("Invalid Choice! Try Again")
		os.system("sleep 5")	

def Linux():
	def avaldisk():
		os.system('tput setaf 6')
		os.system('fdisk -l | less')
		os.system('tput setaf 7')

	def avalpv():
		os.system('tput setaf 6')
		os.system('pvdisplay | less')
		os.system('tput setaf 7')

	def avalvg():
		os.system('tput setaf 6')
		os.system('vgdisplay | less')
		os.system('tput setaf 7')
	def avallv():
		os.system('tput setaf 6')
		os.system('lvdisplay | less')
		os.system('tput setaf 7')

	def pv():
		os.system('clear')
		os.system('tput setaf 1')
		print()
		print("PHYSICAL VOLUME CREATION ")
		print("--------------------------")
		print()
		os.system('tput setaf 3')
		name=input("Enter Hard Disk Name : ")
		x=sp.getstatusoutput('pvcreate {}'.format(name))
		if x[0]== 0 :
		  print('\t\t\t\t\tPHYSICAL VOLUME CREATED')
		  y=sp.getstatus('pvdispaly {}'.format(name))
		  print(y[1])
		else:
		  print("PROCESS FAIL")
		os.system('tput setaf 4')
		z=input("press enter to continue")
		os.system('tput setaf 7')
		





	def vg():
		os.system('clear')
		os.system('')
		print()
		print("VOLUME GROUP CREATION")
		print("\t\t\t----------------")
		print()
		os.system('tput setaf 3')
		name1=input("Enter Group Volume Name : ")
		name2=input("Enter 1 st volume :")
		name3=input("Enter 2nd volume : ")
		x=sp.getstatusoutput('vgcreate {0} {1} {2}'.format(name,name1,name2))
		if x[0]== 0 :
		  print('\t\t\t\t\t VOLUME GROUP CREATED')
		  y=sp.getstatus('vgdispaly {}'.format(name))
		  print(y[1])
		else:
		  print("PROCESS FAIL")		
		os.system('tput setaf 4')
		print(ch)
	def menu():
		while True:
			os.system('clear')
			os.system('tput setaf 1')
			print("                            LVM AUTOMATION WITH PYTHON ")
			print("                            ===========================")
			print()
			os.system('tput setaf 2')
			print("        1.Display All Attached Hard Disk")
			print("        2.Display All Phsical volume")
			print("        3.Display All Volume Group")
			print("        4.Display All Logical Volumes")
			print("        5.Create Physical Volume")
			print("        6.create Volume Group")
			print("        7.create Logical Volume")
			print("        8.Exit")
			print()
			os.system('tput setaf 3')

			ch=input("Enter ur choice : ")
			os.system('tput setaf 6')
			print()
			if int(ch)== 1:
				avaldisk()
				
			elif int(ch)== 2:
				avalpv()
			elif int(ch)== 3:
				avalvg()
			elif int(ch)== 4:
				avallv()
			elif int(ch)== 5:
				pv()
			elif int(ch)== 6:
				vg()
			elif int(ch)== 7:
				lv()
			
			elif int(ch)== 8:
				exit()
			else:
				os.system('tput setaf 7')
				print("wrong command")


	menu()
	

os.system("tput setaf 3")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSVAGATA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

os.system('espeak-ng "Python-based mynu program programmed to perform Docker, Linux" -s 140')

Technology = ["Docker","Linux","Exit"]
os.system("tput setaf 4")
for j in range(0,3):
	print("\t\t\t\t",j+1,". ",Technology[j])
	if j==0:
		os.system("espeak-ng 'press 1 For Docker' -s 150")
	elif j==1:
		os.system("espeak-ng 'press 2 for Linux' -s 150")
	else:
		os.system("espeak-ng 'press 3 to exit'")

while True:
	os.system("tput setaf 6")
	os.system("espeak-ng 'Enter Your Technology' -s 150")
	select_tech=int(input("Enter Your Technology : "))
	if select_tech == 1:
		Docker()
	elif select_tech == 2:
		Linux()
	else:
		break
	