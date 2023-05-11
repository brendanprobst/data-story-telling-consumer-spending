import pandas as pd
import plotly.express as px

# Read in the two CSV files and filter out rows where either column contains "DataX" or "DataY"
gdp = pd.read_csv('GDP_old.csv').replace(['DataX', 'DataY'], pd.NA).dropna(subset=['GDP'])
spending = pd.read_csv('PCE_old.csv').replace(['DataX', 'DataY'], pd.NA).dropna(subset=['PCE'])
savingsRate = pd.read_csv("PSAVERT.csv").replace(['DataX', 'DataY'], pd.NA).dropna(subset=['PSAVERT'])
disposableIncome = pd.read_csv("real_disposable_personal_income.csv").replace(['DataX', 'DataY'], pd.NA).dropna(subset=['DISP_INCOME'])
employmentLevel = pd.read_csv("employment_level.csv").replace(['DataX', 'DataY'], pd.NA).dropna(subset=['EMP_LEV'])

# Merge the two dataframes on the common date column
merged_df_GDP = pd.merge(gdp, spending, on='DATE')
merged_df_Savings = pd.merge(savingsRate, spending, on="DATE")
merged_df_GDP["Year"] = pd.to_datetime(merged_df_GDP['DATE']).dt.year
merged_df_Savings["Year"] = pd.to_datetime(merged_df_Savings['DATE']).dt.year
merged_df_savings_before2000 = merged_df_Savings[merged_df_Savings["Year"] < 2000]
merged_df_savings_after2000 = merged_df_Savings[merged_df_Savings["Year"] >= 2000]
merged_df_disp_income = pd.merge(disposableIncome, spending, on="DATE")
merged_df_disp_income["Year"] = pd.to_datetime(merged_df_disp_income['DATE']).dt.year
merged_df_EmploymentLevel = pd.merge(employmentLevel,spending, on="DATE")
merged_df_EmploymentLevel["Year"] = pd.to_datetime(merged_df_disp_income['DATE']).dt.year
# Calculate the correlation between the two columns
corrGDP = merged_df_GDP['GDP'].corr(merged_df_GDP['PCE'])
corrSavings = merged_df_Savings['PSAVERT'].corr(merged_df_Savings['PCE'])
corrSavingsB2000 = merged_df_savings_before2000['PSAVERT'].corr(merged_df_savings_before2000['PCE'])
corrSavingsA2000 = merged_df_savings_after2000['PSAVERT'].corr(merged_df_savings_after2000['PCE'])
corrDispIncome = merged_df_disp_income["DISP_INCOME"].corr(merged_df_disp_income["PCE"])
corrEmployment = merged_df_EmploymentLevel["EMP_LEV"].corr(merged_df_EmploymentLevel["PCE"])
color_scale = px.colors.sequential.Inferno
# Create a scatter plot with the two columns and the calculated correlation as the title
fig1 = px.scatter(merged_df_GDP, x='GDP', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending & GDP: {corrGDP}",
                 labels={'GDP': 'Gross Domestic Product (Billion $USD)', 'PCE': 'Personal Consumption Expenditures (Billion $USD)', 'DATE': 'Year'},
                 template="plotly_dark"

                  )
fig2 = px.scatter(merged_df_Savings, x='PSAVERT', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending and Personal Savings Rate: {corrSavings}",
                  labels={'PSAVERT': 'Personal Savings Rate (% of Income)',
                          'PCE': 'Personal Consumption Expenditures (Billion USD$)', 'DATE': 'Year'},
                  template="plotly_dark"

                  )

fig3 = px.scatter(merged_df_savings_before2000, x='PSAVERT', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending and Personal Savings Rate - Before 2000: {corrSavingsB2000}",
                  labels={'PSAVERT': 'Personal Savings Rate (% of Income)',
                          'PCE': 'Personal Consumption Expenditures  (Billion USD$)', 'DATE': 'Year'},
                  template="plotly_dark"
                  )

fig4 = px.scatter(merged_df_savings_after2000, x='PSAVERT', y='PCE', color='Year',
                 title=f"Correlation between Consumer Spending and Personal Savings Rate - After 2000: {corrSavingsA2000}",
                 labels={'PSAVERT': 'Personal Savings Rate (% of Income)', 'PCE': 'Personal Consumption Expenditures (Billion USD$)', 'DATE': 'Year'},
                 template="plotly_dark"
                  )



fig5 = px.scatter(merged_df_disp_income, x='DISP_INCOME', y='PCE', color='DATE',
                 title=f"Correlation between Consumer Spending and Real Disposable Income: {corrDispIncome}",
                 labels={'DISP_INCOME': 'Real Disposable Income Per Capita ($USD)', 'PCE': 'Personal Consumption Expenditures (Billion USD$)', 'DATE': 'Year'},
                 template="plotly_dark")
fig6 = px.scatter(merged_df_EmploymentLevel, x='EMP_LEV', y='PCE', color='DATE',
                 title=f"Correlation between Consumer Spending and Employment Level: {corrEmployment}",
                 labels={'EMP_LEV': 'Employment Level (Thousands of workers)', 'PCE': 'Personal Consumption Expenditures (Billion USD$)', 'DATE': 'Year'},
                 template="plotly_dark")
# Show the plot
fig1.update_layout(
    font=dict(
        size=16,  # Set the font size here
    )
)
fig2.update_layout(
    font=dict(
        size=16,  # Set the font size here
    )
)
fig3.update_layout(
    font=dict(
        size=16,  # Set the font size here
    )
)
fig4.update_layout(
    font=dict(
        size=16,  # Set the font size here
    )
)
fig5.update_layout(
    font=dict(
        size=16,  # Set the font size here
    )
)
fig6.update_layout(
    font=dict(
        size=16,  # Set the font size here
    )
)
# fig1.show()
# fig2.show()
# fig3.show()
# fig4.show()
# fig5.show()
fig6.show()
