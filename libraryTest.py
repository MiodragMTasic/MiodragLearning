
try:
    import MiodragLearning as ml
    print("Library imported successfully!")
except ImportError as e:
    print(f"Import error: {e}")

def main():
    
    # Problem 1: Probability Bounds
    print("Problem 1: Probability Bounds")
    print("(a) Using Markov's inequality")
    print("Answer: ", ml.probability_bounds.markov_inequality_upperbound(0.3, 0.6))

    print("(b) Using Chebyshev's inequality")
    print("Answer: ", ml.probability_bounds.chebyshev_inequality_upperbound(0.3, 0.6, 1))

    print("(c) Using Chernoff Bound")
    print("Answer: ", ml.probability_bounds.chernoff_inequality_upperbound(0.3, 0.6, 1))
    
    # Problem 2: Random Load-Balancing
    print("\nProblem 2: Random Load-Balancing")
    print("Answer: ", ml.load_balancing.random_load_balancing(10, 10000, 1200))
    
    # Problem 3: Sampling Theorem
    print("\nProblem 3: Sampling Theorem")
    print("Answer: ", ml.sampling.samplingTheorem(0.05, 0.93))
    
    # Problem 4: 3SAT Problem
    print("\nProblem 4: 3SAT Problem")
    print("Answer: ", ml.sat_problem.satisfying3SATProblem(100, 400, 0.5))
    
    # Problem 5: Entropy
    print("\nProblem 5: Entropy")
    print("(a) Compute and compare entropies of two biased 4-sided dice")
    print("Answer (i): ", ml.entropy.entropyDice([1/2, 1/6, 1/6, 1/6]))
    print("Answer (ii): ", ml.entropy.entropyDice([2/5,2/5,1/10,1/10]))
    print("Comparison of dice(i) versus dice(ii): ", ml.entropy.compareEntropies(ml.entropy.entropyDice([1/2, 1/6, 1/6, 1/6]), ml.entropy.entropyDice([2/5,2/5,1/10,1/10]), 6))
    print("(b) Entropy of the random variable X")
    print("Answer: ", ml.entropy.entropyOfSpecificValueForFairDice(6))

    # Problem 6: ID3 Greedy Algorithm
    print("\nProblem 6: ID3 Greedy Algorithm")
    print("Generate a decision tree for inputted data set, using ID3 Greedy Algorithm. First column must be row numbers. Final column must be concept class.")
    data = [
        ['Row','Age','Employed','Gender','Credit-Score','Approved?'],
        ['1','Young','False','Male','High','No'],
        ['2','Young','True','Male','High','Yes'],
        ['3','Young','True','Female','Low','Yes'],
        ['4','Young','False','Female','Fair','No'],
        ['5','Middle-aged','False','Male','High','No'],
        ['6','Middle-aged','True','Male','Low','Yes'],
        ['7','Middle-aged','False','Black-Ops2','Fair','Yes'],
        ['8','Senior','False','Black-Ops2','High','Yes'],
        ['9','Senior','False','Male','Fair','Yes'],
        ['10','Senior','True','Male','Low','Yes']
    ]
    print("Decision Tree: \n", ml.decision_tree.id3GreedyAlgorithm(data))

if __name__ == "__main__":
    main()