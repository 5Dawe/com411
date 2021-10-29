# A program to help Beep and Bop decide which steps to take.

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    least_likely = min(likelihoods)
    return least_likely


def run():
    likelihood()
    print(f"Minimum likelihood of falling: {likelihood()}")


if __name__ == "__main__":
    run()
