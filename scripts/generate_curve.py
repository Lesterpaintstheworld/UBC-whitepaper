import numpy as np
import matplotlib.pyplot as plt

def calculate_price(supply):
    initial_price = 1
    growth_rate = 0.35
    step_size = 50000
    volatility = 0.3
    
    # Base exponential growth
    base_price = initial_price * (1 + growth_rate) ** (supply / step_size)
    
    # Add sinusoidal variation to the base price
    frequency = 2 * np.pi / step_size  # Complete one cycle every 50,000 tokens
    sinusoidal_component = base_price * volatility * np.sin(frequency * supply)
    
    return base_price + sinusoidal_component

def generate_curve():
    # Create supply points (0 to 1M tokens)
    supply = np.linspace(0, 1000000, 1000)
    
    # Calculate prices with built-in sinusoidal variation
    prices = [calculate_price(s) for s in supply]
    
    # Create the plot
    plt.figure(figsize=(15, 10))
    
    # Plot the bonding curve
    plt.plot(supply, prices, 'b-', linewidth=2, label='Bonding Curve')
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Labels and title
    plt.title('UBC Bonding Curve', fontsize=16, pad=20)
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
