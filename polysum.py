
balance = 4773
annualInterestRate = 0.2

minMonthPay = 10
monthIntRate = annualInterestRate/12.0
testBal = balance
#for i in range(12): #The calc for the year
while testBal > 0:
    monthUnpBal = testBal - minMonthPay
    #The $10 payment - first on beginning balance,
    # in the loop on updated balance
    testBal = monthUnpBal + monthIntRate * monthUnpBal
    #Adding interest to the monthly balance, which is used in the \
    # line above for new calculations of the unpaid balance
    minMonthPay += 10
    print(testBal)
    print(minMonthPay)