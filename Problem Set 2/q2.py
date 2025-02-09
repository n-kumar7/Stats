import pandas as pd

# Load the SPY data (Make sure the file is in the same directory as this script)
file_path = "./data/SPYdata.csv"
spy_data = pd.read_csv(file_path)

# Extract monthly percentage returns
monthly_returns = spy_data["SPY.Close"]

# Compute statistics
mean_return = monthly_returns.mean()  # Mean monthly return (%)
std_dev_return = monthly_returns.std()  # Standard deviation of monthly returns (%)

# Define confidence intervals (95% = ±2 standard deviations)
ci_95_lower = mean_return - 2 * std_dev_return
ci_95_upper = mean_return + 2 * std_dev_return

# Simulation parameters
initial_investment = 100000  # Starting value
months = 240  # 20 years

# Convert percentage returns to decimal and compute cumulative return over 240 months
cumulative_return_95_lower = (1 + ci_95_lower / 100) ** months
cumulative_return_95_upper = (1 + ci_95_upper / 100) ** months
cumulative_return_mean = (1 + mean_return / 100) ** months

# Compute final account values
final_value_95_lower = initial_investment * cumulative_return_95_lower
final_value_95_upper = initial_investment * cumulative_return_95_upper
final_value_95_mean = initial_investment * cumulative_return_mean

# Display results
print("Basic Stats:")
print(f"Mean Return: {mean_return}%")
print(f"standard deviation of return: {std_dev_return}")
print()
print(f"95% Confidence Interval for Monthly Return:")
print(f"Lower Bound: {ci_95_lower}")
print(f"Upper Bound: {ci_95_upper}")
print()
print("95% Confidence Interval for Final Investment Value (after 20 years):")
print(f"Lower Bound: ${final_value_95_lower:,.2f}")
print(f"Upper Bound: ${final_value_95_upper:,.2f}")
print(f"mean based return : ${final_value_95_mean:,.2f}")