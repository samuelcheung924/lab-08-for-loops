mydata = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}

mykeys = []
myvalues = []

for k, v in mydata.items():
  print('key:', k, ', value:', v)
  mykeys.append(k)
  myvalues.append(v)

print('All keys: ',mykeys)
print('All values: ',myvalues)
