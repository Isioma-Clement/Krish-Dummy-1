val = int(input("Enter values 0 to start and 1 to exit: "))

if val == 0:
    try:
        val_1  = val
    except:
        print("Error occured. Please try again witha different input")
elif val == 1:
    raise SystemExit("Closing the application.")
