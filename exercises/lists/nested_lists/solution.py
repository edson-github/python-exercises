#!/usr/bin/env python
# coding=utf-8

scores_stats = [[input(), float(input())] for _ in range(int(input()))]
# Make a unique list of score, sort it and get the lowest second score
second_lowest = sorted(list({score for name, score in scores_stats}))[1]

# Iterate over the list of scores and names and print every match to the
# lowest score we got above
print('\n'.join([a for a,b in sorted(scores_stats) if b == second_lowest]))
