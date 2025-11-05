Aim:

To design a Python application using NumPy that simulates random coin flips and dice rolls,
analyzes the outcomes, and displays the probabilities of each event.

Algorithm:

1. Start the program.

2. Import the required library — numpy.

3. Input the number of simulations (number of flips/rolls).

4. For coin flip simulation:
 - Use numpy.random.choice(['Heads', 'Tails'], size=n) to generate random results.
 - Count the occurrences of “Heads” and “Tails”.

5. For dice roll simulation:
 - Use numpy.random.randint(1, 7, size=n) to simulate dice outcomes (1 to 6).
 - Count the frequency of each face.

6. Display the outcomes and probabilities for both simulations.

7. End the program.

Python Program:
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
Sample Output:
Enter number of simulations: 10
Coin Flip Simulation:
Total Flips: 10
Heads: 6 (60.00%)
Tails: 4 (40.00%)
Dice Roll Simulation:
Total Rolls: 10
Face 1: 1 (10.00%)
Face 2: 3 (30.00%)
Face 3: 2 (20.00%)
Face 4: 1 (10.00%)
Face 5: 2 (20.00%)
Face 6: 1 (10.00%)
