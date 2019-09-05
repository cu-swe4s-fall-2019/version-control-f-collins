import argparse
import math_lib as ml


def main():
    parser = argparse.ArgumentParser(
            description='Program to add or divide two numbers.',
            prog='calculate')

    parser.add_argument('--operation',
                        type=str,
                        help='Supported options are add or divide.',
                        required=True)

    parser.add_argument('--num1',
                        type=float,
                        help='The first number, the numerator if divided.',
                        required=True)

    parser.add_argument('--num2',
                        type=float,
                        help='The second number, the denominator if divided.',
                        required=True)

    args = parser.parse_args()

    if(args.operation == 'add'):
        print(ml.add(args.num1, args.num2))
    elif(args.operation == 'divide'):
        print(ml.div(args.num1, args.num2))
    else:
        print('Unrecognized operation')
        parser.print_help()


if __name__ == '__main__':
    main()
