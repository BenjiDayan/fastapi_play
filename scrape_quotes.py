# json requests
import requests
# Beautiful Soup
from bs4 import BeautifulSoup
# Pandas
import pandas as pd
from tqdm import tqdm

# URL
url = 'http://www.quotationspage.com/quote/{i}.html'

# Empty list to store data
quotes = []

outfile = 'output.csv'
df = pd.DataFrame(quotes, columns=['quote', 'author', 'author_extra'])
df.to_csv(outfile, sep='^', index=False)

# Loop through 1-100
for i in tqdm(range(1, 20)):
    # Get request
    r = requests.get(url.format(i=i))
    # Parse HTML
    soup = BeautifulSoup(r.text, 'html.parser')
    # Get quote
    quote = soup.find('dt').text
    if quote == 'ERROR: No such quotation number.':
        continue
    # Get author
    try:
        author = soup.find('dd').a.text
        author_extra = soup.find('dd').i.text
    except Exception:
        continue
    # actually split by bits inside text

    # Append to list
    quotes.append((quote, author, author_extra))
    # write df row
    row = [quote, author, author_extra]
    row_df = pd.DataFrame([row], columns=['quote', 'author', 'author_extra'])
    row_df.to_csv(outfile, index=False, sep='^', mode='a', header=False)
