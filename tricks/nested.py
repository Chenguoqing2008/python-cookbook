#！/usr/bin/python

# dict nested in list
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)


# dict nested in dict	
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',	
	},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',	
	},
}

for username,user_info in users.items():
	print("\nusername: " + username)
	full_name = user_info['first']+" "+user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
