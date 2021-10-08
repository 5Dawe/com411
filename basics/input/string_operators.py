#Ask for number of lives
print("Please enter the number of lives.")
Lives = int(input(">"))

#Ask for energy level
print("Please enter the energy level.")
Energy = int(input(">"))

#Ask for shielf level
print("Please enter the shield level.")
Shield = int(input(">"))

#Print results
print("Health has been set")

#import time module for sleep
import time


#Declare counting variable
iterations = 1

#Print result of Lives
print("")
print("Lives:", end =" ")
while iterations <= Lives:
    print("♥", end ="")
    iterations = iterations + 1
    time.sleep(0.2)


#Print result of Energy
iterations = 1
print("")
print("Energy:", end =" ")
while iterations <= Energy:
    print("♦", end ="")
    iterations = iterations + 1
    time.sleep(0.2)

#Print result of Shield
iterations = 1
print("")
print("Shield:", end =" ")
while iterations <= Shield:
    print("♦", end ="")
    iterations = iterations + 1
    time.sleep(0.2)

#Lives:  ♥♥♥
#Energy: ♦♦♦♦♦♦♦♦♦♦
#Shield: ♦♦♦♦♦♦♦