import yfinance as yf
import pandas as pd

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
        
        # Drop all-NA columns from the portfolio DataFrame
        portfolio = portfolio.dropna(axis=1, how='all')
        
        # Concatenate the new stock DataFrame with the existing portfolio
        portfolio = pd.concat([portfolio, new_stock], ignore_index=True)
        print(f"Added {symbol} to portfolio.")


def remove_stock(symbol):
    global portfolio
    if symbol in portfolio['Symbol'].values:
        portfolio = portfolio[portfolio['Symbol'] != symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"Stock {symbol} not found in portfolio.")

def track_performance():
    global portfolio
    if portfolio.empty:
        print("Portfolio is empty.")
        return
    
    symbols = portfolio['Symbol'].tolist()
    data = yf.download(symbols, period='1d', group_by='ticker')
    
    total_value = 0
    print(portfolio)
    print("\nCurrent Portfolio Performance:")
    for symbol in symbols:
        if symbol in data.columns.get_level_values(0):
            stock_data = data[symbol]
            current_price = stock_data['Close'].iloc[-1]
            shares = portfolio[portfolio['Symbol'] == symbol]['Shares'].values[0]
            purchase_price = portfolio[portfolio['Symbol'] == symbol]['Purchase Price'].values[0]
            current_value = current_price * shares
            total_value += current_value
            print(f"Symbol: {symbol}, Current Price: ${current_price:.2f}, Shares: {shares}, Total Value: ${current_value:.2f}")
        else:
            print(f"Data for symbol {symbol} not found.")
    
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

def main():
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

if __name__ == "__main__":
    main()
