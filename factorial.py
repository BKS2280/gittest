def factorial( number ):
    if number <= 2:
       return number
    else:
       return number * factorial( number-1 )


if __name__ == "__main__":
    print("The factorial of 10 is: ", factorial( 10 ))

