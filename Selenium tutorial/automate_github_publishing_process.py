# automate_github_publishing_process.py

# check if selenium exists if not then install it
try:
	from selenium import webdriver
except:
	import subprocess, sys
	print("This process happens only once if selenium is not found\nInstalling selenium")
	subprocess.call([sys.executable, "-m", "pip", "--disable-pip-version-chec", "-q", "install", "selenium"])
	print("selenium installed succesfully")

# imports from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
print("\\")
try:
	f = open("driverloc.txt",'r')
	loc = f.read()
	f.close()
	try:
		driver = webdriver.Chrome(loc)
		driver.quit()
	except:
		print(1/0)
except:
	lop = input("Do you have driver? [yes]/no:")
	if lop.lower() != "no":
		while True:
			loc = input("Enter location to driver(ex: C:\\Program Files\\chromedriver.exe):")
			try:
				driver = webdriver.Chrome(loc.replace("\\",'\\\\'))
				driver.quit()
				with open("driverloc.txt",'w') as f:
					f.write(loc)
				break
			except Exception as e:
				print(e)
	else:
		# check if selenium exists if not then install it
		try:
			import webbrowser
		except:
			import subprocess, sys
			print("This process happens only once if selenium is not found\nInstalling selenium")
			subprocess.call([sys.executable, "-m", "pip", "--disable-pip-version-chec", "-q", "install", "webbrowser"])
			print("selenium installed succesfully")
		import webbrowser
		print("Download zip and extract it to a convenient folder.\nYou will be reloaded to download page.")
		import time
		time.sleep(5)
		webbrowser.open("https://sites.google.com/a/chromium.org/chromedriver/downloads")
		while True:
			loc = input("Enter location to driver(ex: C:\\Program Files\\chromedriver.exe):")
			try:
				driver = webdriver.Chrome(loc.replace("\\",'\\\\'))
				driver.quit()
				with open("driverloc.txt",'w') as f:
					f.write(loc)
				break
			except Exception as e:
				print(e)
try:
	with open("Credentials.txt", 'r') as f:
		a, b = f.read().split('\n')

except:
	#take credentials
	a = input("Enter GitHub Username:")
	b = input("Enter GitHub Password:")
	with open("Credentials.txt", 'w') as f:
		f.write(f'{a}\n{b}')

cred = (a, b)

# path to chrome web driver
with open("driverloc.txt",'r') as f:
	PATH = f.read()

# initate web driver
driver = webdriver.Chrome(PATH)

# main code
def main(driver, cred, stats):

	# take repository name
	Rep = input("Enter Repository Name:")

	if not stats:
		# open login page of github
		driver.get("https://github.com/login/")

		# get input fields
		user_search = driver.find_element_by_id("login_field")
		pass_search = driver.find_element_by_id("password")

		# login with credentials
		user_search.send_keys(f"{cred[0]}")
		pass_search.send_keys(f"{cred[1]}")
		user_search.send_keys(Keys.RETURN)

		# Repeatedly ask username and password 
		while driver.title != 'GitHub':
			print("Incorrect Credentials")

			#take credentials
			a = input("Enter GitHub Username:")
			b = input("Enter GitHub Password:")
			with open("Credentials.txt", 'w') as f:
				f.write(f'{a}\n{b}')
			cred = (a, b)
			# open login page of github
			driver.get("https://github.com/login/")

			# get input fields
			user_search = driver.find_element_by_id("login_field")
			pass_search = driver.find_element_by_id("password")

			# login with credentials
			user_search.send_keys(f"{cred[0]}")
			pass_search.send_keys(f"{cred[1]}")
			user_search.send_keys(Keys.RETURN)

	# goto settings site of that repository
	driver.get(f"https://github.com/{cred[0]}/{Rep}/settings")

	# loop till site will be published
	while True:

		# make a variable for taking text from body tag of the site
		status = driver.find_element_by_tag_name("body")

		# if site is published then end the loop
		if "Your site is published at" in status.text:
			print("Site Published")
			break

		# if site is not published yet then reload page
		elif "Your site is ready to be published at" in status.text:
			print("Publishing Site")
			driver.get(f"https://github.com/{cred[0]}/{Rep}/settings")

		# if page not found then ask User to enter repository name again
		elif "Find code, projects, and people on GitHub:" in status.text:
			print("Invalid Repository Name")
			# Retake repository name
			Rep = input("Enter Repository Name:")
			driver.get(f"https://github.com/{cred[0]}/{Rep}/settings")

	# ask user if he/she want to use program again or not
	don = input("Want To Use This Program Again ([Yes]/No):")
	if don.lower() == "no":
		driver.quit()
		print("Thank you for using this Program")
	else:
		print("Reloading")
		# restart main function with status saying that user logged in
		main(driver, cred, True)

if __name__ == '__main__':
	# start main function with status saying that user not logged in
	main(driver, cred, False)
