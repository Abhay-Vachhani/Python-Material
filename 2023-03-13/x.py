import argparse as ap

parser = ap.ArgumentParser(description='This is test')
parser.add_argument('no')
args = parser.parse_args()

print(args.no)