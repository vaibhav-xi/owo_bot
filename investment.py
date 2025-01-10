def risk_amounts(initial_amount, max_tries):
    i = 1
    amounts = []
    
    amounts.append(initial_amount)
    
    while True:
        if i > max_tries:
            return amounts
        
        initial_amount = initial_amount * 2
        
        amounts.append(initial_amount)
        
        i += 1
    

def starting_amount(x, max_tries):
    
    # Calculate the sum of the geometric series: 2^10 - 1
    max_loss_factor = 2**max_tries - 1
    # Calculate the initial amount
    initial_amount = x // max_loss_factor
    return initial_amount

# Example usage
total_coins = 100000
max_tries = 10

initial_risk = starting_amount(total_coins, max_tries)
risk_list = risk_amounts(initial_risk, max_tries)

print(f"Initial amount: {initial_risk}")
print(f"Risk Amounts: {risk_list}")
