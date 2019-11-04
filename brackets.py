"""
File:brackets.py
Check expression for matching brackets
1.Scan the whole expression and push starting brackets to a stack.
2.When meeting a ending brackets,if the stack is empty or the top element of the stack is not the same type to the ending
  brackets,returns not matching.
3.Pop the top element of the stack if it is the same type to the ending brackets.Continue to scan the expression.
4.When reaching the end of the expression the stack should be empty and if it isn't,returns not matching.
"""
from Stack.LinkedStack import LinkedStack

def bracketsBalance(exp):
    """exp is a string the represents the expression"""
    stk=LinkedStack()
    standary={'(','['}
    invertstandary=[')',']']
    for ch in exp:
        if ch in standary:
            stk.push(ch)
        elif ch in invertstandary:
            if stk.isEmpty():
                return 'not matching'
            chFromStack=stk.pop()
            if (ch==')' and chFromStack!='(') or \
                    (ch==']'and chFromStack!='['):
                return 'not matching'
    if stk.isEmpty():
        return 'matching'
    else:return 'not matching'

def main():
    exp=input('Enter a bracketed expression:')
    print(bracketsBalance(exp))

if __name__=='__main__':
    main()

