class SumOfTwoNumbers:
    no_1 = 0
    no_2 = 0

    def input_values(self):
        self.no_1 = int(input('Enter First no : '))
        self.no_2 = int(input('Enter Second no : '))

    def sum_of_two_numbers(self):
        return self.no_1 + self.no_2
    print('Sum : ',sum)


if __name__ == "__main__":
     obj = SumOfTwoNumbers()
     obj.input_values()
     obj.sum_of_two_numbers()