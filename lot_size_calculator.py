#This will be to calculate Lot sizes

#Constants to be manually changed fpor ease

account_size = float(100_000) #account size $50,000 USD
risk_decimal = float(0.01)  #0.01 represents 1% risk
stop_lost_pips = float(input('What is the stop loss in pips?: '))


#Result to be outputted
amount_at_risk = account_size * risk_decimal
lots_needed = amount_at_risk/stop_lost_pips/10

#Print statements that output results
print('Amount at risk: ',amount_at_risk)
print('Amount of lots needed: ',round(lots_needed,3))
