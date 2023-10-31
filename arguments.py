#!/usr/bin/env python3


import argparse
import subprocess



#  Check parameters passed to the script

 
parser = argparse.ArgumentParser(description="Run a command with a specified argument")
parser.add_argument("arg1", help="Argument to be passed to the command")
parser.add_argument("arg2", help="Argument to be passed to the command")
args = parser.parse_args()
 

safe_arg1 = subprocess.list2cmdline([args.arg1])
safe_arg2 = subprocess.list2cmdline([args.arg2])



# Run command with argument


def run_command(safe_args2):
    cmd = f"host {safe_arg2}"
    result = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout) 



match safe_arg1:

    case "H" | "h":
        print("Running host command...")
        run_command(safe_arg2)

    case "F" | "f":
        print("Do something")

    case "Java" | "java":
        print("You can become a mobile app developer")

    case _:
        print("The language doesn't matter, what matters is solving problems.")

 
