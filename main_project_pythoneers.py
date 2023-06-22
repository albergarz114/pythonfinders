import random
import time
import os
from datetime import datetime, timedelta                     # Imported datetime to make presentable
from random import choice                                    # imported random choice function

def show_menu():
    print("\n   Menu:")
    print("1. Python quiz")
    print("2. Python Quiz For our Level")
    print("3. Tutorial Menu")
    print("4. Jokes from Alberto")
    print("5. Receive a compliment and good mood from T & T")
    print("6. Organizer from Kerim\n")
    print("0. Exit")
 
# List of quiz questions
quiz_questions = [
    {
        #1 abs()
        "question":"1. What built-in function in Python returns the absolute value of a number?",
        "options": ["A. abs()", "B. absolute()", "C. abs_value()", "D. value()"],
        "correct_answer": "A"
    },
    {
        #2 all()
        "question": "2. What built-in function in Python returns True if all items in an iterable object are true?",
        "options": ["A. allinclusive()", "B. all()", "C. all_all()", "D. any()"],
        "correct_answer": "B"
    },
    {
        #3 any()
        "question": "3. What built-in function in Python returns True if any item in an iterable object is true?",
        "options": ["A. allinclusive()", "B. all()", "C. all_all()", "D. any()"],
        "correct_answer": "D"
    },
    {
        #4 assii()
        "question": "4. What built-in function in Python returns a readable version of an object, replaces none-ascii characters with escape character?",
        "options": ["A. ascii()", "B. anyret()", "C. ascdo()()", "D. anyway()"],
        "correct_answer": "A"
    },
    {
        #5 bin()
        "question": "5. Which built-in function in Python returns the binary version of a number?",
        "options": ["A. str_to_bin()", "B. bin()", "C. loot()", "D. convert_in()"],
        "correct_answer": "B"
    },
    {
        #6 bool()
        "question": "6. Which built-in function in Python returns the boolean value of the specified object?",
        "options": ["A. lenbo()", "B. length()", "C. bool()", "D. size()"],
        "correct_answer": "C"
    },
    {
        #7 bytearray()
        "question":"7. Which built-in function in Python returns an array of bytes?",
        "options": ["A. random()", "B. array()", "C. bytearray()", "D. randomnumber()"],
        "correct_answer": "C"
    },
    {
        #8 bytes()
        "question": "8. Which built-in function in Python returns a bytes object?",
        "options": ["A. float()", "B. bytes()", "C. isbytes()", "D. isinstance()"],
        "correct_answer": "B"
    },
    {
        #9 callable()
        "question": "9. What built-in function in Python returns True if the specified object is callable, otherwise False?",
        "options": ["A. callable()", "B. to_call()", "C. intcall()", "D. convert_call()"],
        "correct_answer": "A"
    },
    {
        #10 chr() 
        "question": "10. Which built-in function in Python returns a character from the specified Unicode code?",
        "options": ["A. len()", "B. chr()", "C. countchr()", "D. sizeit()"],
        "correct_answer": "B"
    },
    {
        #11 classmethod()
        "question": "11. What built-in function in Python converts a method into a class method?",
        "options": ["A. classmethod()", "B. class()", "C. concat()", "D. append()"],
        "correct_answer": "A"
    },
    {
        #12 compile()
        "question": "12. What built-in function in Python returns the specified source as an object, ready to be executed?",
        "options": ["A. compile()", "B. absolute()", "C. value()", "D. das_ist_value()"],
        "correct_answer": "A"
    },
    {
        #13 complex()
        "question": "13. Which built-in function in Python returns a complex number?",
        "options": ["A. float()", "B. isfloat()", "C. iscomplex()", "D. complex()"],
        "correct_answer": "D"
    },
    {
        #14 delattr()
        "question": "14. What built-in function in Python deletes the specified attribute (property or method) from the specified object?",
        "options": ["A. str_to_int()", "B. int_delattr()", "C. delattr()", "D. convert_int()"],
        "correct_answer": "C"
    },
    {
        #15 dict()
        "question": "15. Which built-in function in Python returns a dictionary (Array)?",
        "options": ["A. len()", "B. dict()", "C. count()", "D. size()"],
        "correct_answer": "B"
    },
    {
        #16 dir()
        "question": "16. What built-in function in Python returns a list of the specified object's properties and methods?",
        "options": ["A. dir()", "B. merge()", "C. concatdir()", "D. append()"],
        "correct_answer": "A"
    },
    {
        #17 divmod()
        "question":"17. What built-in function in Python returns the quotient and the remainder when argument1 is divided by argument2?",
        "options": ["A. abs()", "B. divmod()", "C. div()", "D. value_div()"],
        "correct_answer": "B"
    },
    {
        #18 enumerate()
        "question": "18. What built-in function in Python takes a collection (e.g. a tuple) and returns it as an enumerate object?",
        "options": ["A. allnumer()", "B. enumerate()", "C. eval()", "D. any_numer()"],
        "correct_answer": "B"
    },
    {
        #19 eval()
        "question": "19. What built-in function in Python evaluates and executes an expression?",
        "options": ["A. allinclusive()", "B. val()", "C. all_call()", "D. eval()"],
        "correct_answer": "D"
    },
    {
        #20 exec()
        "question": "20. What built-in function in Python executes the specified code (or object)?",
        "options": ["A. exec()", "B. anyret()", "C. eval()", "D. anyway()"],
        "correct_answer": "A"
    },
    {
        #21 filter()
        "question": "21. Which built-in function in Python use a filter function to exclude items in an iterable object?",
        "options": ["A. str_to_bin()", "B. bin()", "C. classmethod()", "D. filter()"],
        "correct_answer": "D"
    },
    {
        #22 float()
        "question": "22. Which built-in function in Python returns a floating point number?",
        "options": ["A. lenbo()", "B. length()", "C. float()", "D. size()"],
        "correct_answer": "C"
    },
    {
        #23 format()
        "question":"23. Which built-in function in Python formats a specified value?",
        "options": ["A. randomarray()", "B. array()", "C. format()", "D. randomnumber()"],
        "correct_answer": "C"
    },
    {
        #24 frozenset()
        "question": "24. Which built-in function in Python returns a frozenset object?",
        "options": ["A. float()", "B. frozenset()", "C. isbytes()", "D. isinstance()"],
        "correct_answer": "B"
    },
    {
        #25 getattr()
        "question": "25. What built-in function in Python returns the value of the specified attribute (property or method)?",
        "options": ["A. getattr()", "B. to_call()", "C. intcall()", "D. convert_call()"],
        "correct_answer": "A"
    },
    {
        #26 globals()
        "question": "26. Which built-in function in Python returns the current global symbol table as a dictionary?",
        "options": ["A. len()", "B. chrom()", "C. count()", "D. globals()"],
        "correct_answer": "D"
    },
    {
        #27 hasattr()
        "question": "27. What built-in function in Python returns True if the specified object has the specified attribute (property/method)?",
        "options": ["A. classmethod()", "B. class()", "C. hasattr()", "D. append()"],
        "correct_answer": "C"
    },
    {
        #28 hash()
        "question": "28. What built-in function in Python returns the hash value of a specified object?",
        "options": ["A. hash()", "B. absolute()", "C. value()", "D. das_ist_value()"],
        "correct_answer": "A"
    },
    {
        #29 help()
        "question": "29. Which built-in function in Python executes the built-in help system?",
        "options": ["A. float()", "B. isfloat()", "C. is_complex()", "D. help()"],
        "correct_answer": "D"
    },
    {
        #30 hex()
        "question": "30. What built-in function in Python converts a number into a hexadecimal value?",
        "options": ["A. int()", "B. int_delattr()", "C. hex()", "D. convert_int()"],
        "correct_answer": "C"
    },
    {
        #31 id()
        "question": "31. Which built-in function in Python returns the id of an object?",
        "options": ["A. len()", "B. id()", "C. count()", "D. size()"],
        "correct_answer": "B"
    },
    {
        #32 input()
        "question": "32. What built-in function in Python allowing user input?",
        "options": ["A. dir()", "B. merge()", "C. concatdir()", "D. append()"],
        "correct_answer": "A"
    },
    {
        #33 int()
        "question":"33. What built-in function in Python returns an integer number?",
        "options": ["A. abs()", "B. absolute()", "C. int()", "D. value()"],
        "correct_answer": "C"
    },
    {
        #34 isinstance()
        "question": "34. What built-in function in Python returns True if a specified object is an instance of a specified object?",
        "options": ["A. isinstance()", "B. isall()", "C. allinstance()", "D. any()"],
        "correct_answer": "B"
    },
    {
        #35 issubclass()
        "question": "35. What built-in function in Python returns True  if a specified class is a subclass of a specified object?",
        "options": ["A. allinone()", "B. ally()", "C. allisall()", "D. issubclass()"],
        "correct_answer": "D"
    },
    {
        #36 iter()
        "question": "36. What built-in function in Python returns returns an iterator object?",
        "options": ["A. ascii()", "B. iter()", "C. hash()()", "D. max()"],
        "correct_answer": "B"
    },
    {
        #37 len()
        "question": "37. Which built-in function in Python returns the length of an object?",
        "options": ["A. len()", "B. bin()", "C. loot()", "D. convert_in()"],
        "correct_answer": "A"
    },
    {
        #38 list()
        "question": "38. Which built-in function in Python returns a list?",
        "options": ["A. list()", "B. length()", "C. bool()", "D. sizelist()"],
        "correct_answer": "A"
    },
    {
        #39 locals()
        "question":"39. Which built-in function in Python returns an updated dictionary of the current local symbol table?",
        "options": ["A. randomarray()", "B. array()", "C. locals()", "D. randomnumber()"],
        "correct_answer": "C"
    },
    {
        #40 map()
        "question": "40. Which built-in function in Python returns the specified iterator with the specified function applied to each item?",
        "options": ["A. float()", "B. map()", "C. isbytes()", "D. isinstance()"],
        "correct_answer": "B"
    },
    {
        #41 max()
        "question": "41. What built-in function in Python returns the largest item in an iterable?",
        "options": ["A. max()", "B. maxlen()", "C. intmax()", "D. convert_max()"],
        "correct_answer": "A"
    },
    {
        #42 memoryview()
        "question": "42. Which built-in function in Python returns a memory view object?",
        "options": ["A. lenmemoryview()", "B. chr()", "C. countchr()", "D. memoryview()"],
        "correct_answer": "D"
    },
    {
        #43 min()
        "question": "43. What built-in function in Python returns the smallest item in an iterable?",
        "options": ["A. min()", "B. minclass()", "C. concaticat()", "D. append()"],
        "correct_answer": "A"
    },
    {
        #44 next()
        "question": "44. What built-in function in Python returns the next item in an iterable?",
        "options": ["A. compile()", "B. next()", "C. valuenext()", "D. das_ist_value()"],
        "correct_answer": "B"
    },
    {
        #45 object()
        "question": "45. Which built-in function in Python returns a new object?",
        "options": ["A. float()", "B. isfloat()", "C. object()", "D. complex()"],
        "correct_answer": "C"
    },
    {
        #46 oct()
        "question": "46. What built-in function in Python converts a number into an octal?",
        "options": ["A. str_ok()", "B. int_oct()", "C. oct()", "D. convert_it()"],
        "correct_answer": "C"
    },
    {
        #47 open()
        "question": "47. Which built-in function in Python opens a file and returns a file object?",
        "options": ["A. len()", "B. open()", "C. count()", "D. size()"],
        "correct_answer": "B"
    },
    {
        #48 ord()
        "question": "48. What built-in function in Python convert an integer representing the Unicode of the specified character?",
        "options": ["A. dir()", "B. merge()", "C. ord()", "D. append()"],
        "correct_answer": "C"
    },
    {
        #49 pow()
        "question":"49. What built-in function in Python returns the value of x to the power of y?",
        "options": ["A. abs()", "B. pow()", "C. div()", "D. value_div()"],
        "correct_answer": "B"
    },
    {
        #50 print()
        "question": "50. What built-in function in Python prints to the standard output device?",
        "options": ["A. allnumer()", "B. print()", "C. eval()", "D. any_print()"],
        "correct_answer": "B"
    },
    {
        #51 property()
        "question": "51. What built-in function in Python gets, sets, deletes a property?",
        "options": ["A. all()", "B. val()", "C. isproperty()", "D. property()"],
        "correct_answer": "D"
    },
    {
        #52 range()
        "question": "52. What built-in function in Python returns a sequence of numbers, starting from 0 and increments by 1 (by default)?",
        "options": ["A. exec()", "B. range()", "C. eval()", "D. anyway()"],
        "correct_answer": "B"
    },
    {
        #53 repr()
        "question": "53. Which built-in function in Python returns a readable version of an object?",
        "options": ["A. strrepo()", "B. bin()", "C. classmaythod()", "D. repr()"],
        "correct_answer": "D"
    },
    {
        #54 reversed()
        "question": "54. Which built-in function in Python returns a reversed iterator?",
        "options": ["A. reversed()", "B. length()", "C. float()", "D. size()"],
        "correct_answer": "A"
    },
    
    {
        #55 round()
        "question":"55. Which built-in function in Python rounds a numbers?",
        "options": ["A. round()", "B. array()", "C. format()", "D. randomnumber()"],
        "correct_answer": "A"
    },
    {
        #56 set()
        "question": "56. Which built-in function in Python returns a new set object?",
        "options": ["A. setting()", "B. set()", "C. isset()", "D. isinstance()"],
        "correct_answer": "B"
    },
    {
        #57 setattr()
        "question": "57. What built-in function in Python sets an attribute (property/method) of an object?",
        "options": ["A. setattr()", "B. to_call()", "C. intcall()", "D. convert_call()"],
        "correct_answer": "A"
    },
    {
        #58 slice()
        "question": "58. Which built-in function in Python returns a slice object?",
        "options": ["A. len()", "B. slice()", "C. count()", "D. globals()"],
        "correct_answer": "B"
    },
    {
        #59 sorted()
        "question": "59. What built-in function in Python returns a sorted list?",
        "options": ["A. classmethod()", "B. class()", "C. sorted()", "D. appendsorted()"],
        "correct_answer": "C"
    },
    {
        #60 staticmethod()
        "question": "60. What built-in function in Python converts a method into a static method?",
        "options": ["A. hash()", "B. absolute()", "C. value()", "D. staticmethod()"],
        "correct_answer": "D"
    },
    {
        #61 str()
        "question": "61. Which built-in function in Python returns a string object?",
        "options": ["A. float()", "B. str()", "C. is_complex()", "D. help()"],
        "correct_answer": "B"
    },
    {
        #62 sum()
        "question": "62. What built-in function in Python sums the items of an iterator?",
        "options": ["A. int()", "B. int_delattr()", "C. sum()", "D. convert_int()"],
        "correct_answer": "C"
    },
    {
        #63 super()
        "question": "63. Which built-in function in Python returns an object that represents the parent class?",
        "options": ["A. len()", "B. super()", "C. count()", "D. size()"],
        "correct_answer": "B"
    },
    {
        #64 tuple()
        "question": "64. What built-in function in Python returns a tuple?",
        "options": ["A. tuple()", "B. list()", "C. set()", "D. append()"],
        "correct_answer": "A"
    },
    {
        #65 type()
        "question": "16. What built-in function in Python returns the type of an object?",
        "options": ["A. dir()", "B. merge()", "C. type()", "D. append()"],
        "correct_answer": "C"
    },
    {
        #66 vars()
        "question": "16. What built-in function in Python returns the __dict__ property of an object?",
        "options": ["A. vars()", "B. merge()", "C. concatdir()", "D. append()"],
        "correct_answer": "A"
    },
    {
        #67 zip()
        "question": "16. What built-in function in Python returns an iterator, from two or more iterators?",
        "options": ["A. dirzip()", "B. dipzip()", "C. zip()", "D. app()"],
        "correct_answer": "C"
    },
]
  # Initialize score counter

