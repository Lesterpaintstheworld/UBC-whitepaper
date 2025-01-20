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
    
    # Calculate prices
    prices = [calculate_price(s) for s in supply]
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    plt.plot(supply, prices, 'b-', linewidth=2)
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Labels and title
    plt.title('UBC Bonding Curve', fontsize=16, pad=20)
    plt.xlabel('Supply', fontsize=12)
    plt.ylabel('Price ($COMPUTE)', fontsize=12)
    
    # Format y-axis to show prices clearly
    plt.yscale('log')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))
    
    # Add key price points annotations
    for i in range(0, 1000001, 200000):
        if i < len(supply):
            price = calculate_price(i)
            plt.scatter(i, price, color='red', zorder=5)
            plt.annotate(f'${price:.2f}', 
                        (i, price),
                        xytext=(10, 10),
                        textcoords='offset points')

    # Save the plot
    plt.savefig('bonding_curve.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_curve()
