hour = int(input())
day = input()

if 0 <= hour <= 23:
    if day == "Monday" and 10 <= hour <= 18:
        print("open")
    elif day == "Tuesday" and 10 <= hour <= 18:
        print("open")
    elif day == "Wednesday" and 10 <= hour <= 18:
        print("open")
    elif day == "Thursday" and 10 <= hour <= 18:
        print("open")
    elif day == "Friday" and 10 <= hour <= 18:
        print("open")
    elif day == "Saturday" and 10 <= hour <= 18:
        print("open")
    else:
        print("closed")



 #   elif day == "Tuesday":
  #      print("open")
   # elif day == "Wednesday":
    #    print("open")
    #elif day == "Thursday":
       # print("open")
#    elif day == "Friday":
      #print("open")
 # elif day == "Saturday":
  #      print("open")
    #else:
     #   print("closed")