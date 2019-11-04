"""
Filename:calculate.py
Convert an infix expression to a suffix expression and calculate it.
"""
from Calculate_arithmetic_expressions.convert import convert
from Calculate_arithmetic_expressions.calculating_suffix_expression import calculating_suffix_expression

def calculate(string):
    converted_string=convert(string)
    result=calculating_suffix_expression(converted_string)
    return result

if __name__=='__main__':
    string=input('please input expression:')
    result=calculate(string)
    print('The result is :{}'.format(result))
