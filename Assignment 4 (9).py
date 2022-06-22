# Part 1

# For each of the non-recursive functions given here, create
# a recursive function that produces the same result

# Example

def product(x, y):   
   ''' compute the product of x and y, where y is a positive integer '''
   product = 0
   while y >= 1:
      if (y % 2 == 1):
         product += x
      x *= 2
      y //= 2
   return product
   
# ... can be replaced by this recursive function

def product_rec(x,y):
   ''' compute the product of x and y, where y is a positive integer'''
   if y == 0:
      return 0
   else:
      if (y % 2 == 1):
         return x + product_rec(x*2, y // 2)
      else:
         return product_rec(x*2, y // 2)
 

         
# PROBLEM 1 ::::::

# This version of the function doesn't work!!!!!  
# I'm leaving it here in case you want to try to figure what is wrong with it
#~ def exponent(x, y): # y is a positive integer
   #~ ''' compute x^y, where y is a positive integer '''
   #~ result = x
   #~ while y > 1:
      #~ result = result*result
      #~ if (y % 2 == 1):
         #~ result *= x
      #~ y = y // 2
   #~ return result   
   
def correct_exponent(x, y):
   ''' compute x^y, where y is a positive integer '''
   result = 1
   while y >= 1:
      if y % 2 == 1:
         result *= x
      x = x*x
      y = y // 2
   return result   

# example of use
print("\nProblem 1\n")
print(correct_exponent(5, 19), 5**19)              
# printing 5**19 for confirmation that the revised function is correct!
   
def exponent_rec(x, y): # sol to p1  -----------------------------
   if y == 0:
      return 1
   elif y == 1:
      return x
   else:
      return (x * exponent_rec(x, y - 1))

print(exponent_rec(5,19))


# Problem 2:

def sublist_sum(a_list, target):
   ''' determine if list a_list has a consecutive sub-list that sums to target '''
   for start in range(len(a_list)):
      sum = 0
      for finish in range(start, len(a_list)):
         sum += a_list[finish]
         if sum == target:
            return True
   return False

# example of use
print("\nProblem 2\n")
print(sublist_sum([4, 9, 3, 1, 7, 2, 4], 13))
# the result is True because of the consecutive sublist [9, 3, 1]

def sublist_sum_rec(a_list, target): # sol for p2 ------- not sure about this one. I think its wrong.
      sum = 0  # set sum to zero
      for start in range(len(a_list)): # we iterate over the list and add the elements to the sum variable
          sum += a_list[start]
          if sum == target: # check if the sum is equal to the target, and if it is we return True
             return True
          sublist_sum_rec(a_list[1:len(a_list)], target) # call the same function again but exlude the first element with slicing

print(sublist_sum_rec([4, 9, 3, 1, 7, 2, 4], 13)) # Result is true




# Problem 3:

def prime_factors(n):
   ''' print the prime factorization of n'''
   while n > 1:
      candidate = 2
      while candidate <= n:
         if n % candidate == 0:
            print(candidate, " ", end="")    # this prints without starting a new line - very useful!
            n = n // candidate
         else:
            candidate += 1
   print("\n")
   
# example of use
print("\nProblem 3\n")
prime_factors(126)

def prime_factors_rec(n): # sol for p3 -----------------------------------
      factors = []
      if n > 1:
         i = 2
         while n % i != 0:
            i += 1
         factors.append(i)
         factors.extend(prime_factors_rec(n / i))
      return factors

print(prime_factors_rec(126))


# Problem 4:

def reverse(a_string):
   ''' return a string that is the reverse of a_string '''
   new_string = ""
   for i in range(len(a_string)):
      new_string = a_string[i] + new_string
   return new_string


      
# example of use   
print("\nProblem 4\n")
print(reverse("radar"))      
print(reverse("Oh I guess radar wasn't a good choice"))

def reverse_rec(a_string): # sol for p4 ----------------------
      if a_string == "":
         return a_string
      else:
         return reverse_rec(a_string[1:]) + a_string[0]

print(reverse_rec("radar"))
print(reverse_rec("Oh I guess radar wasn't a good choice"))



# Part 2:

# Each of these recursive functions is inefficient due to duplicated
# effort.  Improve them by storing the solutions to smaller problems that
# are needed repeatedly.

# Example:

def fibonacci(n):
   '''compute the n-th number in the Fibonacci sequence'''
   if n <= 2:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

# This is extremely inefficient because computing fibonacci(n-1)
# requires computing fibonacci(n-2), which we then compute again.  And 
# each time we compute fibonacci(n-2), we compute both
# fibonacci(n-3) and fibonacci(n-4), etc.  

# A much better solution is to create a list or dictionary
# containing the fibonacci numbers we have already computed
# so we can just look them up instead of recompute them.

# To keep the interface as simple as possible, we hide the recursive
# function - which now needs an extra parameter - behind a so-called
# 'helper function' which sets things up and initiates the recursion

def better_fibonacci(n):
   '''compute the n-th number in the Fibonacci sequence'''
   fibonacci_nums = [0, 1,1]  # the 0 is just a place-holder - I wanted to get the first Fibonacci number in position 1, etc.
   # to make the indexing easier to follow
   return better_fibonacci_rec(n, fibonacci_nums)

def better_fibonacci_rec(n, fibonacci_nums):
   if n <= 2:
      return fibonacci_nums[n]
   elif len(fibonacci_nums) > n:
      return fibonacci_nums[n]  # previously computed value
   else:
      fibonacci_nums.append(better_fibonacci_rec(n - 1, fibonacci_nums) + better_fibonacci_rec(n - 2, fibonacci_nums))
      return fibonacci_nums[n]  # newly computed value


# Example of use:
print("\nFibonacci Example\n")
print(better_fibonacci(8))
      
    
# Problem 5

# The Collatz sequence for an integer n > 0 is defined as follows:
#      
#      while n > 1:
#          add n to the sequence
#          if n is even:
#               n = n // 2
#          else:
#               n = 3*n + 1
#      add 1 to the end of the sequence

#  For example, the Collatz sequence for n = 10 is 10, 5, 16, 8, 4, 2, 1  (length = 7)  and the
#  Collatz sequence for n = 11 is 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 (length = 15)

#  The Collatz Conjecture proposes that every Collatz sequence terminates.
#  Nobody has proved that the conjecture is true, but nobody has ever found
#  a counterexample.  

#  This problem deals with counting the length of the Collatz sequences for all integers up to
#  a given value.


def collatz_length_up_to_n(n):
   ''' print the length of the Collatz Sequence for each value from 1 to n '''
   for i in range(n):
      print(i+1,":",collatz_length_rec(i+1))

def collatz_length_rec(n):
   ''' print the length of the Collatz Sequence for integer n '''
   if n == 1:
      return 1
   else:
      if n % 2 == 0:
         n = n // 2
      else:
         n = 3*n + 1
      return 1 + collatz_length_rec(n)

# Example of use:
print("\nProblem 5\n")
collatz_length_up_to_n(10)

# begin sol 5
def better_collatz_up_to_n(n):  # I think it is better to create a list or dictionary here, but yolo
      if n == 0:
         return 0
      count = 1
      while n != 1:
         n = (n / 2) if n % 2 == 0 else (3 * n + 1)
         count += 1
      return count
print(better_collatz_up_to_n(10))




# Problem 6

def count_routes(n):
   ''' returns the number of different ways a robot can move forward a total of n metres, when the
       robot can only take steps that go forward either 2 metres or 3 metres. '''
   if n <= 1:
      return 0
   elif n <= 3:
      return 1
   else:
      return count_routes(n-2) + count_routes(n-3)
      
# Example of use:
print("\nProblem 6\n")
print(count_routes(7))

x = {1:0, 2:1, 3:1} # we define x with the description given above

def better_count_routes(n): # sol for p6 ------ not sure about this
   global x
   if n in x:
      return x[n]
   else:
      result = better_count_routes(n-2) + better_count_routes(n-3)
      x[n] = result
      return result

print(better_count_routes(7))




# Part 3

# Write non-recursive functions to produce the same results as these recursive functions

# Example: look back at the example at the very top of this assignment ... but imagine I've
# given you the recursive "product" function and asked you to write the non-recursive version.

# Problem 7

def binary_search(a_list, target):
   ''' returns the location of target in a_list if target is in a_list, returns -1 if target is not in a_list
       a_list must be sorted prior to calling this function
   '''
   return binary_search_rec(a_list, target, 0, len(a_list) - 1)


def binary_search_rec(a_list, target, first, last):
   if first > last:
      return -1
   else:
      mid = (first + last) // 2
      if a_list[mid] == target:
         return mid
      elif a_list[mid] > target:
         return binary_search_rec(a_list, target, first, mid - 1)
      else:
         return binary_search_rec(a_list, target, mid + 1, last)


# Example of use
print("\nProblem 7\n")
print(binary_search([4, 7, 12, 15, 23, 28, 33, 34, 35, 100, 5280, 5281], 100))

# sol to problem begins here ---

a_list = [ 4, 7, 12, 15, 23, 28, 33, 34, 35, 100, 5280, 5281 ] # sorted prior to calling func

def binary_search(a_list, elem): # sol for p7 -----------
   low = 0
   high = len(a_list) - 1
   mid = 0
   while low <= high: # we will search variable from low to mid index
      mid = (high + low) // 2
      if a_list[mid] < elem:
         low = mid + 1
      elif a_list[mid] > elem: # else we will search from high to mid indexx
         high = mid - 1
      else:
         return mid
   return -1

target = 100

result = binary_search(a_list, target)

if result != -1:
   print("target was found at ", str(result))
else:
   print("target is not in list:", -1)




# Problem 8

def gcd(a,b):
   ''' returns the greatest common divisor of a and b, which must be positive integers '''
   if b == 0:
      return a
   else:
      return gcd(b, a % b)
      
# Example of use
print("\nProblem 8\n")
print(gcd(8,20))

def gcd_norec(a, b): #sol to 8 ------------
   while b:
      a, b = b, a % b
   print('GCD:' + str(a))

print(gcd_norec(8,20))
   



