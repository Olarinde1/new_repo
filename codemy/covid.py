from covid import Covid



cov = Covid()
cases = cov.get_status_by_country_name('Nigeria')
for x in cases: 
    print(x)