second_quiz_questions = [
     {
        #6 bool()
        "question_1": "6. Which built-in function in Python returns the boolean value of the specified object?",
        "options_1": ["A. lenbo()", "B. length()", "C. bool()", "D. size()"],
        "correct_answer_1": "C"
    },
    {
        #10 chr() 
        "question_1": "10. Which built-in function in Python returns a character from the specified Unicode code?",
        "options_1": ["A. len()", "B. chr()", "C. countchr()", "D. sizeit()"],
        "correct_answer_1": "B"
    },
    {
        #12 compile()
        "question_1": "12. What built-in function in Python returns the specified source as an object, ready to be executed?",
        "options_1": ["A. compile()", "B. absolute()", "C. value()", "D. das_ist_value()"],
        "correct_answer_1": "A"
    },
    {
        #13 complex()
        "question_1": "13. Which built-in function in Python returns a complex number?",
        "options_1": ["A. float()", "B. isfloat()", "C. iscomplex()", "D. complex()"],
        "correct_answer_1": "D"
    },
    {
        #15 dict()
        "question_1": "15. Which built-in function in Python returns a dictionary (Array)?",
        "options_1": ["A. len()", "B. dict()", "C. count()", "D. size()"],
        "correct_answer_1": "B"
    },
    {
        #16 dir()
        "question_1": "16. What built-in function in Python returns a list of the specified object's properties and methods?",
        "options_1": ["A. dir()", "B. merge()", "C. concatdir()", "D. append()"],
        "correct_answer_1": "A"
    },
    {
        #22 float()
        "question_1": "22. Which built-in function in Python returns a floating point number?",
        "options_1": ["A. lenbo()", "B. length()", "C. float()", "D. size()"],
        "correct_answer_1": "C"
    },
    {
        #26 globals()
        "question_1": "26. Which built-in function in Python returns the current global symbol table as a dictionary?",
        "options_1": ["A. len()", "B. chrom()", "C. count()", "D. globals()"],
        "correct_answer_1": "D"
    },
    {
        #30 hex()
        "question_1": "30. What built-in function in Python converts a number into a hexadecimal value?",
        "options_1": ["A. int()", "B. int_delattr()", "C. hex()", "D. convert_int()"],
        "correct_answer_1": "C"
    },
    {
        #31 id()
        "question_1": "31. Which built-in function in Python returns the id of an object?",
        "options_1": ["A. len()", "B. id()", "C. count()", "D. size()"],
        "correct_answer_1": "B"
    },
    {
        #32 input()
        "question_1": "32. What built-in function in Python allowing user input?",
        "options_1": ["A. dir()", "B. merge()", "C. concatdir()", "D. append()"],
        "correct_answer_1": "A"
    },
    {
        #33 int()
        "question_1":"33. What built-in function in Python returns an integer number?",
        "options_1": ["A. abs()", "B. absolute()", "C. int()", "D. value()"],
        "correct_answer_1": "C"
    },
    {
        #34 isinstance()
        "question_1": "34. What built-in function in Python returns True if a specified object is an instance of a specified object?",
        "options_1": ["A. isinstance()", "B. isall()", "C. allinstance()", "D. any()"],
        "correct_answer_1": "B"
    },
    {
        #37 len()
        "question_1": "37. Which built-in function in Python returns the length of an object?",
        "options_1": ["A. len()", "B. bin()", "C. loot()", "D. convert_in()"],
        "correct_answer_1": "A"
    },
    {
        #38 list()
        "question_1": "38. Which built-in function in Python returns a list?",
        "options_1": ["A. list()", "B. length()", "C. bool()", "D. sizelist()"],
        "correct_answer_1": "A"
    },
    {
        #40 map()
        "question_1": "40. Which built-in function in Python returns the specified iterator with the specified function applied to each item?",
        "options_1": ["A. float()", "B. map()", "C. isbytes()", "D. isinstance()"],
        "correct_answer_1": "B"
    },
    {
        #47 open()
        "question_1": "47. Which built-in function in Python opens a file and returns a file object?",
        "options_1": ["A. len()", "B. open()", "C. count()", "D. size()"],
        "correct_answer_1": "B"
    },
    {
        #50 print()
        "question_1": "50. What built-in function in Python prints to the standard output device?",
        "options_1": ["A. allnumer()", "B. print()", "C. eval()", "D. any_print()"],
        "correct_answer_1": "B"
    },
    {
        #56 set()
        "question_1": "56. Which built-in function in Python returns a new set object?",
        "options_1": ["A. setting()", "B. set()", "C. isset()", "D. isinstance()"],
        "correct_answer_1": "B"
    },
    {
        #58 slice()
        "question_1": "58. Which built-in function in Python returns a slice object?",
        "options_1": ["A. len()", "B. slice()", "C. count()", "D. globals()"],
        "correct_answer_1": "B"
    },
    {
        #59 sorted()
        "question_1": "59. What built-in function in Python returns a sorted list?",
        "options_1": ["A. classmethod()", "B. class()", "C. sorted()", "D. appendsorted()"],
        "correct_answer_1": "C"
    },
    {
        #61 str()
        "question_1": "61. Which built-in function in Python returns a string object?",
        "options_1": ["A. float()", "B. str()", "C. is_complex()", "D. help()"],
        "correct_answer_1": "B"
    },
    {
        #64 tuple()
        "question_1": "64. What built-in function in Python returns a tuple?",
        "options_1": ["A. tuple()", "B. list()", "C. set()", "D. append()"],
        "correct_answer_1": "A"
    },
    {
        #65 type()
        "question_1": "16. What built-in function in Python returns the type of an object?",
        "options_1": ["A. dir()", "B. merge()", "C. type()", "D. append()"],
        "correct_answer_1": "C"
    },
    {
        #66 vars()
        "question_1": "16. What built-in function in Python returns the __dict__ property of an object?",
        "options_1": ["A. vars()", "B. merge()", "C. concatdir()", "D. append()"],
        "correct_answer_1": "A"
    },
    {
        #67 zip()
        "question_1": "16. What built-in function in Python returns an iterator, from two or more iterators?",
        "options_1": ["A. dirzip()", "B. dipzip()", "C. zip()", "D. app()"],
        "correct_answer_1": "C"
    },
]
  # Initialize score counter

