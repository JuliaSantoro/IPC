def progressoes(a1, r, n):
   
    an_pa = a1 + (n - 1) * r

    q = (an_pa / a1) ** (1 / (n - 1))

    sn_pa = n * (a1 + an_pa)

    sn_pg = a1 * ((q ** n) - 1) / (q - 1)

    if an_pa > a1 * (q ** (n - 1)):
        return int(sn_pa)
    else:
        return int(sn_pg)
