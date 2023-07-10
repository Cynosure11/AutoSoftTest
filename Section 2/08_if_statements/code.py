from datetime import datetime
print(datetime.now())

"""
Information.
The order of keywords is important. Remember
that the IF comes first, then any ELIF, if you want them,
and finally the ELSE. The ELIF  and ELSE  keywords 
are optional if you want to add those branches to 
your IF statement.
"""

day_of_week = input("What day of the week is it day? ").lower()

if day_of_week == "monday":
    print("have a great start to your week!")
elif day_of_week == "Tuesday":
    print("It's Tuesday")
else:
    print("Full speed ahead")

print("This always runs")