# quiz #1

def display_question(question):
   # def display_question(question):
   # This line defines a function named display_question that takes a parameter called question. 
   # The function is defined to display the given question on the screen.
    print(question["question"])
      # print(question["question"])
      # This line prints the value associated with the key "question" in the question dictionary.
      # It displays the actual question text on the screen.
    for option in question["options"]:
        # for option in question["options"]:
        # This line starts a loop that iterates over each element (referred to as option) in the list associated with the key 
        # "options" in the question dictionary.
        print(option)
            # print(option)
            # This line prints each option on a separate line.
            # It displays the available answer options for the question.
    print()
        # print()
        # This line prints an empty line, which creates a blank line on the screen.
        # It adds a visual separation after displaying the question and answer options.
        # To summarize, the display_question function takes a question as input, which is a dictionary 
        # containing the question text and answer options. The function then prints the question, 
        # displays each answer option, and adds a blank line for visual clarity. 
        # This function helps to present a question and its answer options in a formatted manner when called in the program.

def get_user_answer():
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        # user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        # This line prompts the user to enter their answer by displaying the message "Enter your answer (A, B, C, or D): ".
        # The input() function waits for the user to input a value, and the entered value is stored in the variable user_answer.
        # .upper() is used to convert the user's input to uppercase letters. This ensures that the user's answer is case-insensitive.
    while user_answer not in ["A", "B", "C", "D"]:
            # while user_answer not in ["A", "B", "C", "D"]:
            # This line starts a while loop. It will continue looping as long as the user_answer is not one of the valid options: "A", "B", "C", or "D".
            # The loop checks if the user_answer is not present in the list ["A", "B", "C", "D"].
            # If the condition is true (i.e., the user's answer is not valid), the loop will execute the code inside it. Otherwise, it will exit the loop.
        print("Invalid input! Please enter A, B, C, or D.")
                # Inside the while loop:
                # print("Invalid input! Please enter A, B, C, or D.") prints an error message indicating that the user's input is invalid.    
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
                # user_answer = input("Enter your answer (A, B, C, or D): ").upper()
                # This line prompts the user to enter their answer by displaying the message "Enter your answer (A, B, C, or D): ".
                # The input() function waits for the user to input a value, and the entered value is stored in the variable user_answer.
                # .upper() is used to convert the user's input to uppercase letters. This ensures that the user's answer is case-insensitive.
                # while user_answer not in ["A", "B", "C", "D"]:
    return user_answer
        # user_answer = input("Enter your answer (A, B, C, or D): ").upper() prompts the user again to enter their answer.
        # The entered value is stored in the user_answer variable after converting it to uppercase.
        # return user_answer
        # Once the user provides a valid answer (i.e., it is one of "A", "B", "C", or "D"), the loop will exit, and the function will 
        # return the valid user_answer value.
        # In summary, this code prompts the user to enter their answer (expecting "A", "B", "C", or "D"), 
        # and it keeps asking for input until a valid answer is provided. 
        # The function then returns the valid user answer for further processing in the program.

