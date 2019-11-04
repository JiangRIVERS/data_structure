"""
Filename:erapp.py
The view of an emergency room scheduler
"""

from Queue.hospitalmodel import ERModel,Patient,Condition

class ERview(object):
    """The view class for the ER application"""
    def __init__(self,model):
        self._model=model

    def run(self):
        """Menu-driven command loop for app"""
        menu="\n"+\
            "Main menu\n"+\
             " 1 Schedule a patient\n"+ \
             " 2 Treat the next patient\n" +\
             " 3 Treat all patients\n" +\
             " 4 Exit the program\n"

        while True:
            command=self._getCommand(4,menu)
            if command==1:self._schedule()
            elif command==2:self.treatNext()
            elif command==3:self.treatAll()
            else:break

    def _schedule(self):
        """Obtains patient info and schedules patient"""
        name=input("\nEnter the patient's name")
        condition=self._getCondition()
        self._model.add(Patient(name,condition))
        print(name,"is added to the ",str(condition)," list\n")

    def _getCondition(self):
        """Obtains condition info"""
        menu="Patient's condition\n"+\
             " 1 Critical\n"+ \
             " 2 Serious\n" + \
             " 3 Fair\n"
        condition=self._getCommand(3,menu)
        return Condition(condition)

    def treatNext(self):
        """Treats one patient if there is one"""
        if self._model.isEmpty():
            print("No patient available to treat")
        else:
            patient=self._model.pop()
            print(patient._name+" is being treated")

    def treatAll(self):
        if self._model.isEmpty():
            print("No patient available to treat")
        while not self._model.isEmpty():
            self.treatNext()

    def _getCommand(self,high,menu):
        """Obtains and returns a command number"""
        prompt="Enter a number from 1 to "+str(high)
        commandRange=list(map(str,range(1,high+1)))
        error="Error,number must be 1 to "+str(high)
        while True:
            print(menu)
            command=input(prompt)
            if command in commandRange:
                return int(command)
            else:
                print(error)


def main():
    model=ERModel()
    view=ERview(model)
    view.run()

if __name__=='__main__':
    main()