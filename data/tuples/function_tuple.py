# A program to help Beep and Bop decide which steps to take.

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    least_likely = min(likelihoods)
    most_likely = max(likelihoods)
    return (least_likely, most_likely)


def run():
    #likelihood()
    #print(f"Minimum likelihood of falling: {likelihood()}")
    tup_ret = likelihood()
    print(f"Minimum likelihood of falling: {tup_ret[0]}%")
    print(f"Maximum likelihood of falling: {tup_ret[1]}%")


if __name__ == "__main__":
    run()
