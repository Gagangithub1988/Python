h_ft = int(input("enter the height feet: "))
h_inch = int(input("enter the height inch: "))
h_inch+=h_ft*12
h_cm= round(h_inch*2.54)
print("The height is in cm : %d cm"%h_cm)