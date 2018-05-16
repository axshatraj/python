#!/usr/bin/python2
import time
import webbrowser
option='''
Press 1: To Enter any thing - split each word and search on google
Press 2: To search images on google
Press 3:To Search url of every website on google 
Press 4:Current date & time
Press 5:open default web browser
Press 6:All n/w ip
Press 7:Enter Domain and check owner email and contact
'''
print option 
ch=raw_input()

#webbrowser.open("my name is akshat")
if ch == '1' :
	search_data=raw_input("Enter data:")
	final_data=search_data.strip()
	#above removing leading and trailing space
	done_data=final_data.split()
	#spliting each word by space	
	for i in done_data:
		 webbrowser.open_new_tab('https://www.google.com/search?q='+i)

elif ch == '2' :
	search_data=raw_input("Enter data:")
	final_data=search_data.strip()
	done_data=final_data.split()
	for i in done_data:
		 webbrowser.open_new_tab('https://www.google.com/search?q='+i)


