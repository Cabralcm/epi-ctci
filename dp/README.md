# Dynamic Programming

## Notes on DP

https://stackoverflow.com/questions/6184869/what-is-the-difference-between-memoization-and-dynamic-programming

Memoization is a term describing an optimization technique where you cache previously computed results, and return the cached result when the same computation is needed again.

Dynamic programming is a technique for solving problems of recursive nature, iteratively and is applicable when the computations of the subproblems overlap.

Dynamic programming is typically implemented using tabulation, but can also be implemented using memoization. So as you can see, neither one is a "subset" of the other.

A reasonable follow-up question is: What is the difference between tabulation (the typical dynamic programming technique) and memoization?

When you solve a dynamic programming problem using tabulation you solve the problem "bottom up", i.e., by solving all related sub-problems first, typically by filling up an n-dimensional table. Based on the results in the table, the solution to the "top" / original problem is then computed.

If you use memoization to solve the problem you do it by maintaining a map of already solved sub problems. You do it "top down" in the sense that you solve the "top" problem first (which typically recurses down to solve the sub-problems).

### DP - Memoization vs Tabulation (Top-down vs Bottom-up):

* If all subproblems must be solved at least once, a bottom-up dynamic-programming algorithm usually outperforms a top-down memoized algorithm by a constant factor
* No overhead for recursion and less overhead for maintaining table
* There are some problems for which the regular pattern of table accesses in the dynamic-programming algorithm can be exploited to reduce the time or space requirements even further
* If some subproblems in the subproblem space need not be solved at all, the memoized solution has the advantage of solving only those subproblems that are definitely required
