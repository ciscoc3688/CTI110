#Distance Traveled


#firstname = input ("Hello What is your name? ")
#input ("Hello " + firstname + " " + "How are you today? ")
#input ("Where are you from " + firstname+"? ")
#print ("Cool Beans!")

def DT():
    print("")
    speed = int(input("How fast will you be going? "))
    if (speed > 75):
        print ("Simmer down Lightning Mcqueen! Lets get you there alive.")
        DT()
    if (speed < 20):
        print("ZZZZZ, No really how fast?")
        DT()
    else:
        hours = int(input("Hours on the Road? "))
    distance = speed*hours
    print("In " + str(hours) + " hrs, at " + str(speed) + " mph, " + "you will have traveled:",str(distance),"miles")
    print("")
    restart = input ("Do you wish to start again? (y)(n) ")
    n = exit

    DT()
    
