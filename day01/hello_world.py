i = 0
result_sum = 0
odd_sum = 0
even_sum = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        even_sum += i
        result_sum += i
    else:
        odd_sum += i
        result_sum -= i

print(result_sum, odd_sum, even_sum)
