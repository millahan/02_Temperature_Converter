def to_c(from_f):
    centigrade = (from_f - 32) / (9/5)
    return centigrade

# main routine
temperatures = [0,40,100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item,answer)
    converted.append(ans_statement)

print(converted)
