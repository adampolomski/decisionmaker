# Decision maker
This is a solution to decision making challange.

I treated the task as two criteria optimisation problem. Expected gain is being maximized, while minimising the risk determined by some scalar value.
I chose to use standard deviation as a risk metric, as in classical Markovitz approach for asset allocations.

Lets define our random variable, as "maximal value observed in remaining match proposals". I assumed that each legitimate match can occur with equal probability.
In any point of time, when decision is required, there are two possible choices:
- Go for the possible match. In this case we know for sure what our expected gain is, with no risk at all.
- Wait for a better option. Here expected gain is equal to expected value of our random variable, while risk is measured by standard deviation.

In order to compare these two vectors, I calculate weighted sum with an arbitrary parameter alpha (weight). By manipulating with this value, we can simulate different tendency to risk taking. 