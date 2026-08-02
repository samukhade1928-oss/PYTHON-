class Simple:
    """
    
    Description : To take input from the user and Display on the screen
    Input : Accept the String from the user
    Output : Display the string
    Author : Samruddhi Khade
    Created on : 16/7/2026 11:02 
    """
    
    var_input = ' '#class variable

    def input_name(self):#snake_case
        """
        Args: i is input
        Return:No 
        """
        self.var_input=input('Enter the Name:')
    def show_name(self):
        print('Name is:',self.var_input)

if __name__ == "__main__":
    object = Simple()
    object.input_name()
    object.show_name()
