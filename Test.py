import argparse

def main():
    parser = argparse.ArgumentParser(description="Build Test")
    parser.add_argument('--source')
    
    args, unknown = parser.parse_known_args()

    print("Args parse ", parser.parse_known_args)

if __name__ == '__main__':
    print("Inside Test1")
    main()