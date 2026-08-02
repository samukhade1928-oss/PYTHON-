class SimpleConstructor:

    def __init__(self,name):#constructor
        self.name= name
    def show_name(self):
        print('Name is:',self.name)

if __name__ == "__main__":
    object = SimpleConstructor('Samruddhi')
    object.show_name()