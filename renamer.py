import os
import pathlib
import argparse


def flag_ok(value):
    return '\x1b[6;30;42m' + value + '\x1b[0m'


def main(folder_name, label_name, n_number):
    folder = folder_name
    label = label_name
    n = int(n_number)
    print("Start renaming..")
    for count, filename in enumerate(os.listdir(folder)):
        file_extension = pathlib.Path(filename).suffix
        dst = f"{str(label)}_{str(count).zfill(n)}{str(file_extension)}"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"
        print(dst, flag_ok("SAVED"))
        os.rename(src, dst)
    print("All executed..")


# Code Driver
if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-i", "--Input", help="Show Output")
    parser.add_argument("-l", "--Label", help="Show Output")
    parser.add_argument("-n", "--NumberPad", help="Show Output", default=3)

    # Read arguments from command line
    args = parser.parse_args()
    if args.Input and args.Label:
        main(args.Input, args.Label, args.NumberPad)
    else:
        print("python renamer.py -h")
