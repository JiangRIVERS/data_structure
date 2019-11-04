"""
Filename:calculate_function
Convert string operator to real operator
"""
def calculate_function(string,operand1,operand2):
    """Raises KeyError if the string operator not in string list"""
    string_list=['+','-','*','/']
    if string not in string_list:
        raise KeyError('We can\'t deal with this operator')
    elif string=='+':
        return operand2+operand1
    elif string=='-':
        return operand2-operand1
    elif string=='*':
        return operand2*operand1
    elif string=='/':
        return operand2/operand1
