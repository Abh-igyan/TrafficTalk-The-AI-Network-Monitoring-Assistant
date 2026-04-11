import argparse
from agentic import agent

parser = argparse.ArgumentParser()
parser.add_argument("--query", type=str, default="top interfaces")
parser.add_argument("--interval", type=int, default=5)
parser.add_argument("--top", type=int, default=5)

args = parser.parse_args()

result = agent(args.query, args.interval, args.top)

print("\n" + result)