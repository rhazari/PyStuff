import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x', type=float, default = 1.0, 
						help='The first number')
	parser.add_argument('--y', type=float, default = 1.0, 
						help='The second number')
	parser.add_argument('--operator', type=str, default = 'add', 
						help='The operation to perform (add, sub, mul, div)')

	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))

def calc(args):
	operator = args.operator
	if(operator == 'add'):
		return args.x+args.y
	elif(operator == 'sub'):
		return args.x-args.y
	elif(operator == 'mul'):
		return args.x*args.y
	elif(operator == 'div'):
		return args.x/args.y

if __name__ == '__main__':
	main()