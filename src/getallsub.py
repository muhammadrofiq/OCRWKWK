import itertools

def get_all_substrings(string, error):
  S = string
  size=int(len(string)*error)
  print size
  pruning=[]
  list(itertools.chain.from_iterable([list(itertools.combinations(S,i)) for i in range(1,len(S))]))
  combos  = list(itertools.chain.from_iterable([list(itertools.combinations(S,i)) for i in range(1,len(S))]))
  li =[''.join(c) for c in combos]
  li.append(string)
  for word in li:
      if len(word) >= size:
          pruning.append(word)
  return pruning

#print get_all_substrings('A1234BD',5)
