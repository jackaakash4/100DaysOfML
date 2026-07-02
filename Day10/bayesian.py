#Bayesian intutioon

#simple python function
#spam filter

def bayes(prior, likelihood, evidence):
    return (likelihood * prior)/evidence

prior = 0.1
likelihood = 0.90
evidence = 0.0585

posterior = bayes(
        prior,
        likelihood,
        evidence)

print("Posterior probability",posterior)

