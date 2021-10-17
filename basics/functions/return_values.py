# Bop is trying to distribute their weight so that both Beep and Bop
# can reach the top of the bridge ladder quicker. A program to help
# Bop achieve this consists of three functions

def sum_weights(beep_w, bop_w):
    w_sum = beep_w + bop_w
    return w_sum

def calc_avg_weights(beep_w, bop_w):
    w_avg = (beep_w + bop_w)/2
    return w_avg

def run():
    print(f"\nwhat is the weight of Beep")
    ibeep_w = int(input())
    print(f"\nwhat is the weight of Bop")
    ibop_w = int(input())
    print(f"\nWould you like to calculate sum or average?")
    user_q = str(input())
    if user_q == "sum":
        print(f"The sum of the robots is ", end="")
        print(sum_weights(ibeep_w, ibop_w))
    elif user_q == "average":
        print(f"The average of the robots is ", end="")
        print(calc_avg_weights(ibeep_w, ibop_w))
    else:
        print(f"Please enter a valid choice.")

# Run the program
run()
