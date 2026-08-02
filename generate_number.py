class SequenceGenerator:
    
    def no_generator(self , start):
        for i in range(start,100):
            print(i, end=" ")

    def input_start(self):
        start_no= int(input('Enter start no: '))
        self.no_generator(start=start_no)


if __name__ == "__main__":
    object = SequenceGenerator()
    object.input_start()
