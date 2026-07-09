#Scraping Basics - Requests + BeautifulSoup

import requests
from bs4 import BeautifulSoup 

html_sample = """
<html>
<body>
  <table id="pricing-table">
    <thead>
      <tr><th>Product</th><th>Price</th><th>Stock</th></tr>
    </thead>
    <tbody>
      <tr><td class="prod-name">Wireless Mouse</td><td class="prod-price">$24.99</td><td>In Stock</td></tr>
      <tr><td class="prod-name">USB-C Hub</td><td class="prod-price">$39.99</td><td>Low Stock</td></tr>
      <tr><td class="prod-name">Mechanical Keyboard</td><td class="prod-price">$89.99</td><td>In Stock</td></tr>
    </tbody>
  </table>
</body>
</html>
"""

soup = BeautifulSoup(html_sample, 'html.parser')

table = soup.find('table', id = 'pricing-table')
rows = table.find('tbody').find_all('tr')

data = []

for row in rows:
    cells = row.find_all('td')
    data.append({
        'Product': cells[0].text.strip(),
        'Price': cells[1].text.strip(),
        'Stock': cells[2].text.strip()
        })


for item in data:
    print(item)
