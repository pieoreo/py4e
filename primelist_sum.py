# indentation might not be correct
def prime_list_sum(n):
  filter = [True] * (n+1)
  for i in range(2, n+1):
    if filter[i] == True:
      for j in range(i+i, (n+1), i):
        filter[j] = False
  prime_list = [i for i in range(2, n+1) if filter[i] == True]
  result = sum(prime_list)
  return result
print(prime_list_sum(549))  
  
