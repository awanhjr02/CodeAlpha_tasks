import yfinance as yf         #library used to fetch real-time financial data
import pandas as pd           # Python library for data manipulation and analysis

# Initialize an empty DataFrame to store portfolio
portfolio = pd.DataFrame(columns=['Symbol', 'Shares', 'Purchase Price'])

def add_stock(symbol, shares, purchase_price):
    """Add a stock to the portfolio."""
    global portfolio
    
    # Check if stock already exists
    if symbol in portfolio['Symbol'].values:
        print(f"Stock {symbol} already in portfolio.")
    else:
        # Create a new DataFrame with the new stock data
        new_stock = pd.DataFrame({'Symbol': [symbol], 'Shares': [shares], 'Purchase Price': [purchase_price]})
        
        # Drop all-NA columns from the new_stock DataFrame
        new_stock = new_stock.dropna(axis=1, how='all')
        
        # Concatenate the new stock DataFrame with the existing portfolio
        portfolio = pd.concat([portfolio, new_stock], ignore_index=True)
        print(f"Added {symbol} to portfolio.")




def remove_stock(symbol):
    """Remove a stock from the portfolio."""
    global portfolio
    # Check if stock exists
    if symbol in portfolio['Symbol'].values:
        portfolio = portfolio[portfolio['Symbol'] != symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"Stock {symbol} not found in portfolio.")

def track_performance():
    """Track and display the performance of the portfolio."""
    global portfolio
    if portfolio.empty:
        print("Portfolio is empty.")
        return
    
    # Fetch real-time data
    symbols = portfolio['Symbol'].tolist()
    data = yf.download(symbols, period='1d', group_by='ticker')
    
    # Calculate current value of the portfolio
    total_value = 0
    print(portfolio)
    print("\nCurrent Portfolio Performance:")
    for symbol in symbols:
        if symbol in data.columns.get_level_values(0):  # Check if data for the symbol is available
            stock_data = data[symbol]
            current_price = stock_data['Close'][-1]
            shares = portfolio[portfolio['Symbol'] == symbol]['Shares'].values[0]
            purchase_price = portfolio[portfolio['Symbol'] == symbol]['Purchase Price'].values[0]
            current_value = current_price * shares
            total_value += current_value
            print(f"Symbol: {symbol}, Current Price: ${current_price:.2f}, Shares: {shares}, Total Value: ${current_value:.2f}")
        else:
            print(f"Data for symbol {symbol} not found.")
    
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")



def main():
    """Main function to interact with the user."""
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL,DG): ").upper()
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price per share: "))
            add_stock(symbol, shares, purchase_price)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove (e.g., AAPL): ").upper()
            remove_stock(symbol)
        elif choice == '3':
            track_performance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# It is only executed when the script is run directly,not without importing  a module
# It is best for creating scripts that are both executable and importable.
if __name__ == "__main__":
    main()

