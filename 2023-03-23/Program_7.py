from argparse import ArgumentParser as Parser

parser = Parser('Program 7')

parser.add_argument('number', type=int)
args = parser.parse_args()

print(f'{args.number} + 2 = {args.number + 2}')