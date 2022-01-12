import streamlit as st
import datetime
import timedelta
from datetime import datetime,timedelta
import requests
import pandas as pd
import os


today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date')
end_date = st.date_input('End date')
#if start_date < end_date:
 #   st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
#else:
  #  st.error('Error: End date must fall after start date.')

currentTimeDate = end_date - timedelta(days=1)
currentTime = currentTimeDate.strftime('%Y-%m-%d')
st.write(currentTime)


#a=end_date + timedelta(days = 1)
bearer_token = os.environ.get('BEARER_TOKEN')
headers = {"Authorization": "Bearer {}".format(bearer_token)}
url_1="https://72ab3c1c126c24365a51553f67e1db84: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@acelance.myshopify.com/admin/api/2022-01/orders/count.json?status=any&created_at_min="+str(start_date)
url_2=url_1+"&created_at_max="+str(currentTime)
url = url_2
response = requests.request("GET", url, headers=headers).json()

if start_date <= end_date:
 st.write(response)
 st.write(url)
# a=url.json()["count"]
 #st.write(str(a))


