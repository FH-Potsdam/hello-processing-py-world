h = hour()
m = minute()
s = second()

cross_sum_str =  str(h) + str(m) +str(s) 
cross_sum = sum(int(x) for x in str(cross_sum_str))
print cross_sum
