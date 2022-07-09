customer_purchase= int(input("NUMBER OF BOOKS PURCHASED: "))
print("books purchased this month", customer_purchase)
if customer_purchase <0:
  print('PLEASE ENTER A VALID NUMBER')
else:
  print('You have Earned Book Club Points')
if customer_purchase ==0:
  print('EARNED = 0 POINTS')
elif customer_purchase ==1:
  print('EARNED = 6 POINTS')
elif customer_purchase ==2:
  print('EARNED = 16 POINTS')
elif customer_purchase ==3:
  print('EARNED = 32 POINTS')
elif customer_purchase >=4:
  print('EARNED = 60 POINTS')
print('')