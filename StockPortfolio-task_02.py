# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 310,
    "TSLA": 250,
    "AMZN": 120
}

# Dictionary to store user's stock holdings
user_portfolio = {}

print("Welcome to the Stock Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from the available list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity must be non-negative.")
            continue
        user_portfolio[stock] = user_portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in user_portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optionally save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as file:
        file.write("Investment Summary:\n")
        for stock, qty in user_portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Summary saved to 'investment_summary.txt'.")
