# Online Portfolio Selection



## Benchmarks:
### Buy and Hold: BAH
Never rebalances after initial purchase
### Best Stock: Best_Stock
Tracks the best performing stock in hindsight
### Constant Rebalanced Portfolio: CRP
Rebalances weight each day to a predetermined weight
### Best Constant Rebalanced Portfolio: BCRP
Tracks the best constant rebalanced portfolio in hindsight
## Follow-the-Winner: (Momentum)
### Universal Portfolio: UP
### Exponential Gradient: EG
### Follow the Leader: FTL
### Follow the Reguliarized Leader --- skip over for now (just need to add a regularization factor)
### Aggregating-type Algorithms --- skip over for now

## Follow-the-Loser: (Mean-Reversion)
### Anti Correlation
### Passive Aggressive Mean Reversion
### Confidence Weighted Mean Reversion
### Online Moving Average Reversion
### Robust Median Reversion

## Pattern-Matching:
### Nonparametric Histogram Log-optimal Strategy
### Nonparametric Histogram Log-optimal Strategy
### Nonparametric Kernel-based Log-optimal Strategy
### Nonparametric Nearest Neighbor Log-optimal Strategy
### Correlation-driven Nonparametric Learning Strategy: CORN
### Nonparametric Kernel-based Semi-log-optimal Strategy
### Nonparametric Kernel-based Markowitz-type Strategy
### Nonparametric Kernel-based GV-type Strategy

## Meta-Learning:
### Aggregating Algorithm
### Fast Universalization Algorithm
### Online Gradient Updates
### Online Newton Updates
### Follow the Leading History

## Most importantly:
### CORN-K
### RACORN-K
### SCORN-K
### FCORN-K

## Method
### Public
#### allocate
- sets all weights
#### clean_data
- clean given data to the right format
#### summary
- returns metrics