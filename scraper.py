import glassdoor_scraper as gs
import pandas as pd
import sys

path = '/Users/batoolalmarzouq/Downloads/scrapy_project/Bioinformatics_jobs/chromedriver'

df = gs.get_jobs('Bioinformatics', 2000, False, path, 60)

print(df.head(15))

df.to_csv(r'usa_dataframe.csv', index=True, header=True)

df.head().to_csv(sys.stdout)
