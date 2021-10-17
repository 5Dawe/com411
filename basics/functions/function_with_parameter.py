# A program that will help Beep and Bop find a way to escape.
def escape_by(plan):
    if plan == "jumping over":
        print(f"We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print(f"We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print(f"That might just work! Let's go deeper!")
    else:
        print(f"We cannot escape that way! The boulder is in the way")

escape_by("ducking")
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")


