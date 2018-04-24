from travianapi import *
import re
import sys
import datetime
import random
import time

##############################CHANGE ONLY THIS VARS!!!!!!!!!!!!#########################
#				dev by Duarte Petiz
#					dpetiz
#
#
########################################################################################
########################################################################################
#USER EDITABLE VARS
user='dpetiz'
password='password'
server='ts20'
domain='pt'
mode='4'
#mode = '2' = reinforce
#mode = '3' = normal
#mode ='4' = farm

#END OF EDITABLE VARS
########################################################################################
########################################################################################
#FIXED VARS
villages=''
villageSelect=0
contador=0
trops=''
timer=random.randint(6,12)
#END OF FIXED VARS
########################################################################################
########################################################################################
#FILE FARM LIST READER
#the farm list text must be cord1,cord1,number_of_troops(first type of troops only)
file = open(sys.argv[1],"r")
farm = file.read();
file.close();
#END OF READER
########################################################################################

########################################################################################
#
#
#			DONT CHANGE ANYTHING MORE
#
#
########################################################################################

login = TravianGuerrillaApi(user, password, server, domain)
login.loggin(user, password)
villages=login.list_villages();
print('Available villages: ');
print(villages);
try:
    villageSelect=int(raw_input('select your farmer village ID: '))
except ValueError:
    print "ERROR: number ID!!!!!!!!!"
#print('selected village com ID: ');
#print(villageSelect);

#trops=login.get_actual_units_by_tier()
#print(trops)

#print('lets d3stroy my friend!!!')

#parse farm list
splitedFarm = farm.split(",")
while True:
	print('re-logging again')
	login = TravianGuerrillaApi(user, password, server, domain)
	login.loggin(user, password)
	login.set_village(villageSelect);
	timer=random.randint(7,12)
	timer=timer*60;
	tamanho = len(splitedFarm)
	contador = 0
	while (tamanho>0):
		number=0;
		cords=[];
		tamanho=tamanho-3
		cords.append(splitedFarm[contador]);
		cords.append(splitedFarm[contador+1]);
		number=splitedFarm[contador+2];
		contador=contador+3;
		login.send_attack(cords, mode, number, t2=0, t3=0, t4=0, t5=0, t6=0, t7=0, t8=0, t9=0, t10=0);
	print datetime.datetime.now()
	print('sleeping (minutes)')
	print(timer/60)
	time.sleep(timer)

