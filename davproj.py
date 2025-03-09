import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:\Python\DAVproj1\customers-100.csv')

# 1. Display brief information about the dataset
df.info()

# 2. Fetch the first and last ten rows of the dataframe
print("First 10 rows:")
print(df.head(10))
print("Last 10 rows:")
print(df.tail(10))

# 3. Determine data type of specific columns
print("Data types:")
print(df[['Customer Id', 'First Name', 'Last Name', 'Company', 'Country']].dtypes)

# 4. Create new dataset with selected columns
new_df = df[['Customer Id', 'First Name', 'Last Name', 'Company', 'Country']]

# 5. Extract details of specific customers by ID
print(df.loc[df['Customer Id'] == 'DD37Cf93aecA6Dc', ['First Name', 'Last Name', 'Company']])
print(df.loc[df['Customer Id'] == '1Ef7b82A4CAAD10', ['Email', 'Subscription Date']])

# 6. Group customers by country
grouped_countries = df.groupby('Country')
for name, group in grouped_countries:
    print(f"Country: {name}, Total Customers: {len(group)}")

# 7. Count the number of customers per country
country_counts = df['Country'].value_counts()
print(country_counts)

# 8. Plot top 5 countries with most customers
top_5_countries = country_counts.head(5)
top_5_countries.plot(kind='bar', title='Top 5 Countries by Customer Count')
plt.xlabel('Country')
plt.ylabel('Number of Customers')
plt.show()

# 9. Extract email domain and analyze common providers
df['Email Domain'] = df['Email'].apply(lambda x: x.split('@')[-1])
domain_counts = df['Email Domain'].value_counts().head(5)
print("Top 5 Email Domains:")
print(domain_counts)

domain_counts.plot(kind='bar', title='Top 5 Email Providers')
plt.xlabel('Email Provider')
plt.ylabel('Number of Customers')
plt.show()

# 10. Pie chart for company distribution
top_companies = df['Company'].value_counts().head(5)
top_companies.plot(kind='pie', autopct='%1.1f%%', title='Top 5 Companies by Customer Count')
plt.ylabel('')
plt.show()
