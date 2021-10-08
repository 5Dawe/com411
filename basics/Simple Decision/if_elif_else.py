#Instructions for painting
print("Towards which direction should I paint (up, down, left, right)?")
paintdirection = str(input(">").lower())
if paintdirection  == "up":
    print("I am painting in the upwards direction!")
elif paintdirection  == "down":
    print("I am painting in the downwards direction!")
elif paintdirection  == "left":
    print("I am painting in the left direction!")
elif paintdirection  == "right":
    print("I am painting in the right direction!")
else:
    print("I don't know that direction")