def check_answer(question, user_answer):
    if user_answer == question["correct_answer"]:
        print("Correct answer!")
        return True
    else:
        print("Wrong answer!")
        return False

def play_quiz(num_questions):
    score = 0
    questions = random.sample(quiz_questions, num_questions)  # Select random questions
    user_answers = {}  # Dictionary to store user answers for each question
    for question in questions:
        display_question(question)
        start_time = time.time()  # Start tracking time
        user_answer = get_user_answer()
        end_time = time.time()  # Stop tracking time
        time_taken = end_time - start_time
        if time_taken > 60:  # Check if time limit (60 seconds) exceeded
            print("Time's up!")
        else:
            if check_answer(question, user_answer):
                score += 1  # Increment score for each correct answer
            user_answers[question["question"]] = user_answer  # Store user answer
        print()
       # Display correct answers
    print("Correct answers:")
    for question in questions:
        print(question["question"])
        print("Correct answer:", question["correct_answer"])
        print()
    
    # Display user's answers
    print("Your answers:")
    for question, user_answer in user_answers.items():
        print(question)
        print("Your answer:", user_answer)
        print()
    
    return score

def main_quiz_menu():
    print("Welcome to the Python Quiz!")
    num_questions = int(input("Enter the number of questions you want to attempt(From 1 up to 67): "))
    print()
    score = play_quiz(num_questions)
    print("Quiz completed!")
    print("Your score:", score)

# quiz #2

# The display_question_1() function is used to display a question and its corresponding options. 
# Here's how it works:
# 1. The function takes a parameter question_1, which is a dictionary representing a question and its options.
def display_question_1(question_1):
  
