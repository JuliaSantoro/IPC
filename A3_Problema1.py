def progressoes(a1, r, n):
    # Cálculo do enésimo termo da PA
    an_pa = a1 + (n - 1) * r

    # Cálculo do enésimo termo da PG
    q = a1 * (an_pa / a1) ** (1 / (n - 1))

    # Cálculo da soma dos n primeiros termos da PA
    sn_pa = n * (a1 + an_pa)

    # Cálculo da soma dos n primeiros termos da PG
    sn_pg = a1 * (q ** n - 1) / (q - 1)

    if sn_pa > sn_pg:
        return int(sn_pa)
    else:
        return int(sn_pg)
