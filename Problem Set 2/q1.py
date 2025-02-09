import pandas as pd
import numpy as np

# Load the CSV file
file_path = "./data/ETFdata.csv"  # Replace with actual path if running locally
df = pd.read_csv(file_path)

# Define portfolio weights (from 0% VTI to 100% VTI, in 10% increments)
weights_vti = np.linspace(0, 1, 11)  # 11 points from 0 to 1 in 10% increments
weights_vglt = 1 - weights_vti  # Complementary weights for VGLT

# Calculate expected returns and standard deviations
mean_vti = df["VTI.Close"].mean()
mean_vglt = df["VGLT.Close"].mean()
std_vti = df["VTI.Close"].std()
std_vglt = df["VGLT.Close"].std()
corr_matrix = df.corr()
corr_vti_vglt = corr_matrix.loc["VTI.Close", "VGLT.Close"]

# Calculate portfolio statistics
portfolio_returns = weights_vti * mean_vti + weights_vglt * mean_vglt
portfolio_volatility = np.sqrt(
    (weights_vti ** 2) * (std_vti ** 2) +
    (weights_vglt ** 2) * (std_vglt ** 2) +
    2 * weights_vti * weights_vglt * std_vti * std_vglt * corr_vti_vglt
)

# Compute Sharpe Ratios (assuming risk-free rate is 0%)
sharpe_ratios = portfolio_returns / portfolio_volatility

# Create a DataFrame for the Efficient Frontier (10% increments)
efficient_frontier_df = pd.DataFrame({
    "Weight VTI": weights_vti,
    "Weight VGLT": weights_vglt,
    "Expected Return (%)": portfolio_returns,  # Convert to percentage
    "Portfolio Volatility (%)": portfolio_volatility,  # Convert to percentage
    "Sharpe Ratio": sharpe_ratios
})

# Display the DataFrame
print(efficient_frontier_df)