# 2. It prints the question by accessing the value associated with the key "question_1" in the question_1 dictionary.   
    print(question_1["question_1"])
    
# 3. The function then enters a loop that iterates over each option in the "options_1" list of the question_1 dictionary.
    for option_1 in question_1["options_1"]:
        
# 4. For each option, it prints the option by iterating through the loop.
        print(option_1)
        
# 5. After displaying all the options, it prints a blank line using print() to create a separation between questions.
    print()
# 6. The function does not return any value.

#  By using this function, you can easily display a question and its options to the user. 
#  It improves the readability of the code and helps in presenting the quiz questions in a clear and organized manner.


#  The code defines a function called get_user_answer_1(), which is responsible for getting and 
#  validating the user's answer to a question. Here's how it works:
# 1. The function prompts the user to enter their answer with the message "Enter your answer (A, B, C, or D): ".
def get_user_answer_1():

# 2. The input() function is used to capture the user's input, and upper() is applied to convert the input to uppercase. 
#  This is done to make the user's input case-insensitive, allowing them to enter either lowercase or uppercase letters.   
    user_answer_1 = input("Enter your answer (A, B, C, or D): ").upper()
    
# 3. The while loop is used to repeatedly check if the user's answer is not one of the valid options ("A", "B", "C", or "D").
    while user_answer_1 not in ["A", "B", "C", "D"]:
        
# 4. If the user enters an invalid answer, the code inside the loop is executed. It displays the error message "Invalid input! 
# Please enter A, B, C, or D." using the print() function.
        print("Invalid input! Please enter A, B, C, or D.")
        
# 5. After displaying the error message, the user is prompted again to enter their answer with the same message as before.
# 6. The user's input is captured again and converted to uppercase.
# 7. The loop continues until the user enters a valid answer (one of the options "A", "B", "C", or "D").
        user_answer_1 = input("Enter your answer (A, B, C, or D): ").upper()
    
# 8. When the user finally enters a valid answer, the loop is exited, and the function returns the valid 
#  user answer using the return statement.    
    return user_answer_1

#  The code defines a function called check_answer_1() that compares the user's answer to the correct answer for question 1. 
#  Here's how it works:
#  1. The function takes two parameters: question_1 and user_answer_1. question_1 is a dictionary that contains 
#  the question information, including the correct answer, and user_answer_1 is the user's answer to question 1.
def check_answer_1(question_1, user_answer_1):
    
#  2. The if statement is used to compare the user's answer (user_answer_1) with the correct answer 
#  for question 1 (question_1["correct_answer_1"]).   
    if user_answer_1 == question_1["correct_answer_1"]:
        
#  3. If the user's answer matches the correct answer, the code inside the if block is executed.
#  It displays the message "Correct answer!" using the print() function.
        print("Correct answer!")
        
#  4. After displaying the message, the function returns True to indicate that the answer is correct.       
        return True
    
    else:
        
#  5. If the user's answer does not match the correct answer, the code inside the else block is executed. 
#  It displays the message "Wrong answer!" using the print() function.
        print("Wrong answer!")
        
#  6. After displaying the message, the function returns False to indicate that the answer is wrong.
        return False
    """
  7. By using this function, you can check if the user's answer for question 1 is correct or not 
  by passing the question information and the user's answer to the function.
 
  The function will compare the answers and provide the appropriate feedback.
    """

#  The code defines a function called play_second_quiz_1() that allows the user to play the second quiz.
#  Here's how it works:

#   1. The function takes a parameter num_questions_1 that represents the number of questions to be included in the quiz.   
def play_second_quiz_1(num_questions_1):
    
#  2. The score_1 variable is initialized to 0 to keep track of the user's score.  
    score_1 = 0
    
#  3. questions_1 is created by randomly selecting num_questions_1 questions from the second_quiz_questions list.   
    questions_1 = random.sample(second_quiz_questions, num_questions_1) # Select random questions
    
#  4. user_answers_1 is an empty dictionary that will be used to store the user's answers for each question.   
    user_answers_1 = {}  # Dictionary to store user answers for each question
    
#  5. The function then loops through each question in questions_1. 
    for question_1 in questions_1:
        
#  6. For each question, it displays the question to the user using the display_question_1() function.
        display_question_1(question_1)
        
#  7. It starts tracking the time by recording the current time in the start_time_1 variable.
        start_time_1 = time.time()  # Start tracking time
        
#  8. The user's answer for the question is obtained using the get_user_answer_1() function.
        user_answer_1 = get_user_answer_1()
        
#  9. The time tracking is stopped by recording the current time in the end_time_1 variable.
        end_time_1 = time.time()  # Stop tracking time
        
#  10. The time taken to answer the question is calculated by subtracting start_time_1 from end_time_1.
        time_taken_1 = end_time_1 - start_time_1
        if time_taken_1 > 60:  # Check if time limit (60 seconds) exceeded

#  11. If the time taken exceeds 60 seconds, a message "Time's up!" is displayed.
            print("Time's up!")
        else:
            
#  12. Otherwise, it checks if the user's answer is correct by calling the check_answer_1() function.  
            if check_answer_1(question_1, user_answer_1):
                
#  13. If the answer is correct, the score_1 is incremented by 1.
                score_1 += 1  # Increment score for each correct answer
                
#  14. The user's answer is stored in the user_answers_1 dictionary using the question as the key and the user's answer as the value.
            user_answers_1[question_1["question_1"]] = user_answer_1  # Store user answer
            
#  15. After each question, a blank line is printed to separate the questions.
        print()

    # Display correct answers
    
#  16. After all the questions have been answered, the function displays the correct answers and the user's answers.
    print("Correct answers:")
    
#  17. It loops through the questions_1 and prints each question along with the correct answer.
    for question_1 in questions_1:
        print(question_1["question_1"])
        print("Correct answer:", question_1["correct_answer_1"])
        print()
    
    # Display user's answers
    
#  18. It then loops through the user_answers_1 dictionary and prints each question along with the user's answer.
    print("Your answers:")
    for question_1, user_answer_1 in user_answers_1.items():
        print(question_1)
        print("Your answer:", user_answer_1)
        print()

#  19. Finally, the function returns the score_1, which represents the user's final score.
    return score_1   
#  By using this function, you can play the second quiz, track the user's answers, and calculate the score based on the correct answers.
    
    
#  The second_quiz_menu_1() function serves as a menu for the Python quiz. 
#  Here's how it works: 
#  1. The function starts by printing a welcome message to greet the user.  
def second_quiz_menu_1():
    print("Welcome to the Python Quiz For our Level!")
    
