#this code might not perfect so just refer partially.

def factorization(n):
  filter = [True] * (n+1)
  for i in range(2, n+1):
    if filter[i] == True:
      for j in range(i+i, (n+1), i):
        filter[j] = False
        
  prime_list = [i for i in range(2, n+1) if filter[i] == True]
  
  for p in prime_list:
    if n % p == 0:
      result = p
  return result

print(factorization(723956))
