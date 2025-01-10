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
print(f"Initial amount: {initial_risk}")