#  2. It prompts the user to enter the number of questions they want to attempt in the quiz. 
#  The input is obtained using the input() function and converted to an integer using int() for further processing.
    num_questions_1 = int(input("Enter the number of questions you want to attempt: "))
    
#  3. After the user enters the number of questions, it prints a blank line for formatting purposes.  
    print()
    
#  4. The function then calls the play_second_quiz_1() function, passing the num_questions_1 as an argument.
#  This starts the quiz and returns the score achieved by the user, which is stored in the score_1 variable.
    score_1 = play_second_quiz_1(num_questions_1)
    
#  5. Once the quiz is completed, it prints a message indicating that the quiz has been completed.  
    print("Quiz completed!")
    
#  6. Finally, it prints the user's score achieved in the quiz by displaying the message 
#  "Your score:" followed by the value of the score_1 variable.
    print("Your score:", score_1)

    """
This function provides a simple menu interface for the Python quiz, allowing the user to choose the 
number of questions they want to attempt and displaying their final score after completing the quiz.
    """

# Tutorial Stuff

def tutorial_menu():
    print("1 Introduction")
    print("2 Variables and Examples")
    print("3 Data Types and Examples")
    print("4 Conditional Statements")
    print("5 Loops")
    print("6 Functions")
    print("7 Lists and Dictionaries")
    print("8 File Handling")
    print("9 Conclusion")
    print("0 Back to Main Menu")

def introduction():
    print("Welcome to the Python Tutorial!")
    print("In this tutorial, you will learn the basics of Python programming.")

    print("""
Introduction:

Python was created by Guido van Rossum and released in 1991.

It is used for:
- Web development (server-side)
- Software development
- Mathematics
- System scripting

What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems and read/modify files.
Python can handle big data and perform complex mathematics.
Python can be used for rapid prototyping or production-ready software development.

Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python allows developers to write programs with fewer lines compared to some other languages.
Python runs on an interpreter system, enabling quick prototyping.
Python supports procedural, object-oriented, and functional programming.

Python Syntax compared to other programming languages:
Python was designed for readability, with influences from the English language and mathematics.
Python uses new lines to complete a command, instead of semicolons or parentheses.
Python defines scope using indentation (whitespace), unlike other languages that use curly braces.
""")

def variable_and_examples():
    print("""
Variables and Data Types:

In Python, you can use variables to store values.
For example:
name = 'John'
age = 25
pi = 3.14

You can also perform operations on variables.
For example:
result = 10 + 5
print(result)  # Output: 15

Variables do not need to be declared with any particular type and can even change type after they have been set.
If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))
""")

def data_types_and_examples():
    print("# The following code example would print the data type of x, what data type would that be?\n"
"int - or integer, is a whole number, positive or negative, without decimals, of unlimited length\n"
"\nx = 5\n"
"print(type(x)) # <class 'int'>\n"

"\n The following code example would print the data type of x, what data type would that be?\n"
"str - A STRING is literally a \"string\" of characters. A letter, a sentence, anything that is not a \"value\"\n"
"Python Strings are sequences of characters.\n"
"The four main ways to create strings are the following.\n"
"1. Single quotes 'Yes'\n"
"2. Double quotes \"Yes\"\n"
"3. Triple quotes (multi-line)\"\"\" \"\"\"Yes we can\"\"\"\n"
"4. String method str(5) == '5' True\n"
"5. Concatenation \"Ma\" + \"hatma\" # 'Mahatma'\n"
"These are whitespace characters in strings.\n")

    print("This is a newline: \\n")
    print("This is a tab: \\t")
    
    print("\nx1 = \"Hello World\"\n"
"x2 = 'Hello Tendai'\n"
"print(type(x1)) # <class 'str'>\n"
"print(type(x2))\n"

"\n The following code example would print the data type of x, what data type would that be?\n"
"float - Float is a function or reusable code in the Python programming language that converts values into\n"
"floating point numbers. Floating point numbers are decimal values or fractional numbers like 133.5, 2897.11,\n"
"and 3571.213, whereas real numbers like 56, 2, and 33 are called integers.\n"
"\nx = 20.5\n"
"print(type(x)) # <class 'float'>\n"

"\n The following code example would print the data type of x, what data type would that be?\n"
"list - A container data type that stores a sequence of elements. Unlike strings, lists are mutable: modification possible.\n"
"Lists are used to store multiple items in a single variable.\n"
"Lists are one of 4 built-in data types in Python used to store collections of data,\n"
"the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.\n"
"The most common way to declare a list in Python is to use square brackets.\n"
"A list is a data structure in Python that contains an ordered sequence of zero or more elements.\n"
"Lists in Python are mutable, which means they can be changed. They can contain any type of data, like a string or a dictionary.\n"
"\nx = [\"apple\", \"banana\", \"cherry\"]\n"
"print(type(x)) # <class 'list'>\n"

"\n The following code example would print the data type of x, what data type would that be?\n"
"tuple - A tuple is a collection which is ordered and unchangeable. The primary difference between tuples and lists is\n"
"that tuples are immutable as opposed to lists which are mutable.\n"
"Therefore, it is possible to change a list but not a tuple.\n"
"The contents of a tuple cannot change once they have been created in Python due to the immutability of tuples.\n"
"Tuples are more memory efficient than the lists.\n"
"When it comes to the time efficiency, tuples have a slight advantage over the lists\n"
"especially when we consider lookup value.\n"
"If you have data that shouldn't change, you should choose tuple data type over lists.\n"
"\nx = (\"apple\", \"banana\", \"cherry\")\n"
"print(type(x)) # <class 'tuple'>\n"

"\n The following code example would print the data type of x, what data type would that be?\n"
"dict - Dict Hash Table. Python's efficient key/value hash table structure is called a \"dict\".\n"
"The contents of a dict can be written as a series of key:value pairs within braces { },\n"
"e.g. dict = {key1:value1, key2:value2, ... }.\n"
"The dict() function creates a dictionary. A dictionary is a collection which is unordered, changeable and indexed.\n"
"What Are Python Dictionaries Used for? Python dictionaries allow us to associate a value to a unique key,\n"
"and then to quickly access this value. It's a good idea to use them whenever we want to find (lookup for) a certain Python object.\n"
"\nx = {\"name\" : \"John\", \"age\" : 36}\n"
"print(type(x)) # <class 'dict'>\n"

"\n The following code example would print the data type of x, what data type would that be?\n"
"bool - The Boolean data type is a truth value, either True​ ​ or False​. The bool() function returns the boolean value of a specified object.\n"
"The object will always return True, unless: The object is empty, like [], (), {} The object is False.\n"
"The Python Boolean type is one of Python's built-in data types. It's used to represent the truth value of an expression.\n"
"For example, the expression 1 <= 2 is True , while the expression 0 == 1 is False .\n"
"Understanding how Python Boolean values behave is important to programming well in Python.\n"
"\nx = True\n"
"print(type(x)) # <class 'bool'>\n"

"\n The following code example would print the data type of x, what data type would that be?\n"
"Python complex() Function. Python complex() function is used to convert numbers or string into a complex number.\n"
"This method takes two optional parameters and returns a complex number.\n"
"The first parameter is called a real and second as imaginary parts.\n"
"\nx = 5\n"
"x = complex(x)\n"
"print(type(x)) # <class 'complex'>\n")

