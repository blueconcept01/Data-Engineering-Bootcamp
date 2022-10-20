from typing import Dict, List, Tuple

"""
n is an int
check if n is negative, return -1
Else, Return the numbers from 0 till n(including n)
"""
def list_numbers(n: int) -> List[int]:
    
    pass

"""
n is a positive integer

Return a list of integers from 1 to n(including n) that are even.
"""
def even_numbers(n: int) -> List[int]:
    
    pass

"""
n is a positive integer

Return a list of integers from 1 to n(including n) that are odd.
"""
def odd_numbers(n: int) -> List[int]:
    pass

"""
Implement a function that will take a string and return the list with its individual characters. If the string is empty, then return -1

For example: if string is "hello", then answer should be ['h', 'e', 'l', 'l', 'o']
"""
def individual_characters(string: str) -> Tuple[int, List[str]]:
    pass

"""
Implement a function that will take a string and return the list with its unique characters. If the string is empty, then return -1.

For example: if string is "hello", then answer should be ['h', 'e', 'l', 'o']

Make use of continue statement.
"""
def individual_unique_characters(string: str) -> Tuple[int, List[str]]:

    pass   

"""
Implement a function that will take a list of numbers(integers) and return the sum of numbers. If the list is empty, then return -1.

"""
def sum_list(num_list: List[int]) -> int:

    pass

"""
Implement a function that will take a list of numbers(integers) and return the maximum number from the list of numbers. 
If the list is empty, then return -1.

"""
def max_list(num_list: List[int]) -> int:

    pass

"""
Implement a function that will take a list of numbers(integers) and return the minimum number from the list of numbers. 
If the list is empty, then return -1.

"""
def min_list(num_list: List[int]) -> int:

    pass   

"""
Implement a function that will take a list of numbers(integers) and number num and check whether the number exists in the list.

If number exists return "Found", else return "Not Found"
If the list is empty, then return -1.

Make use of break statement
"""
def find_num_in_list(num_list: List[int], num: int) -> Tuple[str, int]:

    pass

"""
Implement a function that will take a list of numbers(integers) and return the list of positive numbers from the list of numbers. 
If the list is empty, then return -1.
If there are no positive numbers in the list, return -1

Make use of continue statement.
"""
def get_positives(num_list: List[int]) -> int:

    pass 

"""
Implement a function that will take a list of numbers(integers) and return the list of negative numbers from the list of numbers. 
If the list is empty, then return -1.
If there are no negative numbers in the list, return -1

Make use of continue statement.
"""
def get_negative(num_list: List[int]) -> int:

    pass  

"""
Implement a function that will take a dictionary and return the list of keys from the dictionary
For example: if dictionary is {'a':1, 'b': 2}, then it should return ['a', 'b'] 

If the dictionary is empty, then return -1.
"""
def get_keys(dictionary: Dict) -> List:

    pass 

"""
Implement a function that will take a dictionary and return the list of values from the dictionary
For example: if dictionary is {'a':1, 'b': 2}, then it should return [1, 2] 

If the dictionary is empty, then return -1.
"""
def get_values(dictionary: Dict) -> List:

    pass


"""
Implement a function to return the coordinates of a plane.

You are given two list of coordinates 
x-coordinates x1, x2, x3,....
y-coordinates y1, y2, y3, .....

Return a list of (x, y) coordinates i.e all possible coordinates in the plane [(x1, y1), (x1, y2), (x1, y3),(x2, y1), (x2, y2), .....]

If any lists of coordinates are empty, return -1

"""
def get_coordinates(x_coordinates: List[int], y_coordinates: List[int]) -> List[Tuple[int, int]]:

    pass


