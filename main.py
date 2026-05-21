import argparse

parser = argparse.ArgumentParser(description="A script with a optional flags")

parser.add_argument("v", "--verbose", action="store_true", help="Turn on verbose logging")
parser.add_argument("-o", "--output", type=str, default="log.txt", help="Output file path")

args = parser.parse_args()

if args.verbose:
  print(f"Verbose mode active. Saving results to: {args.output}")