def conditional_example():
    print("Conditional Statements:")
    print("Conditional statements are used to make decisions in the program.")
    print("For example:")
    print("x = 10")
    print("if x > 0:")
    print("    print('Positive')")
    print("elif x < 0:")
    print("    print('Negative')")
    print("else:")
    print("    print('Zero')")
    print("This will output 'Positive'.")

def loop_example():
    print("Loops:")
    print("Loops are used to repeat a block of code multiple times.")
    print("For example:")
    print("for i in range(5):")
    print("    print(i)")
    print("This will output numbers from 0 to 4.")

def function_example():
    print("Functions:")
    print("Functions are reusable blocks of code.")
    print("For example:")
    print("def greet(name):")
    print("    print('Hello, ' + name + '!')")
    print("greet('Alice')")
    print("This will output 'Hello, Alice!'")

def list_dict_example():
    print("Lists and Dictionaries:")
    print("Lists and dictionaries are used to store collections of data.")
    print("For example:")
    print("fruits = ['apple', 'banana', 'orange']")
    print("print(fruits[0])  # Output: 'apple'")
    print("ages = {'John': 25, 'Alice': 30, 'Bob': 35}")
    print("print(ages['Alice'])  # Output: 30")

def file_handling_example():
    print("File Handling:")
    print("You can read from and write to files in Python.")
    print("For example, to read from a file:")
    print("file = open('example.txt', 'r')")
    print("content = file.read()")
    print("print(content)")
    print("file.close()")
    print("To write to a file:")
    print("file = open('example.txt', 'w')")
    print("file.write('Hello, world!')")
    print("file.close()")

def print_conclusion():
    print("Congratulations!")
    print("You have completed the Python tutorial.")
    print("Now you have a basic understanding of Python programming.")

# Jokes from Alberto

Today_Date = datetime.now()             # .now() to get the present/current date

year = Today_Date.strftime("%Y")        ##strftime:datetime object####
month = Today_Date.strftime("%m")
day = Today_Date.strftime("%d")
Formatted_Date = day + "/" + month + "/" + year 

def jokes_menu():                        #def
    print("\n   Menu:")                 #displays menu and all options on Terminal
    print("1. Logical Jokes")
    print("2. Random Jokes")
    print("0. Exit")

def love():
    # List of logical jokes
    logical_jokes = [                               
        "U look good today.",
        "How do mathematicians scold their children?\n\t> If I've told you n times, I've told you n+1 times... Math equations use letters in place of unsolved numbers.",
        "A mathematician wanders back home at 3 a.m. and proceeds to get an earful from his wife.\n\t> 'You are late!' she yells. 'You said you'd be home by 11:45!' Actually, the mathematician replies coolly, I said I'd be home by a quarter of 12. Divide 12 by four or a quarter, which is three!",
        "Did you hear about the mathematician who's afraid of negative numbers?\n\t> He will stop at nothing to avoid them. Explanation: Once he hits zero in the countdown, it's all negative numbers from there.",
        "Why did Beethoven get rid of his chickens?\n\t> All they said was Bach, Bach, Bach.",
        "C, E-flat, and G walk into a bar.\n\t> The bartender shows them the door and says, 'Sorry, we don't serve minors.'",
        "A sign at a music shop:\n\t> Gone chopin. Bach in a minuet.",
        "What was Beethoven's favorite fruit?\n\t> Ba-na-na-naaaaaaa!",                         ####REMEMBER!!!! LISTS ARE WITH BRACKETS###
        "DNA say to the other DNA?\n\t> Do these genes make me look fat?",
        "A German walks into a bar and asks for a martini. The bartender asks, 'Dry?'\n\t> The German replies, 'Nein, just one.'",
        "I finally decided to sell my vacuum cleaner.\n\t> All it was doing was gathering dust.",
        "If you jumped off the bridge in Paris,\n\t> You would be in Seine.",
        "God, how long is a million years?\n\t> To me, it's about a minute.\n\t> God, how much is a million dollars?\n\t> To me, it's a penny.\n\t> God, may I have a penny?\n\t> Wait a minute.",
        "How can you make time fly?\n\t> Throw a clock out a window.",
        "What is the best way to get a math tutor?\n\t> An add."
    ]

    print(choice(logical_jokes))

    # Displayed LIST
    print(Formatted_Date)  #current date##
    print("Welcome to Jokes! Press 'n' to generate a logical joke, 'q' to exit, or 'a' to add a joke.")
    while True:
        user_Input = input("N/Q for Exit/A: ").lower() # OPTIONS AND IMPLEMENTED LOWER CASES
        if user_Input == "n":
            print(choice(logical_jokes))
        if user_Input == "q":
            break
        if user_Input == "a":
            user_Joke = input("Please Enter Your Joke:")  # Implementing and entering a joke if 'a'
            logical_jokes.append(user_Joke)      
            print("Updated List: ", logical_jokes)
    print("Thank you for using Jokes!") # Decided to implement to make it presentable