import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # list_numbers function
        self.assertEqual(list_numbers(5), [0, 1, 2, 3, 4, 5], msg="Returning the list from 0 till given number") 
        self.assertEqual(list_numbers(-1), -1, msg="Returning -1 as the given number is negative") 
        
        # even_numbers function
        self.assertEqual(even_numbers(5), [2, 4], msg="Returning list of even numbers from 1 till the given number")
        self.assertEqual(even_numbers(12), [2, 4, 6, 8, 10, 12], msg="Returning list of even numbers from 1 till the given number")
        self.assertEqual(even_numbers(1), [], msg="Returning empty list")

        # odd_numbers function
        self.assertEqual(odd_numbers(5), [1, 3, 5], msg="Returning list of odd numbers from 1 till the given number")
        self.assertEqual(odd_numbers(12), [1, 3, 5, 7, 9, 11], msg="Returning list of odd numbers from 1 till the given number")
        self.assertEqual(odd_numbers(0), [], msg="Returning empty list")       

        # individual_characters function
        self.assertEqual(individual_characters("hello"), ['h', 'e', 'l', 'l', 'o'], msg="Returning list of characters in the string")
        self.assertEqual(individual_characters("okay"), ['o', 'k', 'a', 'y'], msg="Returning list of characters in the string")
        self.assertEqual(individual_characters(""), -1, msg="Returning -1 as given string is empty")    

        # individual_unique_characters function
        self.assertEqual(individual_unique_characters("hello"), ['h', 'e', 'l', 'o'], msg="Returning list of unique characters in the string")
        self.assertEqual(individual_unique_characters("okay"), ['o', 'k', 'a', 'y'], msg="Returning list of unique characters in the string")
        self.assertEqual(individual_characters(""), -1, msg="Returning -1 as given string is empty")               

        # sum_list function
        self.assertEqual(sum_list([1, 2, 3, 4]),10, msg="Returning the sum of all the numbers in the list")
        self.assertEqual(sum_list([2, 2, 2]),6, msg="Returning the sum of all the numbers in the list")
        self.assertEqual(sum_list([]), -1, msg="Returning -1 as given list is empty") 

        # max_list function
        self.assertEqual(max_list([1, 2, 3, 4]),4, msg="Returning the maximum of all the numbers in the list")
        self.assertEqual(max_list([2, 2, 2]),2, msg="Returning the maximum of all the numbers in the list")
        self.assertEqual(max_list([]), -1, msg="Returning -1 as given list is empty")

        # min_list function
        self.assertEqual(min_list([1, 2, 3, 4]),1, msg="Returning the minimum of all the numbers in the list")
        self.assertEqual(min_list([2, 2, 2]),2, msg="Returning the minimum of all the numbers in the list")
        self.assertEqual(min_list([]), -1, msg="Returning -1 as given list is empty")        

        # find_num_in_list function
        self.assertEqual(find_num_in_list([1, 2, 3, 4], 4),"Found", msg="Returning Found as number exists in the list")
        self.assertEqual(find_num_in_list([2, 2, 2], 3),"Not Found", msg="Returning Not Found as the number not found")
        self.assertEqual(find_num_in_list([], 5), -1, msg="Returning -1 as given list is empty")

        # get_positives function
        self.assertEqual(get_positives([1, -2, 3, -1, -8, 0]),[1, 3], msg="Returning the list of positive numbers that exists in the list")
        self.assertEqual(get_positives([-1, -2, -3]),-1, msg="Returning -1 as there are no positive numbers in the list")
        self.assertEqual(get_positives([]), -1, msg="Returning -1 as given list is empty")     

        # get_negative function
        self.assertEqual(get_negative([1, -2, 3, -1, -8, 0]),[-2, -1, -8], msg="Returning the list of negative numbers that exists in the list")
        self.assertEqual(get_negative([1, 2, 3]),-1, msg="Returning -1 as there are no negative numbers in the list")
        self.assertEqual(get_negative([]), -1, msg="Returning -1 as given list is empty")    

        # get_keys function
        self.assertEqual(get_keys({'hello': 1, 'my': 7, 'okay': 4}),['hello', 'my', 'okay'], msg="Returning the keys from the given dictionary")
        self.assertEqual(get_keys({}), -1, msg="Returning -1 as given dictionary is empty")   

        # get_values function
        self.assertEqual(get_values({'hello': 1, 'my': 7, 'okay': 4}),[1, 7, 4], msg="Returning the values from the given dictionary")
        self.assertEqual(get_values({}), -1, msg="Returning -1 as given dictionary is empty")          

        # get_coordinates function
        self.assertEqual(get_coordinates([1, 2], [3, 4]),[(1, 3), (1, 4), (2, 3), (2, 4)], msg="Returning the (x, y) coordinates)")
        self.assertEqual(get_coordinates([1], [3, 4]),[(1, 3), (1, 4)], msg="Returning the (x, y) coordinates)")
        self.assertEqual(get_coordinates([], [1, 2]), -1, msg="Returning -1 as x-coordinates is empty")                      
        self.assertEqual(get_coordinates([1, 2], []), -1, msg="Returning -1 as y-coordinates is empty")          

unittest.main()
