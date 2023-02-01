import argparse
parser = argparse.ArgumentParser()
parser.add_argument("arg_2")
parser.add_argument("arg_1")
args = parser.parse_args()
arg1 = args.arg_1
arg2 = args.arg_2
print(arg1)
print(arg2)

