# A program to help Beep and Bop cross the falling steps.

# Define a function to store step data

def steps():
    likelihoods = ("step 1", 50, "step 2", 38, "step 3", 27, "step 4", 99, "step 5", 4)
    return likelihoods





# function to determine if each step is bad or good and then add to lists.
# function will print total of step types
def run():
    loc_var = steps()
    good_steps = []
    bad_steps = []
    for index in range(1, (len(loc_var)), 2):
        if loc_var[index] >= 50:
            bad_steps.append(loc_var[index])
        else:
            good_steps.append(loc_var[index])
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")



if __name__ == "__main__":
    run()
