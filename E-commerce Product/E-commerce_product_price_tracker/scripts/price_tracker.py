import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

product_url = 'https://www.amazon.in/dp/B0CCP9RSG9/ref=AF_WIN_bub_w_cml_t_4?pf_rd_r=CA4GEBVGGHP84XCQYCFE&pf_rd_p=53cd3974-ac8c-4375-85ed-2d5c1e79b14f&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_t=&pf_rd_i=1375424031&th=1'
desired_price = 60000.00
EMAIL_ID = 'youremail@example.com'
PASSWORD = 'yourgeneratedpassword'  # Write App Generate Password

def check_price():
    response = requests.get(product_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    soup = BeautifulSoup(response.content, "html.parser")
    price_tag = soup.find('span', {'class': 'a-price-whole'})
    price_str = price_tag.get_text()
    price_str = price_str.replace('₹', '').replace(',', '').strip()
    current_price = float(price_str)
    return current_price

def notify(current_price):
    server = SMTP("smtp.gmail.com", 587)
    server.starttls()  # tls - transport layer security
    server.login(EMAIL_ID, PASSWORD)
    subject = 'Price Drop Alert!'
    body = f'The price of the product has dropped to ₹{current_price}. Check the link: {product_url}'
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(EMAIL_ID, EMAIL_ID, msg)
    server.quit()

current_price = check_price()
if current_price <= desired_price:
    notify(current_price)
