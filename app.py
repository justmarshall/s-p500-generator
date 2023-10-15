import streamlit as st

#Title
st.title("S&P 500 Snippet Generator")

st.write("Generates the snippet for the S&P 500 snippet")
st.link_button("Yahoo Finance", "https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC")

price_at_close = st.number_input("S&P 500 Today's Closing Price", min_value=0.0)
yesterday_price = st.number_input("S&P 500 Yesterday's Price", min_value=0.0)
last_week_price = st.number_input("S&P 500 Last Week's Closing Price", min_value=0.0)

#Calculations
percent_change_day = ((price_at_close - yesterday_price)/yesterday_price) * 100
percent_change_week = ((price_at_close - last_week_price)/last_week_price) * 100
percent_change_market_low = ((price_at_close - 2237.40)/2237.40) * 100
percent_change_market_high = ((price_at_close - 4796.56)/4796.56) * 100

if percent_change_day >= 0: pc_day = "up +"
else: pc_day = 'down '

if percent_change_week >= 0: pc_week = "up +"
else: pc_week = 'down '

if price_at_close > 2237.40: pc_bear_market_low = "up +"
else: pc_bear_market_low = "down "

if price_at_close > 4796.56: pc_all_time_high = "up"
else: pc_all_time_high = "down "


#Snippet
st.write(f"The Standard & Poor’s 500 stock index closed Friday at {price_at_close:.2f}, {pc_day}{percent_change_day:.2f}% from Thursday, and {pc_week} {percent_change_week:.2f}% from a week ago. The index is {pc_bear_market_low}{percent_change_market_low:.2f}% from the March 23, 2020 bear market low and {pc_all_time_high}{percent_change_market_high:.2f}% from its January 3, 2022, all-time high") 

#Notes: Use a tool like https://www.soscisurvey.de/tools/view-chars.php to view any non-printable characters that are generating errors.