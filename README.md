## Project: Market Basket Analysis

This project implements a Python script to analyze a market basket dataset and generate association rules. The script performs the following tasks:

* Imports libraries like pandas, NumPy, and mlxtend
* Reads the CSV data file containing transactional records
* Preprocesses the data by:
    * Changing the data type of the 'Price' column to float
    * Calculating the total price (quantity * price)
    * Dropping irrelevant columns like 'Country'
    * Handling missing values and data inconsistencies
    * Removing rows with invalid entries (e.g., negative price, quantity less than 1)
* Creates a second copy of the data for association rule generation
* Filters the data based on item and bill frequency to focus on relevant transactions
* Generates a pivot table to identify co-occurrences of items in customer bills
* Uses the mlxtend library to find frequent itemsets and association rules
* Sets minimum support and confidence thresholds to filter relevant rules
* Sorts the results by confidence, lift, and support for better readability
* Exports the association rules to a CSV file (Optional)

## Additional Information:

* This script can be used with other transactional datasets for market basket analysis.
* The project also includes a Power BI file (`project.pbix`) that utilizes the generated association rules alongside other transactional data to create meaningful data visualizations.

## How to Run the Script:

1. Ensure you have Python and the required libraries (pandas, NumPy, matplotlib, mlxtend) installed.
2. Replace the path in `data = pd.read_csv('MSB_Data.csv', sep=';',parse_dates=['Date'])` with the actual location of your CSV data file.
3. Run the script using a Python IDE or command line.
