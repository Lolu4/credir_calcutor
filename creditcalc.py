import math
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--type', action='store', dest='type_cul', type=str)
parser.add_argument('--periods', action='store', default=0, type=float)
parser.add_argument('--interest', action='store', default=0,  type=float)
parser.add_argument('--principal', action='store', default=0,  type=float)
parser.add_argument('--payment', action='store', default=0,  type=float)
args = parser.parse_args()
argv = sys.argv
if args.periods < 0 or args.interest < 0 or args.principal < 0 or args.payment < 0 or len(argv) != 5:
    print('Incorrect parameters')
    exit()

if args.type_cul == 'annuity':
    i = args.interest / 100 / 12
    if args.periods == 0:
        args.periods = math.ceil(math.log((args.payment / (args.payment - i * args.principal)), 1 + i))
        if args.periods % 12 == 0:
            print('You need {} years to repay this credit!'.format(args.periods // 12))
        else:
            print('You need {} years and {} months to repay this credit!'.format(args.periods // 12, args.periods % 12))
        print('Overpayment = {0:.0f}'.format(math.ceil((args.payment * args.periods) - args.principal)))
    elif args.payment == 0:
        args.payment = args.principal * ((i * ((1 + i) ** args.periods)) / (((1 + i) ** args.periods) - 1))
        print('Your annuity payment = {}!'.format(math.ceil(args.payment)))
        print('Overpayment = {0:.0f}'.format(math.ceil((math.ceil(args.payment) * args.periods) - args.principal)))
    elif args.principal == 0:
        args.principal = args.payment / ((i * (1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1))
        print('Your credit principal = {}!'.format(math.floor(args.principal)))
        print('Overpayment = {0:.0f}'.format(math.ceil((args.payment * args.periods) - args.principal)))
elif args.type_cul == 'diff':
    payment_counter = 0
    i = args.interest / 100 / 12
    for m in range(1, int(args.periods) + 1):
        dif_payment = math.ceil((args.principal / args.periods) + i * (args.principal - ((args.principal * (m - 1)) / args.periods)))
        payment_counter += dif_payment
        m += 1
        print('Month {}: paid out {}'.format(m - 1, dif_payment))
    print('\nOverpayment = {0:.0f}'.format(payment_counter - args.principal))
