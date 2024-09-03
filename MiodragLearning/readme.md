# MiodragLearning Library

This library provides various functions for probability theory and information theory calculations, including probability bounds, load balancing, sampling, SAT problems, entropy calculations, and decision tree algorithms.

## Installation

You can install this library using pip:

```
pip install miodraglearning
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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

Miodrag Tasic

## Contact

For any questions or feedback, please contact miodragmtasic@gmail.com.
