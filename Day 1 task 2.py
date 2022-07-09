square_feet = int(input('SQUARE FEET OF WALL SPACE:  '))
print('')
paint= int(input('PAINT PER GALLON: '))
a = square_feet
b = paint
paint_required= int(a//115)
print('Paint required in gallons', paint_required)
print('')
hours_required= int(a/115)*8
print('Hours of labour required', hours_required)
print('')
cost_paint = int(b * paint_required)
print('Cost of paint in $', cost_paint)
print('')
labor_charge = hours_required * 20
print('Labor charges', labor_charge)
print('')
total_cost= cost_paint + labor_charge 
print('TOTAL COST IN $',  total_cost)