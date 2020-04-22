import numpy as np
import pandas as pd

import quandl
import datetime

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-darkgrid')
plt.rc('figure',figsize=(16,10))
data=quandl.get("CHRIS/MGEX_IH1", authtoken="k1EmQBi4HzoLswsDDyKz")


start_date = datetime.date(2005, 1,2) 
end_date = datetime.date.today() 
quandl.ApiConfig.api_key="k1EmQBi4HzoLswsDDyKz"

dato=quandl.get("CHRIS/MGEX_IH1",start_date=start_date,end_date=end_date)
dato.head()

dato.info
dato.describe()
dato.columns

dato.to_csv('dad.csv')