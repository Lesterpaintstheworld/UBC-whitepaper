import matplotlib.pyplot as plt
import numpy as np

def create_revenue_charts():
    # Create charts for 0%, 50%, and 100% autonomy levels
    autonomy_levels = [0, 50, 100]
    
    for autonomy in autonomy_levels:
        plt.figure(figsize=(10, 8))
        
        # Calculate distributions based on autonomy
        if autonomy == 0:
            sizes = [50, 50, 0, 0]  # [UBC Burn, Team Share, Partner Burn, Shareholder Share]
            labels = ['UBC Burn', 'Team Share', 'Partner Token Burn', 'Shareholder Share']
        elif autonomy == 50:
            sizes = [25, 25, 25, 25]
            labels = ['UBC Burn', 'Team Share', 'Partner Token Burn', 'Shareholder Share']
        else:  # 100% autonomy
            sizes = [0, 0, 50, 50]
            labels = ['UBC Burn', 'Team Share', 'Partner Token Burn', 'Shareholder Share']
        
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title(f'Revenue Distribution at {autonomy}% Autonomy')
        plt.axis('equal')
        plt.savefig(f'revenue_distribution_{autonomy}.png', bbox_inches='tight', dpi=300)
        plt.close()

def create_fee_charts():
    # Primary Market Fees
    plt.figure(figsize=(10, 8))
    primary_sizes = [2.5, 2.5]  # [Partner, Platform]
    primary_labels = ['Partner Fee (2.5%)', 'Platform Fee (2.5%)']
    colors = ['#ff9999', '#66b3ff']
    
    plt.pie(primary_sizes, labels=primary_labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Primary Market Fee Distribution')
    plt.axis('equal')
    plt.savefig('primary_market_fees.png', bbox_inches='tight', dpi=300)
    plt.close()
    
    # Secondary Market Fees
    plt.figure(figsize=(10, 8))
    secondary_sizes = [2, 1, 2]  # [Partner, Platform, Investor]
    secondary_labels = ['Partner Fee (2%)', 'Platform Fee (1%)', 'Investor Fee (2%)']
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    
    plt.pie(secondary_sizes, labels=secondary_labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Secondary Market Fee Distribution')
    plt.axis('equal')
    plt.savefig('secondary_market_fees.png', bbox_inches='tight', dpi=300)
    plt.close()

def create_compute_burn_chart():
    # Weekly Compute Burn System
    plt.figure(figsize=(10, 8))
    burn_sizes = [50, 50]  # [Burn, UBC Purchase]
    burn_labels = ['Permanent Burn (50%)', 'UBC Purchase (50%)']
    colors = ['#ff9999', '#66b3ff']
    
    plt.pie(burn_sizes, labels=burn_labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Weekly Unstaked $COMPUTE Distribution')
    plt.axis('equal')
    plt.savefig('compute_burn_system.png', bbox_inches='tight', dpi=300)
    plt.close()

def main():
    # Set style for all plots
    plt.style.use('seaborn')
    
    # Generate all charts
    create_revenue_charts()
    create_fee_charts()
    create_compute_burn_chart()

if __name__ == "__main__":
    main()
