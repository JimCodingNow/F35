import argparse

def main():
    parser = argparse.ArgumentParser(description="Build Test")
    parser.add_argument('--source')
    parser.add_argument('--update')
    
    args, unknown = parser.parse_known_args()

    print("Args parse ", args.source)
    print("Args parse update", args.update)

if __name__ == '__main__':
    print("Inside Test1")
    main()