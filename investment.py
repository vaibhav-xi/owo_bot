def parse_amount(input_string):
    """Parse and validate"""
    try:
        return int(input_string.replace(",", "").replace(".", ""))
    except ValueError:
        return None


def risk_amounts(total_coins, initial_risk, max_tries):
    """Calculate risk amounts"""
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
    """Calculate initial risk"""
    max_loss_factor = 2**max_tries - 1
    return x // max_loss_factor


def main():
    max_tries = 5 
    
    while True:
        total_amount = input("Enter total coins (or type 'exit' to quit): ")
        
        if total_amount.lower() == "exit":
            print("Goodbye!")
            break
        
        # validate the input
        total_coins = parse_amount(total_amount)
        if total_coins is None:
            print("Invalid input")
            continue
        
        # calculations
        initial_risk = starting_amount(total_coins, max_tries)
        risk_list = risk_amounts(total_coins, initial_risk, max_tries)
        
        # results
        print(f"\nTotal Coins: {total_coins:,}")
        print(f"Initial Risk: {initial_risk:,}")
        print(f"Risk Amounts: {', '.join(map(str, risk_list))}\n")

if __name__ == "__main__":
    main()
