import glassdoor_scraper as gs
import pandas as pd


path = '/Users/batoolalmarzouq/Downloads/scrapy_project/Bioinformatics_jobs/chromedriver'

df = gs.get_jobs('Bioinformatician', 15, False, path, 15)

df.head(15)
