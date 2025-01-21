import numpy as np
import matplotlib.pyplot as plt

def calculate_price(supply):
    # Normalize supply to 0-1 range
    x = supply/100000
    
    # Base price calculation
    base_price = 1 + 999 * (0.4 * x + 0.6 * x**1.8)
    
    # Add sinusoidal variation
    frequency = 2 * np.pi / 5000  # Complete one cycle every 5000 tokens
    volatility = 0.3
    sinusoidal_factor = 1 + volatility * np.sin(frequency * supply)
    
    return base_price * sinusoidal_factor

def generate_curve():
    # Create supply points (0 to 100k tokens)
    supply = np.linspace(0, 100000, 1000)
    
    # Calculate prices with built-in sinusoidal variation
    prices = [calculate_price(s) for s in supply]
    
    # Create the plot
    plt.figure(figsize=(5, 3))  # Smaller size
    
    # Plot the bonding curve
    plt.plot(supply, prices, '-', linewidth=1.5, label='Bonding Curve', color='#4d94ff')
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Labels and title
    plt.title('UBC Bonding Curve', fontsize=10, pad=10)
    plt.xlabel('Supply', fontsize=8)
    plt.ylabel('Price', fontsize=8)
    
    # Set y-axis limits
    plt.ylim(0, 1300)  # Maximum theoretical price is 1000 * 1.3
    
    # Add trading cycle markers
    for cycle in range(0, 100001, 5000):
        if cycle < len(supply):
            base_price = calculate_price(cycle)
            plt.axvline(x=cycle, color='#ff9999', linestyle='--', alpha=0.2)
            if cycle % 20000 == 0:  # Label fewer points to avoid crowding
                plt.annotate(f'${base_price:.0f}',  # Remove decimal places for larger numbers
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
