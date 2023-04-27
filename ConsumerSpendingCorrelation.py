import pandas as pd
import plotly.express as px

# Read in the two CSV files and filter out rows where either column contains "DataX" or "DataY"
gdp = pd.read_csv('GDP.csv').replace(['DataX', 'DataY'], pd.NA).dropna(subset=['GDP'])
spending = pd.read_csv('PCE.csv').replace(['DataX', 'DataY'], pd.NA).dropna(subset=['PCE'])
savingsRate = pd.read_csv("PSAVERT.csv").replace(['DataX', 'DataY'], pd.NA).dropna(subset=['PSAVERT'])

# Merge the two dataframes on the common date column
merged_df_GDP = pd.merge(gdp, spending,on='DATE')
merged_df_Savings = pd.merge(savingsRate, spending, on="DATE")
merged_df_GDP["Year"] = pd.to_datetime(merged_df_GDP['DATE']).dt.year
merged_df_Savings["Year"] = pd.to_datetime(merged_df_Savings['DATE']).dt.year
merged_df_savings_before2000 = merged_df_Savings[merged_df_Savings["Year"] < 2000]
merged_df_savings_after2000 = merged_df_Savings[merged_df_Savings["Year"] >= 2000]

# Calculate the correlation between the two columns
corrGDP = merged_df_GDP['GDP'].corr(merged_df_GDP['PCE'])
corrSavings = merged_df_Savings['PSAVERT'].corr(merged_df_Savings['PCE'])
corrSavingsB2000 = merged_df_savings_before2000['PSAVERT'].corr(merged_df_savings_before2000['PCE'])
corrSavingsA2000 = merged_df_savings_after2000['PSAVERT'].corr(merged_df_savings_after2000['PCE'])

color_scale = px.colors.sequential.Inferno
# Create a scatter plot with the two columns and the calculated correlation as the title
fig1 = px.scatter(merged_df_GDP, x='GDP', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending & GDP: {corrGDP}",
                 labels={'GDP': 'Gross Domestic Product', 'PCE': 'Personal Consumption Expenditures', 'DATE': 'Year'},
                 template="plotly_dark"

                  )
fig2 = px.scatter(merged_df_Savings, x='PSAVERT', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending and Personal Savings Rate: {corrSavings}",
                 labels={'PSAVERT': 'Personal Savings Rate', 'PCE': 'Personal Consumption Expenditures', 'DATE': 'Year'},
                 template="plotly_dark"
                  )

fig3 = px.scatter(merged_df_savings_before2000, x='PSAVERT', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending and Personal Savings Rate - Before 2000: {corrSavingsB2000}",
                 labels={'PSAVERT': 'Personal Savings Rate', 'PCE': 'Personal Consumption Expenditures', 'DATE': 'Year'},
                 template="plotly_dark"
                  )

fig4 = px.scatter(merged_df_savings_after2000, x='PSAVERT', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending and Personal Savings Rate - After 2000: {corrSavingsA2000}",
                 labels={'PSAVERT': 'Personal Savings Rate', 'PCE': 'Personal Consumption Expenditures', 'DATE': 'Year'},
                 template="plotly_dark"
                  )
# Show the plot
fig1.show()
# fig2.show()
# fig3.show()
# fig4.show()