def random_joke():  #def key word you can create a function and give it a name. Without it is NOT A FUNCTION##
    # Dictionary of random jokes
    random_jokes = {
        'Why did the student wear glasses in math class?':'\n\t> To improve di-vision',         #left is KEY and right is VALUE###
        'Why did the obtuse angle jump in the pool?':'\n\t> Because it was over 90 degrees',
        'Why does algebra improve your dancing skills?':'\n\t> Because you can use algo-rhythm.',
        'What is a math teachers favorite place in NYC?':'\n\t> Times Square',
        'Do you know what seems odd to me?':'\n\t> Numbers that are not divisible by two',
        'Where should you do your math homework?':'\n\t> On a multiplication table',
        'Why do teens always travel in groups of three or five?':'\n\t> Because they can not even',                     ###DICTIONARIES ARE THE BOMB####
        'Why did seven eat nine?':'\n\t> Because you are supposed to eat three squared meals every day',                ####REMEMBER ALWAYS WITH CURLY BRACES###
        'Are monsters good at math?':'\n\t> Not unless you Count Dracula',
        'Did you know that there are three kinds of people in the world?':'\n\t> People who can count and people who can\'t',
        'What did the calculator say to the student?':'\n\t> You can always count on me',
        'What do you call a group of dudes who love math?':'\n\t> Alge-bros',
        'Do you know who invented algebra?':'\n\t> An x-pert',
        'Why was math class so long?':'\n\t> The teacher kept going off on a tangent',
        'Why did the two fours skip lunch?':'\n\t> They already eight',
        'Why do mathematicians like parks?':'\n\t> Because of all the natural logs',
        'Why don\'t math majors throw house parties?':'\n\t> Because it\'s dangerous to drink and derive'   ##left is KEY and right is VALUE###
    }

    # Displayed DICTIONARIES 
    print(Formatted_Date) #current date##
    print("Welcome to Jokes! Press 'n' to generate a random joke, 'q' to exit, or 'a' to add a joke.")
    while True:
        user_Input = input("N/Q for Exit/A: ").lower() #lower cases is easier for humans##
        if user_Input == "n":
            #created a function 'CHOSEN_JOKE'####
            chosen_joke = choice(list(random_jokes.keys()))  #method to retrieve the dictionary keys for example '.key' {key:new value}#
            print(chosen_joke)                               # key method gives the input from the left side of the colon(:)#  
            print(random_jokes[chosen_joke])                 # for example on line #56:'Why did the student wear glasses in math class?'#
                                                             # another example on line #71:'Why do mathematicians like parks?##
        if user_Input == "q":
            break
        if user_Input == "a":
            user_Joke = input("Please Enter Your Joke:")
            user_Answer = input("Why? ")
            random_jokes.update({user_Joke: user_Answer})     ##Remember:{Key is LEFT:VALUE IS RIGHT}
            print("Updated Dictionary: ", random_jokes)
    print("Thank you for using Jokes!")

# T & T Task

def tendai():
    compliments = [                              
        "U look good today.",
        "U look bad today.",
        "U look weird today.",
        "U look exhausted today.",
    ]

    print(choice(compliments))

# Organizer from Kerim
def Kerim():
            while True:
                # Welcome message
                print("\n"
                    "Welcome to the Holo-Orginazer!\n"
                    "\n"
                    "This is a Orginazer that creates a user-entered dated folder\n"
                    "for you to be prepared for your next week.\n"
                    "Enter a date from any monday(needs to be start of the week).\n"
                    "Within this folder it creates 5 Folder named: Mo - Fr.\n"
                    "Corrosponding with the fitting date u entered\n"
                    "\n"
                    "\n"
                    "1: Enter a Date for the Week.\n"
                    "2: Enter your Path.\n"
                    "3: Check out your path and you are ready to start the next week!\n")

                # Enter folder name as date
                main_folder_date = input('Enter a date from a week "05.06-09.06". (enter "q" to quit): ')
                if main_folder_date.lower() == "q":
                    break
                # Break the loop with "q" (exit programm)

                # User entered dates are stored as variables and split between each other with '.split(and the symbol)'
                start_date_var, end_date_var = main_folder_date.split("-")

                # Converts the first user entered name as date (start_date) into datetime and formats(parse time) with 'strptime' into string ("%days.%month")
                start_date = datetime.strptime(start_date_var, "%d.%m")
                # Converts the first user entered name as date (start_date) into datetime and formats(parse time) with 'strptime' into string ("%days.%month")
                end_date = datetime.strptime(end_date_var, "%d.%m")
                
                # Enter path where to create folder
                main_folder_path = input('Enter your path "/home/{username}/{folder}". (enter "q" to quit): ')
                if main_folder_path.lower() == "q":
                    break
                # Break the loop with "q" (exit programm)

                # Gives the folder the name (start.date)(strftime=convert to ("%d.%m")) + (Symbol = '-') + (end.date)(strftime=convert to ("%d.%m")) = (start-end)
                main_folder_name = start_date.strftime("%d.%m") + "-" + end_date.strftime("%d.%m")
                # Mix path and folder name together
                main_folder_path = os.path.join(main_folder_path, main_folder_name)
                
                # Create folder in your system thorugh 'os' module and 'mkdir' command
                os.mkdir(main_folder_path)

                # Returns the variable 'start_date' as an integer (monday=0)
                current_weekday = start_date.weekday()
                # (2)Substracts the variable 'start_date' from (1)a 'timedelta' object is created with the number of days set to 'current_weekday' (By performing this adjustment, the 'start_date' will represent the first day of the week (Monday) for the entered week, regardless of the initial day the user specified.)
                start_date = start_date - timedelta(days=current_weekday)
                # Calculate the dates within the specified variables ('start_date' added(+) to object 'timedelta'(with nr of 'days=' set to 'd' it will generate a new sequence for each iteration and represent the duration or difference of days for each one.) to calculate the range between 'end_date' minus(-) 'start_date' with '.days' given)
                dates = [start_date + timedelta(days=d) for d in range((end_date - start_date).days)]

                # for 'new_variable' in 'dates' from above it will create a specific sequence to create 5 folders(mo-fr) inside of 'main_folder_name'
                for date in dates:
                    # Converts the calculated 'date' variable and formats with 'strftime' into string ("%days.%month_%dayoftheweek")
                    sub_folder_name = date.strftime("%d.%m_%A")
                    # Mix the path and name together
                    sub_folder_path = os.path.join(main_folder_path, sub_folder_name)
                    # Creates the sub folder we calculated above through the module 'os' with command 'mkdir' into 'sub_folder_path'
                    os.mkdir(sub_folder_path)

                # Finished message
                print(f'Dated-Folder: "{main_folder_date}" created successfully in "{main_folder_path}".') 
                break
                # break the loop (exit) the programm after the code
    
# Call the main function to start the quiz
while True:
    show_menu()
    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        main_quiz_menu()
    elif user_choice == "2":
        second_quiz_menu_1()
    elif user_choice == "3":
        while True:
            tutorial_menu()
            user_choice_tutorial = input("Enter your choice: ")
            if user_choice_tutorial == "1":
                introduction()
            elif user_choice_tutorial == "2":
                variable_and_examples()
            elif user_choice_tutorial == "3":
                data_types_and_examples()
            elif user_choice_tutorial == "4":
                conditional_example()
            elif user_choice_tutorial == "5":
                loop_example()
            elif user_choice_tutorial == "6":
                function_example()
            elif user_choice_tutorial == "7":
                list_dict_example()
            elif user_choice_tutorial == "8":
                file_handling_example()
            elif user_choice_tutorial == "9":
                print_conclusion()
            elif user_choice_tutorial == "0":
                break
            else:
                 print("We are here 24/7")
    elif user_choice == "4":
        while True:
            jokes_menu()
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                love()
            elif user_choice == "2":
                random_joke()
            elif user_choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")# Call your own surprise feature function here    
    elif user_choice == "5":
        print(tendai())
        pass
    elif user_choice == "6":
        print(Kerim())
        break
    elif user_choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")