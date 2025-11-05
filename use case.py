import numpy as np
# Function for simulating coin flips
def simulate_coin_flips(n):
 outcomes = np.random.choice(['Heads', 'Tails'], size=n)
 heads = np.count_nonzero(outcomes == 'Heads')
 tails = np.count_nonzero(outcomes == 'Tails')
 print("\nCoin Flip Simulation:")
 print(f"Total Flips: {n}")
 print(f"Heads: {heads} ({heads/n:.2%})")
 print(f"Tails: {tails} ({tails/n:.2%})")
# Function for simulating dice rolls
def simulate_dice_rolls(n):
 rolls = np.random.randint(1, 7, size=n)
 print("\nDice Roll Simulation:")
 print(f"Total Rolls: {n}")
 for i in range(1, 7):
 count = np.count_nonzero(rolls == i)
 print(f"Face {i}: {count} ({count/n:.2%})")
# Main program
def main():
 n = int(input("Enter number of simulations: "))
 simulate_coin_flips(n)
 simulate_dice_rolls(n)
if __name__ == "__main__":
 main()
