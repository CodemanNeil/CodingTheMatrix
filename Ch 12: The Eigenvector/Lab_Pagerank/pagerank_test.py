from mat import Mat
#test case
from pagerank_lab import make_Markov

D = set(range(1,7))
f = [(1,1),(1,4),(2,3),(2,4),(2,5),(2,6),(3,2),(4,5),(5,6),(6,5)]
small_links = Mat((D, D), {x:1 for x in f})
A2= Mat(small_links.D, {(r, c):1/6 for r in small_links.D[0] for c in small_links.D[1]})

make_Markov(small_links)
print(small_links)

#normalize(ra)
#pra = power_method(ra,d,250)
