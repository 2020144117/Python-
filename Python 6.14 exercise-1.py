str = 'X-DSPAM-Confidence:0.8475'
str = str.split(':')[1]
result = float(str)
print(result)