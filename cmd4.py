#passing arguments
#ip - name, roll no
#op - name, roll no
#sys.argv[0] is u r program name

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--rollno", required=True)

args = parser.parse_args()

print("Name :", args.name)
print("Roll no :", args.rollno)

