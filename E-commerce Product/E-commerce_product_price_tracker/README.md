# Ecommerce Product Price Tracker

This project involves tracking the price of a specific product on Amazon and sending an email notification when the price drops below a desired amount.

## Project Overview

The project performs the following steps:

1. **Fetch Product Price**:
   - Scrapes the product price from the provided Amazon product URL using the BeautifulSoup library.

2. **Check Price**:
   - Compares the current price with the desired price.

3. **Send Notification**:
   - Sends an email notification if the current price is lower than the desired price.

## Requirements

Ensure you have the following Python libraries installed:
- requests
- beautifulsoup4
- smtplib

You can install the required libraries using the following command:
```bash
pip install -r requirements.txt


## Usage

1. Clone the repository and navigate into the `ecommerce_product_price_tracker` directory.
2. Ensure you have Python and the required libraries installed.
3. Update the `product_url`, `desired_price`, `EMAIL_ID`, and `PASSWORD` in the `scripts/price_tracker.py` file.
4. Run the script to check the price and send notifications.

```bash
python scripts/price_tracker.py
