import requests

def get_crypto_prices():
    # CoinGecko free public API endpoint
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # Query parameters: requesting BTC, ETH, and DOGE prices in USD & INR
    params = {
        "ids": "bitcoin,ethereum,dogecoin",
        "vs_currencies": "usd,inr"
    }

    try:
        print("Fetching live cryptocurrency data...")
        response = requests.get(url, params=params, timeout=10)

        # Check if HTTP status code is 200 (Success)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        print("\n==================================")
        print("      LIVE CRYPTO PRICES         ")
        print("==================================")

        for coin, prices in data.items():
            coin_name = coin.capitalize()
            usd_price = prices.get("usd", "N/A")
            inr_price = prices.get("inr", "N/A")

            print(f"Coin: {coin_name}")
            print(f"  - Price (USD): ${usd_price:,.2f}")
            print(f"  - Price (INR): ₹{inr_price:,.2f}")
            print("-" * 34)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the internet or API server!")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again later.")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    except KeyError:
        print("Error: Could not parse response data.")

if __name__ == "__main__":
    get_crypto_prices()