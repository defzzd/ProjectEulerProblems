'''

#### Project Euler Problem 2 ####

"Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."


'''


def generate_fibonacci_numbers_up_to_this_number(the_limit_number):

    ## The inits for this function:
    number_alpha = 1
    number_beta = 2
     
    steps_taken = 2 # 1 and 2 are the first steps and first Fibonacci numbers, by definition
    
    
    while ( (number_alpha + number_beta) < int(the_limit_number) ): # checks a+b because otherwise it would iterate over the target before realizing it needs to stop

    
        print("\n\nPreprocessing alpha: %r\n Preprocessing beta: %r" %  (number_alpha, number_beta))
    
        print("    ... processing ...")
        
        number_alpha, number_beta = number_beta, (number_alpha + number_beta)
        
        steps_taken += 1

        print("  New number alpha: %r\n  New number beta: %r" % (number_alpha, number_beta))
        
        yield number_beta

 
    
    
inputted_limit = input("Please enter a number to run to: ")    
    
    

running_sum = 2 # init to 2, due to definitions above

## Now take the generator's output and modulo check it for evenness, then throw it on the pile if even:
for each_fibonacci_number in generate_fibonacci_numbers_up_to_this_number(inputted_limit):
    
    if each_fibonacci_number % 2 == 0:
        
        running_sum += each_fibonacci_number

        
        print("\n\n        each_fibonacci_number == %r\n\n        running_sum == %r" % (each_fibonacci_number, running_sum))



## Print the result.
print("The result:\n    %r" % (running_sum))


kek = input("\n\n\nPress enter to end program . . .\n> ")