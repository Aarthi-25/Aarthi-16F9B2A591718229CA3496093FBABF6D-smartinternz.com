def isLeapYear(Year):
 if(Year%4==0 and Year%100!=0) or Year%400==0:
    return True
 else:
    return False
Year =int(input("Enter the Year:"))
if isLeapYear(Year):
   print ('{} is a  LeapYear.'.format(year))
else:
    print('{} is not a LeapYear.'.format(year))

