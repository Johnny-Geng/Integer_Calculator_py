# Johnny Geng, johnnyge@usc.edu

# Description:
# This program helps to find and calculate the largest, smallest, and average number of a set of integers.

def main():

    large_num = 0
    small_num = float('inf')
    count = 0
    sum = 0
    question = True
    print("Input an integer greater than or equal to 0 or -1 to quit:")

    while question == True:
        num = int(input(">"))
        if num != -1:
            if num < small_num:
                small_num = num
            if num > large_num:
                large_num = num
            count = count + 1
            sum = sum + num
        else:
            question = False
    # The following codes take into consideration of a special situation:
    # if you enter "-1" at the very first time, without the following code, it will return error.
    # Because in that case, count == 0, and the (sum / count) will not work since the denominator count is 0.
    if count == 0:
        print("You have entered 0 number")
        print("The largest number is undefined")
        print("The smallest number is undefined")
        print("The average number is undefined")
    else:
        print("The largest number is", str(large_num))
        print("The smallest number is", str(small_num))
        print("The average number is", str(sum / count))

    question2 = input("Would you like to enter another set of numbers? (y/n):")
    while question2.lower() == "y":
            large_num = 0
            small_num = float('inf')
            count = 0
            sum = 0
            print("Input an integer greater than or equal to 0 or -1 to quit:")
            extra = True
            while extra == True:
                num = int(input(">"))
                if num != -1:
                    if num < small_num:
                        small_num = num
                    if num > large_num:
                        large_num = num
                    count = count + 1
                    sum = sum + num
                else:
                    extra = False
            if count == 0:
                print("You have entered 0 number")
                print("The largest number is undefined")
                print("The smallest number is undefined")
                print("The average number is undefined")
            else:
                print("The largest number is", str(large_num))
                print("The smallest number is", str(small_num))
                print("The average number is", str(sum / count))
            question2 = input("Would you like to enter another set of numbers? (y/n):")
    print("Goodbye!")

main()