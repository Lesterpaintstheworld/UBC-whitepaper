import numpy as np
import matplotlib.pyplot as plt

def calculate_price(supply):
    initial_price = 1
    growth_rate = 0.35
    step_size = 5000
    volatility = 0.3
    
    # Base exponential growth
    base_price = initial_price * (1 + growth_rate) ** (supply / step_size)
    
    # Add sinusoidal variation to the base price
    frequency = 2 * np.pi / step_size  # Complete one cycle every 50,000 tokens
    sinusoidal_component = base_price * volatility * np.sin(frequency * supply)
    
    return base_price + sinusoidal_component

def generate_curve():
    # Create supply points (0 to 100k tokens)
    supply = np.linspace(0, 100000, 1000)
    
    # Calculate prices with built-in sinusoidal variation
    prices = [calculate_price(s) for s in supply]
    
    # Create the plot
    plt.figure(figsize=(5, 3))  # Smaller size
    
    # Plot the bonding curve
    plt.plot(supply, prices, 'b-', linewidth=1.5, label='Bonding Curve', color='#4d94ff')
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Labels and title
    plt.title('UBC Bonding Curve', fontsize=10, pad=10)
    plt.xlabel('Supply', fontsize=8)
    plt.ylabel('Price', fontsize=8)
    
    # Add trading cycle markers
    for cycle in range(0, 100001, 5000):
        if cycle < len(supply):
            base_price = calculate_price(cycle)
            plt.axvline(x=cycle, color='#ff9999', linestyle='--', alpha=0.2)
            if cycle % 10000 == 0:  # Label every other cycle
                plt.annotate(f'${base_price:.1f}', 
                            (cycle, base_price),
                            xytext=(5, 5),
                            textcoords='offset points',
                            fontsize=6)
    
    # Add legend
    plt.legend()
    
    # Format axes
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:.2f}'))
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
    
    # Save the plot
    # Tighter layout
    plt.tight_layout()
    plt.savefig('bonding_curve.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_curve()
