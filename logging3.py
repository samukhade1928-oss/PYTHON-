import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s-%(message)s")
logging.info("Program started")
def add(a,b):
    logging.info("Addition of two numbers")
    result=  a + b
    logging.info("Calculation Completed")
    return result
x= add(10,20)
print("Result",x)