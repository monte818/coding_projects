# Question 1 printing username from input!
username = input("What is your username? \n")

def hello_name(user_name):
    """Display username greeting"""
    print("hello " + user_name + "!")

hello_name(username)

# Question 2 print first odds

def first_odds():
    for num in range(1, 101, 2):
        print(num)
print(first_odds())

# Question 3 max number list

def max_num_in_list(my_list):

    return max(my_list, default = None)

my_list = [2, 20, 3, 72, 13, 29]
print("\n", my_list)
result = max_num_in_list(my_list)
print("\nthe highest number in the list above is ", result, "\n")

# Question 4

def is_leap_year(a_year):
    if (a_year %4 == 0 and a_year % 100 != 0) or(a_year % 400 == 0):
        return True
    else:
        return False
    
year = 2018
result = is_leap_year(year)
print(result, "\n")

# Question 5 

def is_consecutive(a_list):
    if not a_list:
        return False
    min_num = min(a_list)
    max_num = max(a_list)
    num_list = set(range(min_num, max_num + 1))
    return set(a_list) == num_list

print(is_consecutive([2, 3, 4, 5, 6]))
print(is_consecutive([1, 3, 5, 7]))