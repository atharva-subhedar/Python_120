#Permanent delete
import os
for filename in os.listdir():
 if filename.endswith('.rxt'):
 os.unlink(filename)

#Safe delete
import send2trash
baconFile = open('alice.txt', 'a') 
baconFile.write('alice is not a vegetable.)
