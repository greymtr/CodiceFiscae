def cleanser(nonclean):
#ASSUMING nonclean is a lowercase word


	#If all characters are alphabets then GO 
	if (nonclean.isalpha()):
		clean=nonclean
	#If any character are numbers then STOP
	elif (nonclean.isalnum()):
		printf("ERROR : Numbers aren't allowed in a name.")
		quit()
	#If any characters are not alphabets or they are not numbers then 
	#Basically if any character is special
	else :
		for i in nonclean:
			if ( ( ( 'a' < i < 'z' ) or ( i == "'" ) or ( i == "-" ) ) == False ):
				print("ERROR : Invalid characters [ valid characters : ( \"A-Z\" , \"a-z\" , \"0-9\" , \"-\", \"'\)]")
				quit()
			
		if (nonclean.replace("-","").replace("'","").isalpha()):
			clean=nonclean	
		else:
			print("ERROR : Must contain alphabets.")
			
		
		

a=input()
cleanser(a)
