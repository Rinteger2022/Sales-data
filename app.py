import streamlit as st
import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
#if start_date < end_date:
 #   st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
#else:
  #  st.error('Error: End date must fall after start date.')

import requests
import pandas as pd
import os

bearer_token = os.environ.get('BEARER_TOKEN')
headers = {"Authorization": "Bearer {}".format(bearer_token)}

url = "https://72ab3c1c126c24365a51553f67e1db84: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@acelance.myshopify.com/admin/api/2022-01/orders/count.json?status=any&updated_at_min="start_date"&updated_at_max="end_date
response = requests.request("GET", url, headers=headers).json()
 
