import os
import time

#1. The files and directories to be backed up are specified in a list.
source = ['/home/fritzrage/Learning/Codeforces', '/home/fritzrage/Learning/Python']

#2. The directory where the backup is to be taken
target_dir = '/home/fritzrage/Learning/Backup'

#3. The files are backed up into a zip file.
#4. The current day is the name of the subdirectory in the main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')

# The current time is used as the name of the file to be backed up and saved inside the subdirectory.
now = time.strftime('%H%M%S')

#Get comment from user to append to filename
comment = input('Enter a comment:')
if len(comment) == 0: #check if coment was entered
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

#Create subdirectory if it already doesnt exist
if not os.path.exists(today):
	os.mkdir(today)
	print ('Successfully created directory', today)

#5. Finally use the zip command to put the files in a zip archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

#Run the backup
if os.system(zip_command) == 0:
	print ('Successful backup to', target)
else:
	print ('Backup Failed')




