"""
Filename:Calculating_suffix_expression
While there are more tokens in the expression
    Get the next token
    If the token is an operand
        push the operand onto the stack
    Else if the token is an operator
        Pop the top two operands from the stack
        Apply the operator to the two operands just popped
        Push the resulting value onto the stack
    Return the value at the top of the stack
"""
from Stack.LinkedStack import LinkedStack
from Calculate_arithmetic_expressions.calculate_function import calculate_function

def calculating_suffix_expression(exp):
    """
    exp is a string that represents the expression
    operand:numbers
    operator:['+','-','*','/']
    """
    operator=['+','-','*','/']
    stk=LinkedStack()
    for i in exp.split():
        if i in operator:
            operand1=stk.pop()
            operand2=stk.pop()
            newoperand=calculate_function(i,operand1,operand2)
            stk.push(newoperand)
        else:
            stk.push(int(i))
    return stk.pop()
