def progressoes(a1, r, n):
   
    an_pa = a1 + (n - 1) * r
    an_pg = a1 * r**(n - 1)

    sm_pa = n * (a1 + an)/2
    sm_pg = a1 * (r**n - 1)/ r - 1 

if an_pa > an_pg and n = 9:
   return sm_pa
else: 
   return sm_pg
    
