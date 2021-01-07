import argparse

parser = argparse.ArgumentParser(description='Personal information')
parser.add_argument('-token', dest='token', type=str, help='Name of the candidate')

args = parser.parse_args()
print(args.token)

if args.token is None:
    print("token is none")


