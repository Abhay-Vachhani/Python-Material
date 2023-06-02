from argparse import ArgumentParser as Parser

parser = Parser('Program 5')

parser.add_argument('Number', type=int)
parser.add_argument('String', type=str)
parser.add_argument('List', nargs='+')
args = parser.parse_args()

[print(f'{key}: {value}') for key, value in args._get_kwargs()]