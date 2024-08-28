# Probability Theory Library

This library provides various functions for probability theory and information theory calculations, including probability bounds, load balancing, sampling, SAT problems, entropy calculations, and decision tree algorithms.

Based on Assignment 1 for an AI(lv.2) course I had taken during the summer of 2024.

## Installation

You can install this library using pip:

```
pip install probability_theory_lib
```

## Usage

Here's a quick example of how to use some of the functions in this library:

```python
from probability_theory_lib import probability_bounds as pb
from probability_theory_lib import entropy

# Calculate Markov's inequality upper bound
markov_bound = pb.markov_inequality_upperbound(0.3, 0.6)
print(f"Markov's inequality upper bound: {markov_bound}")

# Calculate entropy of a biased 4-sided die
die_probabilities = [1/2, 1/6, 1/6, 1/6]
die_entropy = entropy.entropyDice(die_probabilities)
print(f"Entropy of the biased die: {die_entropy}")
```

For more detailed usage instructions and examples, please refer to the documentation of each module.

## ID3 Algorithm
Um.. not great in the current version. If you can find the fix feel free to submit a Pull request !

## License

This project is licensed under the MIT License.

## Author

Miodrag Tasic

## Contact

For any questions or feedback, please contact miodragmtasic@gmail.com.
