import numpy as np
import matplotlib.pyplot as plt

def calculate_price(supply):
    initial_price = 1
    growth_rate = 0.35
    step_size = 50000
    return initial_price * (1 + growth_rate) ** (supply / step_size)

def generate_curve():
    # Create supply points (0 to 1M tokens)
    supply = np.linspace(0, 1000000, 1000)
    
    # Calculate base prices
    base_prices = [calculate_price(s) for s in supply]
    
    # Calculate volatility bands (±30%)
    upper_prices = [p * 1.3 for p in base_prices]
    lower_prices = [p * 0.7 for p in base_prices]
    
    # Create the plot
    plt.figure(figsize=(15, 10))
    
    # Plot volatility band
    plt.fill_between(supply, lower_prices, upper_prices, alpha=0.2, color='gray', label='Trading Range (±30%)')
    
    # Plot base curve
    plt.plot(supply, base_prices, 'b-', linewidth=2, label='Base Price')
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Labels and title
    plt.title('UBC Bonding Curve with Trading Cycles', fontsize=16, pad=20)
    plt.xlabel('Supply', fontsize=12)
    plt.ylabel('Price ($COMPUTE)', fontsize=12)
    
    # Add trading cycle markers
    for cycle in range(0, 1000001, 50000):
        if cycle < len(supply):
            base_price = calculate_price(cycle)
            plt.axvline(x=cycle, color='r', linestyle='--', alpha=0.3)
            plt.annotate(f'Cycle {cycle//50000}\n${base_price:.2f}', 
                        (cycle, base_price),
                        xytext=(10, 10),
                        textcoords='offset points',
                        fontsize=8)
    
    # Add legend
    plt.legend()
    
    # Format axes
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:.2f}'))
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
    
    # Save the plot
    plt.savefig('bonding_curve.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_curve()
