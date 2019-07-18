def list_mean(x):
     
     if x==[]:
         return "Must key in the numbers"
     i=0
     for h in x:
         i=i+h
     i=i/float(len(x))
     return i
         


print list_mean([1,2,3,4])

print list_mean([1,3,4,5,2])

print list_mean([])

print list_mean([2])
