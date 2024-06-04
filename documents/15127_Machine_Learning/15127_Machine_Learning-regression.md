# Regression 

## What Is Regression?

Regression is to relate input variables to the output variable, to either predict outputs for new inputs and/or to understand the effect of the input on the output.

## Dataset For Regression

In regression, data consists of pairs (xn, yn), where yn is the n'th output and xn is a vector of D inputs. The number of pairs N is the data-size and D is the dimensionality.

## Two Goals Of Regression

In prediction, we wish to predict the output for a new input vector, e.g. what is the weight of a person who is 170 cm tall? 

In interpretation, we wish to understand the effect of inputs on output, e.g. are taller people heavier too?

## The Regression Function

For both the goals, we need to find a function that approximates the output "well enough" given inputs.

$$y_{n}\approx f(\mathbf{x}_{n}),\mathrm{~for~all~}n$$

## Additional Notes Correlation ̸= Causation

Regression finds correlation not a causal relationship, so interpret your results with caution.

## Machine Learning Jargon For Regression

Input variables are also known as features, covariates, independent variables, explanatory variables, exogenous variables, predictors, regressors.

Output variables are also known as target, label, response, outcome, dependent variable, endogenous variables, measured variable, regressands.
