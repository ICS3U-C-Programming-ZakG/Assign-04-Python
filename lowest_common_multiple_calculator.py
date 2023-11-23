#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 23, 2023
# This program calculates the lowest common multiple of two numbers.


def main():
    # introduce program to the user
    print(
        "Hello, this program takes two positive integers and will find the lowest common multiple and display the result."
    )

    # get user input for two numbers
    user_num_one_str = input("Enter a positive integer: ")
    user_num_two_str = input("Enter a positive integer: ")

    # try converting first input to an integer
    try:
        user_num_one_int = int(user_num_one_str)

        # try converting second input into an integer
        try:
            user_num_two_int = int(user_num_two_str)

            # check if any inputs are negative
            if (user_num_one_int > 0) and (user_num_two_int > 0):
                # check if users first input is bigger than second
                if user_num_one_int > user_num_two_int:
                    # if first input is bigger, variable higher gets the first inputs value
                    higher = user_num_one_int

                    # else variable higher gets the second inputs value
                else:
                    higher = user_num_two_int

                # initialize the variable value with the value of the bigger input
                value = higher

                # do while loop
                while True:
                    # check if the bigger input mod the inputs both equal zero (To find lowest common multiple)
                    if (higher % user_num_one_int == 0) and (
                        higher % user_num_two_int == 0
                    ):
                        # if true then tell user the lowest common multiple
                        print(
                            "The LCM of {} and {} is {}.".format(
                                user_num_one_int, user_num_two_int, higher
                            )
                        )

                        # break out of the loop
                        break

                    # else if the bigger number mod the inputs don't both equal zero
                    else:
                        # higher variable gets the value of higher plus the initial value
                        higher = higher + value

            else:
                print("You must input two positive integers")

        # catch invalid data and tell user
        except Exception:
            print("{} is not a positive integer".format(user_num_two_str))

    # catch invalid data and tell user
    except Exception:
        print("{} is not a positive integer".format(user_num_one_str))


if __name__ == "__main__":
    main()
