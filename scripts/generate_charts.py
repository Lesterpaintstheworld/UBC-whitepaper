import matplotlib.pyplot as plt
import numpy as np

def create_revenue_charts():
    autonomy_levels = [0, 50, 100]
    
    for autonomy in autonomy_levels:
        plt.figure(figsize=(4, 2.5))
        
        # Calculate distributions based on autonomy
        if autonomy == 0:
            sizes = [50, 50]  # Removed 0% shares
            labels = ['UBC Burn', 'Team']  # Only show non-zero shares
        elif autonomy == 50:
            sizes = [25, 25, 25, 25]
            labels = ['UBC Burn', 'Team', 'Partner Burn', 'Shareholders']
        else:  # 100% autonomy
            sizes = [50, 50]  # Removed 0% shares
            labels = ['Partner Burn', 'Shareholders']  # Only show non-zero shares
        
        # More muted colors - adjust colors array to match the number of segments
        colors = ['#e6b3b3', '#b3d1ff', '#b3e6b3', '#ffe6b3'][:len(sizes)]
        
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)
        plt.title(f'{autonomy}% Autonomy', pad=10, fontsize=10)
        plt.axis('equal')
        plt.savefig(f'revenue_distribution_{autonomy}.png', bbox_inches='tight', dpi=300)
        plt.close()

def create_fee_charts():
    # Primary Market Fees
    plt.figure(figsize=(4, 2.5))
    primary_sizes = [2.5, 2.5]
    primary_labels = ['Partner', 'Platform']  # Shorter labels
    colors = ['#e6b3b3', '#b3d1ff']
    
    plt.pie(primary_sizes, labels=primary_labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Primary Market Fees', pad=10, fontsize=10)
    plt.axis('equal')
    plt.savefig('primary_market_fees.png', bbox_inches='tight', dpi=300)
    plt.close()
    
    # Secondary Market Fees
    plt.figure(figsize=(4, 2.5))
    secondary_sizes = [2, 1, 2]
    secondary_labels = ['Partner', 'Platform', 'Investor']  # Shorter labels
    colors = ['#e6b3b3', '#b3d1ff', '#b3e6b3']
    
    plt.pie(secondary_sizes, labels=secondary_labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Secondary Market Fees', pad=10, fontsize=10)
    plt.axis('equal')
    plt.savefig('secondary_market_fees.png', bbox_inches='tight', dpi=300)
    plt.close()

def create_compute_burn_chart():
    plt.figure(figsize=(4, 2.5))
    burn_sizes = [50, 50]
    burn_labels = ['Burn', 'UBC Purchase']  # Shorter labels
    colors = ['#e6b3b3', '#b3d1ff']
    
    plt.pie(burn_sizes, labels=burn_labels, colors=colors, autopct='%1.0f%%', startangle=90)
    plt.title('Weekly $COMPUTE Distribution', pad=10, fontsize=10)
    plt.axis('equal')
    plt.savefig('compute_burn_system.png', bbox_inches='tight', dpi=300)
    plt.close()

def main():
    # Set default style parameters
    plt.rcParams['font.size'] = 8  # Smaller default font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['figure.facecolor'] = 'white'
    
    # Generate all charts
    create_revenue_charts()
    create_fee_charts()
    create_compute_burn_chart()

if __name__ == "__main__":
    main()
