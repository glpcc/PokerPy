import poker_probs
from time import perf_counter_ns
a = [poker_probs.Card(1,2),poker_probs.Card(2,2),poker_probs.Card(7,1),poker_probs.Card(7,2),poker_probs.Card(13,3),poker_probs.Card(1,1),poker_probs.Card(10,0)]
b = poker_probs.Hand('test',a[0:5])
t1 = perf_counter_ns()
print(poker_probs.calculate_hand_frecuency(a,2))
print(perf_counter_ns()-t1)