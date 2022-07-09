from datetime import datetime

now = datetime.now()

password='12345'

open = 'open'
close = 'close'

pswd = input('Enter password to open the door: ')

while (pswd != password):
  paswd=input("Wrong password please try again: ")

flag_open_door = False
flag_close_door = True

open_time = now.strftime("%Y/%m/%d, %H:%M:%S")
close_time = now.strftime("%Y/%m/%d, %H:%M:%S")

while (True):
  x = input("Enter command: ")
  if x == 'open' and flag_close_door== True :
    print("The door is now open")
    print("The door was last opened at",open_time)
    flag_open_door = True
    flag_close_door = False
    now = datetime.now()
    open_time = now.strftime("%Y/%m/%d, %H:%M:%S")
  elif x == 'open' and flag_close_door== False:
    print("The door is already open")
  elif x == 'close' and flag_open_door== True:
    print("The door is now closed")
    print("The door was last closed at",close_time)
    now = datetime.now()
    close_time = now.strftime("%Y/%m/%d, %H:%M:%S")
    flag_open_door = False
    flag_close_door = True
  elif x == 'close' and flag_open_door== False:
    print("The door is already close")
  elif x == 'quit':
    break
  else:
    print("Invalid input, please try again")
    