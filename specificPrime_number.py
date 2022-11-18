def Specitif_Prime_Number(n):
  filter = [True] * 1000000
  for i in range(2, len(sieve)):
    if sieve[i] == True:
      for j in range(i+i, len(sieve), i):
        sieve[j] = False
      
      prime_list = [i for i in range(2, len(sieve)) if sieve == True]
      
      result = prime_list[n-1]

print(Specific_Prime_Number(78))
