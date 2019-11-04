"""
Filename:convert.py
Converts infix expression to suffix expression
"""
from Stack.LinkedStack import LinkedStack

class convert_class(LinkedStack):
    """Define two types of popping method"""
    def __init__(self):
        LinkedStack.__init__(self)

    def usual_pop(self):
        """pop when meets '+'&&'-' """
        string=''
        while not self.isEmpty():
            if self._item.data=='(':
                break
            else:
                string=string+self.pop()+' '
        return string

    def prior_pop(self):
        """pop when meets '*'&&'/' """
        string=''
        while not self.isEmpty():
            if self._item.data=='(' or self._item.data=='+' or self._item.data=='-':
                break
            else:
                string=string+self.pop()+' '
        return string

def function(i,suffix_expression,stk):
    if i == '+' or i == '-':
        suffix_expression=suffix_expression + stk.usual_pop() + ' '
        return suffix_expression
    elif i == '*' or i == '/':
        suffix_expression=suffix_expression + stk.prior_pop() + ' '
        return suffix_expression
    else:
        while stk.peek()!='(':
            suffix_expression = suffix_expression + stk.pop() + ' '
        stk.pop()
        return suffix_expression

def convert(infix_expression):
    operator = ['+', '-', '*', '/','(']
    infix_expression=infix_expression.split()
    suffix_expression=''
    stk=convert_class()

    for i in infix_expression:
        if i in operator:
            if i=='(':
                stk.push(i)
            elif stk.isEmpty():
                stk.push(i)
            else:
                suffix_expression=function(i,suffix_expression,stk)
                stk.push(i)
        elif i==')':
            suffix_expression=function(i,suffix_expression,stk)
        else:
            suffix_expression=suffix_expression+i+' '

    while not stk.isEmpty():
        if stk.peek()!='(':
            suffix_expression =suffix_expression+stk.pop()+' '
        else:stk.clear()
    return suffix_expression


if __name__=='__main__':
    a=' ( 4 + 5 )  * ( 6 - 3 ) + ( 3 * 2 + 10 ) '
    b=convert(a)
    print(b)







