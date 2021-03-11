from math import ceil, log, floor
import argparse

parser = argparse.ArgumentParser(description='Calculates mortgage data')
parser.add_argument("--type", choices=["annuity", "diff"], )
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
payment_type = args.type
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest

if payment_type is None or (payment_type == "diff" and payment is not None) or (
        len(vars(args)) < 5) or interest is None:
    print("Incorrect parameters")

elif (payment is not None and payment < 0) or (principal is not None and principal < 0) or (
        periods is not None and periods < 0) or (interest < 0):
    print("Incorrect parameters")

elif payment_type == "diff":
    nominal_interest = interest / (12 * 100)
    payments = []
    total_payments = 0
    for i in range(1, periods + 1):
        payments.append(
            ceil((principal / periods) + nominal_interest * (principal - ((principal * (i - 1)) / periods))))
        total_payments += payments[i - 1]
        print("Month {}: payment is {}".format(i, payments[i - 1]))
    overpayment_diff = int(total_payments - principal)
    print("\nOverpayment = {}".format(overpayment_diff))

elif payment_type == "annuity":
    nominal_interest = interest / (12 * 100)
    if payment is None:
        monthly_payment = ceil(principal * ((nominal_interest * ((1 + nominal_interest) ** periods)) / (
                    ((1 + nominal_interest) ** periods) - 1)))
        overpayment_annuity = int((monthly_payment * periods) - principal)
        print('Your monthly payment = {}!'.format(monthly_payment))
        print('Overpayment = {}'.format(overpayment_annuity))
    elif principal is None:
        loan_principal = payment / ((nominal_interest * ((1 + nominal_interest) ** periods)) / (
                    ((1 + nominal_interest) ** periods) - 1))
        overpayment_annuity = int((payment * periods) - loan_principal)
        print('Your loan principal = {}!'.format(floor(loan_principal)))
        print('Overpayment = {}'.format(overpayment_annuity))
    elif periods is None:
        total_months = ceil(log((payment / (payment - nominal_interest * principal)), (1 + nominal_interest)))
        overpayment_annuity = int((payment * total_months) - principal)
        num_years = floor(total_months / 12)
        num_months = total_months % 12
        if num_years == 0:
            print('It will take {} months to repay this loan!'.format(num_months))
        elif num_months == 0:
            print('It will take {} years to repay this loan!'.format(num_years))
        else:
            print('It will take {} years and {} months to repay this loan!'.format(num_years, num_months))
        print("Overpayment = {}".format(overpayment_annuity))
# print("What do you want to calculate?")
# print('type "n" for number of monthly payments')
# print('type "a" for annuity monthly payment amount')
# print('type "p" - for the loan principle:')
# calculation_choice = input()
# calculation_choice = None
# if calculation_choice == 'n':
#     print('Enter the loan principal')
#     principal = float(input())
#     print('Enter the monthly payment:')
#     monthly_payment = float(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#     nominal_interest = (loan_interest) / (12 * 100)
#     total_months = ceil(
#         log((monthly_payment / (monthly_payment - nominal_interest * principal)), (1 + nominal_interest)))
#     num_years = floor(total_months / 12)
#     num_months = total_months % 12
#     if num_years == 0:
#         print('It will take {} months to repay this loan!'.format(num_months))
#     else:
#         print('It will take {} years and {} months to repay this loan!'.format(num_years, num_months))
#
# elif calculation_choice == 'a':
#     print('Enter the loan principal:')
#     principal = float(input())
#     print('Enter the number of periods:')
#     loan_periods = int(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#     nominal_interest = (loan_interest) / (12 * 100)
#     monthly_payment = ceil(principal * ((nominal_interest * ((1 + nominal_interest) ** loan_periods)) / (
#                 ((1 + nominal_interest) ** loan_periods) - 1)))
#     print('Your monthly payment = {}!'.format(monthly_payment))
#
#
# elif calculation_choice == 'p':
#     print('Enter the annuity payment:')
#     monthly_payment = float(input())
#     print('Enter the number of periods:')
#     loan_periods = int(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#     nominal_interest = (loan_interest) / (12 * 100)
#     loan_principal = monthly_payment / ((nominal_interest * ((1 + nominal_interest) ** loan_periods)) / (
#                 (((1 + nominal_interest) ** loan_periods)) - 1))
#     print('Your loan principal = {}!'.format(floor(loan_principal)))
