def digital_root(n):
  sum_n = 0
  while True:
    for i in str(n):
        sum_n += int(i)
    if sum_n<10:
        return sum_n
    else:
        n= sum_n
        sum_n=0
  return sum_n

#test.assert_equals(digital_root(16), 7)
#      test.assert_equals(digital_root(942), 6)
#     test.assert_equals(digital_root(132189), 6)
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))

n=942
print(list(map(int,str(n))))

