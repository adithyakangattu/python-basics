#nested if









age = 24
cmpltd_driver_edu = "yes"
if 16 <= age <=100:
    if age >=18:
      print("eligible for driving license.")
    else:
      if cmpltd_driver_edu== "yes":
        print("eligible for driving license.")
      else:
        print("not eligible for driving license. must complete driver's education")
else:
    print("invalid age.")

