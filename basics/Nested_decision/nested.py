# Book classification program
# Ask user questions about book covers

print("What type of cover does the book have?")
book_cover = str(input(">").lower())
if book_cover == "soft":
    print("Is the soft cover perfect bound?")
    soft_book_cover = str(input(">").lower())
    if soft_book_cover == "yes":
        print(f"\nSoft cover, perfect bound books are very popular!")
    else:
        print(f"\nSoft covers with coils or stitches are great for short books!")
else:
    print(f"\nBooks with hard covers can be more expensive!")
