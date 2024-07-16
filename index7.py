salary = [340 ,210 ,450, 600, 230, 500, 550, 300]
shumaEpagave = 0
for y in salary:
    shumaEpagave = shumaEpagave + y
print(f"shuma e pagave eshte: {shumaEpagave}")
pagamesatare = shumaEpagave / len(salary)
print(pagamesatare)

pagaMin = salary[0]
for pagaaktuale in salary :
    if(pagaaktuale < pagaMin):
        pagaMin = pagaaktuale
print(f"paga minimale eshte : {pagaMin}")

pagaMin = salary[0]
for pagaaktuale in salary :
    if(pagaaktuale > pagaMin):
        pagaMin = pagaaktuale
print(f"paga maksimale eshte : {pagaMin}")

