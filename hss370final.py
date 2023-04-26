import pandas as pd
import plotly.express as px

consumer = pd.read_csv("Affinity - State - Daily.csv")
# consumer.info()

consumer_subset = consumer.loc[(consumer["year"] > 2018) & (consumer["year"] < 2022)]
consumer_subset.info()
consumer_subset = consumer_subset[consumer_subset.spend_retail_no_grocery != "."]
consumer_subset["spend_retail_no_grocery"] = consumer_subset["spend_retail_no_grocery"].astype("float64")
consumer_subset["spend_grf"] = consumer_subset["spend_grf"].astype("float")
corr = consumer_subset["spend_grf"].corr(consumer_subset["spend_retail_no_grocery"])
consumer_spending = px.scatter(consumer_subset, x="spend_grf", y="spend_retail_no_grocery", template="plotly_dark",
                               color="statefips", facet_col="year",
                               labels={"spend_grf": "Money spent on Groceries", "spend_retail_no_grocery":
                                   "Money spent on Retail", "statefips": "State Codes"},
                               title=f'Correlation: {corr}')
consumer_spending.show()

# creating choropleth
# consumer_choropleth = px.choropleth(consumer_subset, locations="statefips", locationmode="USA-states",
#                                     color="spend_retail_no_grocery",
#                                     scope="usa", labels={"spend_retail_no_grocery": "Retail Spending"})
# consumer_choropleth.show()
