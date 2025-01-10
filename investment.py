def risk_amounts(total_coins, initial_risk, max_tries):
    i = 1
    amounts = []
    
    while total_coins > 0 and i <= max_tries:
        if initial_risk > total_coins:
            break
        
        amounts.append(initial_risk)
        total_coins -= initial_risk
        
        if total_coins > 0:
            initial_risk *= 2
        
        i += 1
    
    return amounts


def starting_amount(x, max_tries):
    
    # Calculate the sum of the geometric series: 2^max_tries - 1
    max_loss_factor = 2**max_tries - 1
    
    # Calculate the initial amount
    initial_risk = x // max_loss_factor
    return initial_risk


# Example usage
total_coins = 100000
max_tries = 10

initial_risk = starting_amount(total_coins, max_tries)
risk_list = risk_amounts(total_coins, initial_risk, max_tries)

print(f"Initial amount: {initial_risk}")
print(f"Risk Amounts: {risk_list}")
