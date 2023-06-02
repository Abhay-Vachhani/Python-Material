from argparse import ArgumentParser as Parser
from sys import argv

parser = Parser('Program 6')

parser.add_argument('number', type=int)
parser.add_argument('string', type=str)
parser.add_argument('list', nargs='+')
args = parser.parse_args()

print(f'The name of file is {argv[0]} and its values are [{", ".join([f"{value}" for _, value in args._get_kwargs()])}]')