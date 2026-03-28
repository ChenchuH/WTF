import argparse
import sys
import rich

def parse_args():
    parser = argparse.ArgumentParser(prog="wtf", description="A CLI tool that takes error messages and describes the problem in plain english")
    parser.add_argument("error_msg", nargs="*", help="error message")

    return parser.parse_args()



def main():
    try:
       args=parse_args()

       error_msg = " ".join(args.error_msg)
       print(error_msg)


    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")

if __name__=="__main__":
    main()