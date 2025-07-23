from ModelBuilder.model import Model
from ModelBuilder.tester import Tester
from userInput import UserInput

def drop_column_fun():
   drop_column = input("Would you like to remove any columns that are maybe not compatible values (y/n)")
   if drop_column not in ('y', 'n'):
       print("That was not an option, try again")
       return drop_column_fun()
   elif drop_column == 'n':
       return None
   else:
       amount = int(input("How many"))
       if amount == 1:
           column = input("What column")
       else:
           print("put a comma between columns")
           column = list(input("what columns").split(","))
   return column
def menu():
    print("Welcome to the program")
    path = input("What is the path to the CSV file")
    classifier = input("What is the name of the column that you would like to receive the info on")
    columns_to_drop = drop_column_fun()
    try:
        model = Model(path, classifier, columns_to_drop)
        test = Tester(model)
        if test.test() >= 0.9:
            ui = UserInput(model)
            print (f"The answer to you query is: {ui.probability()}")
        else:
            print( "Your dataset is not big enough, did not pass test")
    except:
        print( "Un-valid model")
if __name__ == '__main__':
    menu()


