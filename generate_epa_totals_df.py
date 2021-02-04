import pandas as pd

def generate_epa_totals_df():
    df = pd.read_csv('epa_budget_updated.csv')

    #convert amounts from thousands of dollars to dollars
    df['Actuals'] = df['Actuals']*1000
    df['Annualized_CR'] = df['Annualized_CR']*1000
    df['PresBud'] = df['PresBud']*1000
    df['PresBud_vs_Annualized_CR'] = df['PresBud_vs_Annualized_CR']*1000
    df['Enacted'] = df['Enacted']*1000
    df['PresBud_vs_Enacted'] = df['PresBud_vs_Enacted']*1000

    #EPA Totals Data
    epa_totals = df[df['Sub-Program Project'].str.contains(pat = 'TOTAL, EPA', na=False)]
    epa_totals = epa_totals.groupby('Year').tail(1)

    epa_totals.to_csv('epa_totals.csv')

if __name__ == '__main__':
    generate_epa_totals_df()
